"""Genera la fuente reproducible del dashboard a partir de los CSV originales."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "processed" / "airbnb_dashboard.csv"
LISTING_COLUMNS = [
    "id",
    "city",
    "neighbourhood",
    "room_type",
    "price",
    "minimum_nights",
    "number_of_reviews",
    "reviews_per_month",
]


def load_listings(project_root: Path) -> pd.DataFrame:
    """Carga los seis archivos declarados en el manifiesto y conserva su ciudad."""
    manifest = pd.read_csv(project_root / "data" / "manifest.csv")
    city_frames: list[pd.DataFrame] = []

    for record in manifest.itertuples(index=False):
        source = pd.read_csv(
            project_root / record.relative_path,
            low_memory=False,
        )
        source["city"] = record.city
        city_frames.append(source)

    listings = pd.concat(city_frames, ignore_index=True, sort=False)

    missing_columns = sorted(set(LISTING_COLUMNS) - set(listings.columns))
    if missing_columns:
        raise ValueError(
            "Faltan columnas necesarias: " + ", ".join(missing_columns)
        )

    return listings[LISTING_COLUMNS].copy()


def add_listing_indicators(listings: pd.DataFrame) -> pd.DataFrame:
    """Añade indicadores simples sin corregir los valores originales."""
    enriched = listings.copy()
    enriched["review_activity_proxy"] = enriched["reviews_per_month"]

    zero_reviews_without_rate = (
        enriched["review_activity_proxy"].isna()
        & enriched["number_of_reviews"].eq(0)
    )
    enriched.loc[zero_reviews_without_rate, "review_activity_proxy"] = 0

    enriched["has_reviews"] = enriched["number_of_reviews"].gt(0)
    enriched["non_positive_price"] = enriched["price"].le(0)
    enriched["minimum_nights_over_8"] = enriched["minimum_nights"].gt(8)
    enriched["minimum_nights_1000_plus"] = enriched["minimum_nights"].ge(1000)
    enriched["reviews_without_monthly_rate"] = (
        enriched["number_of_reviews"].gt(0)
        & enriched["reviews_per_month"].isna()
    )
    enriched["has_priority_quality_issue"] = enriched[
        [
            "non_positive_price",
            "minimum_nights_1000_plus",
            "reviews_without_monthly_rate",
        ]
    ].any(axis=1)
    enriched["positive_price"] = enriched["price"].where(
        enriched["price"].gt(0)
    )

    return enriched


def neighbourhood_metrics(listings: pd.DataFrame) -> pd.DataFrame:
    """Calcula presencia y actividad por ciudad y barrio como en el EDA."""
    summary = (
        listings.groupby(["city", "neighbourhood"], as_index=False)
        .agg(
            neighbourhood_listing_count=("id", "nunique"),
            neighbourhood_median_review_activity=(
                "review_activity_proxy",
                "median",
            ),
            neighbourhood_reviewed_listing_percentage=(
                "number_of_reviews",
                lambda values: values.gt(0).mean() * 100,
            ),
            neighbourhood_missing_activity_count=(
                "review_activity_proxy",
                lambda values: values.isna().sum(),
            ),
        )
    )
    summary["neighbourhood_city_share_percentage"] = (
        summary["neighbourhood_listing_count"]
        / summary.groupby("city")["neighbourhood_listing_count"].transform("sum")
        * 100
    )

    rounded = [
        "neighbourhood_median_review_activity",
        "neighbourhood_reviewed_listing_percentage",
        "neighbourhood_city_share_percentage",
    ]
    summary[rounded] = summary[rounded].round(2)
    summary["eligible_neighbourhood"] = summary[
        "neighbourhood_listing_count"
    ].ge(100)

    return summary


def segment_metrics(listings: pd.DataFrame) -> pd.DataFrame:
    """Calcula referencias ciudad-tipo y selecciona hasta cinco segmentos por ciudad."""
    baselines = (
        listings.groupby(["city", "room_type"], as_index=False)
        .agg(
            baseline_median_price=("positive_price", "median"),
            baseline_median_activity=("review_activity_proxy", "median"),
        )
    )

    segments = (
        listings.groupby(
            ["city", "neighbourhood", "room_type"],
            as_index=False,
        )
        .agg(
            segment_listing_count=("id", "nunique"),
            segment_median_positive_price=("positive_price", "median"),
            segment_median_review_activity=("review_activity_proxy", "median"),
            segment_reviewed_listing_percentage=(
                "number_of_reviews",
                lambda values: values.gt(0).mean() * 100,
            ),
        )
        .merge(
            baselines,
            on=["city", "room_type"],
            how="left",
            validate="many_to_one",
        )
    )

    segments["segment_price_index"] = (
        segments["segment_median_positive_price"]
        / segments["baseline_median_price"]
        * 100
    )
    segments["segment_activity_difference"] = (
        segments["segment_median_review_activity"]
        - segments["baseline_median_activity"]
    )
    segments["segment_city_room_type_share_percentage"] = (
        segments["segment_listing_count"]
        / segments.groupby(["city", "room_type"])[
            "segment_listing_count"
        ].transform("sum")
        * 100
    )

    rounded = [
        "segment_median_positive_price",
        "segment_median_review_activity",
        "segment_reviewed_listing_percentage",
        "segment_price_index",
        "segment_activity_difference",
        "segment_city_room_type_share_percentage",
    ]
    segments[rounded] = segments[rounded].round(2)

    segments["meets_candidate_rule"] = (
        segments["segment_listing_count"].ge(50)
        & segments["segment_activity_difference"].gt(0)
        & segments["segment_price_index"].le(100)
    )

    selected_indexes = (
        segments.loc[segments["meets_candidate_rule"]]
        .sort_values(
            ["city", "segment_activity_difference", "segment_listing_count"],
            ascending=[True, False, False],
        )
        .groupby("city", group_keys=False)
        .head(5)
        .index
    )
    segments["selected_candidate"] = False
    segments.loc[selected_indexes, "selected_candidate"] = True

    segments["candidate_evidence"] = "No seleccionado"
    segments.loc[
        segments["selected_candidate"]
        & segments["segment_listing_count"].between(50, 99),
        "candidate_evidence",
    ] = "Exploratorio (50-99)"
    segments.loc[
        segments["selected_candidate"]
        & segments["segment_listing_count"].ge(100),
        "candidate_evidence",
    ] = "Más estable (100+)"

    return segments


def build_dashboard_data(project_root: Path) -> pd.DataFrame:
    """Combina los indicadores y agregados en una tabla a nivel de anuncio."""
    listings = add_listing_indicators(load_listings(project_root))
    neighbourhoods = neighbourhood_metrics(listings)
    segments = segment_metrics(listings)

    dashboard_data = (
        listings.merge(
            neighbourhoods,
            on=["city", "neighbourhood"],
            how="left",
            validate="many_to_one",
        )
        .merge(
            segments,
            on=["city", "neighbourhood", "room_type"],
            how="left",
            validate="many_to_one",
        )
    )
    validate_dashboard_data(dashboard_data)
    return dashboard_data


def validate_dashboard_data(data: pd.DataFrame) -> None:
    """Detiene la generación si los controles principales difieren del EDA."""
    checks = {
        "filas": len(data),
        "ids_unicos": data["id"].nunique(),
        "ciudades": data["city"].nunique(),
        "precios_no_positivos": int(data["non_positive_price"].sum()),
        "estancias_1000_plus": int(data["minimum_nights_1000_plus"].sum()),
        "resenas_sin_frecuencia": int(
            data["reviews_without_monthly_rate"].sum()
        ),
    }
    expected = {
        "filas": 220_031,
        "ids_unicos": 220_031,
        "ciudades": 6,
        "precios_no_positivos": 50,
        "estancias_1000_plus": 20,
        "resenas_sin_frecuencia": 123,
    }
    if checks != expected:
        raise ValueError(f"Controles distintos del EDA: {checks}")

    main_room_types = data["room_type"].isin(
        ["Entire home/apt", "Private room"]
    ).mean()
    if round(main_room_types * 100, 2) != 97.56:
        raise ValueError("La distribución de tipos no coincide con el EDA")

    selected = data.loc[
        data["selected_candidate"],
        ["city", "neighbourhood", "room_type"],
    ].drop_duplicates()
    expected_segments = {
        ("London", "Tower Hamlets", "Entire home/apt"),
        ("Madrid", "Embajadores", "Entire home/apt"),
        ("Milan", "CENTRALE", "Entire home/apt"),
        ("Sydney", "Auburn", "Entire home/apt"),
    }
    if not expected_segments.issubset(set(selected.itertuples(index=False, name=None))):
        raise ValueError("Faltan segmentos destacados en el EDA")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Ruta del CSV generado.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    dashboard_data = build_dashboard_data(PROJECT_ROOT)
    dashboard_data.to_csv(output, index=False, encoding="utf-8-sig")

    selected_segments = dashboard_data.loc[
        dashboard_data["selected_candidate"],
        ["city", "neighbourhood", "room_type"],
    ].drop_duplicates()

    print(f"Fuente creada: {output}")
    print(f"Filas: {len(dashboard_data):,}")
    print(f"Ciudades: {dashboard_data['city'].nunique()}")
    print(f"Segmentos seleccionados: {len(selected_segments)}")
    print("Controles: 50 precios no positivos, 20 estancias >= 1000, 123 reseñas sin frecuencia")


if __name__ == "__main__":
    main()
