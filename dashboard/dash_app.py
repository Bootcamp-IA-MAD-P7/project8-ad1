"""Dashboard web portable para explorar la oferta de Airbnb.

La aplicación reutiliza exactamente la preparación validada para Power BI. Los
datos se cargan una vez al iniciar el proceso y los filtros actualizan las
tarjetas, los gráficos y las tablas mediante un único callback.
"""

from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, Input, Output, dash_table, dcc, html
from dash.dash_table.Format import Format, Scheme


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.prepare_dashboard_data import build_dashboard_data


CITY_ORDER = ["London", "Madrid", "Milan", "New York", "Sydney", "Tokyo"]
CITY_LABELS = {
    "London": "Londres",
    "Madrid": "Madrid",
    "Milan": "Milán",
    "New York": "Nueva York",
    "Sydney": "Sídney",
    "Tokyo": "Tokio",
}
ROOM_ORDER = ["Entire home/apt", "Private room", "Shared room", "Hotel room"]
ROOM_LABELS = {
    "Entire home/apt": "Alojamiento entero",
    "Private room": "Habitación privada",
    "Shared room": "Habitación compartida",
    "Hotel room": "Habitación de hotel",
}

RAUSCH = "#ff385c"
INK = "#222222"
BABU = "#00a699"
ARCHES = "#fc642d"
AUBERGINE = "#92174d"
FOGGY = "#717171"
ROOM_COLORS = {
    "Alojamiento entero": RAUSCH,
    "Habitación privada": BABU,
    "Habitación compartida": ARCHES,
    "Habitación de hotel": AUBERGINE,
}
CITY_COLORS = {
    "Londres": RAUSCH,
    "Madrid": INK,
    "Milán": BABU,
    "Nueva York": AUBERGINE,
    "Sídney": "#6c5ce7",
    "Tokio": ARCHES,
}
ISSUE_LABELS = {
    "non_positive_price": "Precio no positivo",
    "minimum_nights_1000_plus": "Mínimo de 1.000+ noches",
    "reviews_without_monthly_rate": "Reseñas sin frecuencia mensual",
}
ISSUE_COLORS = {
    "Precio no positivo": RAUSCH,
    "Mínimo de 1.000+ noches": ARCHES,
    "Reseñas sin frecuencia mensual": BABU,
}
GRAPH_CONFIG = {
    "displaylogo": False,
    "modeBarButtonsToRemove": ["lasso2d", "select2d"],
    "responsive": True,
}


DASHBOARD_DATA = build_dashboard_data(PROJECT_ROOT)


def format_integer(value: int | float) -> str:
    """Formatea miles con punto para la interfaz en español."""
    return f"{int(value):,}".replace(",", ".")


def format_percentage(value: float) -> str:
    """Formatea porcentajes con coma decimal para la interfaz en español."""
    return f"{value:.2f}".replace(".", ",") + "%"


def apply_filters(
    data: pd.DataFrame,
    cities: list[str] | None,
    room_types: list[str] | None,
) -> pd.DataFrame:
    """Aplica los filtros seleccionados; una selección vacía equivale a todos."""
    filtered = data
    if cities:
        filtered = filtered.loc[filtered["city"].isin(cities)]
    if room_types:
        filtered = filtered.loc[filtered["room_type"].isin(room_types)]
    return filtered


def selected_cities_data(
    data: pd.DataFrame,
    cities: list[str] | None,
) -> pd.DataFrame:
    """Filtra solo por ciudad para los indicadores calculados a nivel de barrio."""
    if cities:
        return data.loc[data["city"].isin(cities)]
    return data


def empty_figure(title: str, message: str) -> go.Figure:
    """Devuelve un estado vacío comprensible para combinaciones sin datos."""
    figure = go.Figure()
    figure.add_annotation(
        text=message,
        x=0.5,
        y=0.5,
        xref="paper",
        yref="paper",
        showarrow=False,
        font={"size": 15, "color": FOGGY},
        align="center",
    )
    figure.update_layout(
        title={"text": title, "x": 0.02, "xanchor": "left"},
        template="plotly_white",
        height=390,
        margin={"l": 35, "r": 25, "t": 75, "b": 35},
        xaxis={"visible": False},
        yaxis={"visible": False},
    )
    return figure


def finish_figure(figure: go.Figure, *, y_suffix: str | None = None) -> go.Figure:
    """Aplica un acabado visual común y legible a todos los gráficos."""
    figure.update_layout(
        template="plotly_white",
        height=390,
        margin={"l": 55, "r": 25, "t": 82, "b": 55},
        font={
            "family": "Avenir Next, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
            "color": INK,
        },
        title={"x": 0.02, "xanchor": "left", "font": {"size": 17}},
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "left",
            "x": 0,
            "title_text": "",
        },
        hoverlabel={"bgcolor": "white", "font_size": 13},
        plot_bgcolor="white",
        paper_bgcolor="white",
    )
    figure.update_xaxes(showgrid=False, linecolor="#dddddd")
    figure.update_yaxes(gridcolor="#ebebeb", linecolor="#dddddd")
    if y_suffix:
        figure.update_yaxes(ticksuffix=y_suffix)
    return figure


def build_composition_figure(data: pd.DataFrame) -> go.Figure:
    """Muestra cómo se reparte la oferta de cada ciudad por tipo de alojamiento."""
    if data.empty:
        return empty_figure(
            "Composición de la oferta por ciudad",
            "No existen anuncios para esta combinación de filtros.",
        )

    composition = data.groupby(["city", "room_type"], as_index=False).agg(
        listing_count=("id", "nunique")
    )
    composition["city_total"] = composition.groupby("city")[
        "listing_count"
    ].transform("sum")
    composition["share_percentage"] = (
        composition["listing_count"] / composition["city_total"] * 100
    )
    composition["Ciudad"] = composition["city"].map(CITY_LABELS)
    composition["Tipo de alojamiento"] = composition["room_type"].map(
        ROOM_LABELS
    )

    figure = px.bar(
        composition,
        x="Ciudad",
        y="share_percentage",
        color="Tipo de alojamiento",
        custom_data=["listing_count", "city_total"],
        category_orders={
            "Ciudad": [CITY_LABELS[city] for city in CITY_ORDER],
            "Tipo de alojamiento": [ROOM_LABELS[room] for room in ROOM_ORDER],
        },
        color_discrete_map=ROOM_COLORS,
        labels={"share_percentage": "% de la oferta"},
        title=(
            "Composición de la oferta por ciudad"
            "<br><sup>Porcentaje sobre los anuncios visibles de cada ciudad</sup>"
        ),
    )
    figure.update_layout(barmode="stack", yaxis_range=[0, 100])
    figure.update_traces(
        hovertemplate=(
            "<b>%{x}</b><br>%{fullData.name}<br>"
            "Oferta: %{y:.2f}%<br>Anuncios: %{customdata[0]:,.0f}<br>"
            "Total visible en la ciudad: %{customdata[1]:,.0f}<extra></extra>"
        )
    )
    return finish_figure(figure, y_suffix="%")


def build_neighbourhood_figure(data: pd.DataFrame) -> go.Figure:
    """Relaciona presencia y actividad aproximada a nivel completo de barrio."""
    neighbourhoods = (
        data.loc[
            data["eligible_neighbourhood"],
            [
                "city",
                "neighbourhood",
                "neighbourhood_listing_count",
                "neighbourhood_city_share_percentage",
                "neighbourhood_median_review_activity",
                "neighbourhood_reviewed_listing_percentage",
            ],
        ]
        .drop_duplicates(["city", "neighbourhood"])
        .copy()
    )
    if neighbourhoods.empty:
        return empty_figure(
            "Presencia y actividad aproximada por barrio",
            "No hay barrios con al menos 100 anuncios en la selección.",
        )

    neighbourhoods["Ciudad"] = neighbourhoods["city"].map(CITY_LABELS)
    figure = px.scatter(
        neighbourhoods,
        x="neighbourhood_city_share_percentage",
        y="neighbourhood_median_review_activity",
        size="neighbourhood_listing_count",
        color="Ciudad",
        hover_name="neighbourhood",
        custom_data=[
            "neighbourhood_listing_count",
            "neighbourhood_reviewed_listing_percentage",
        ],
        category_orders={"Ciudad": [CITY_LABELS[city] for city in CITY_ORDER]},
        color_discrete_map=CITY_COLORS,
        size_max=34,
        labels={
            "neighbourhood_city_share_percentage": "Oferta local del barrio",
            "neighbourhood_median_review_activity": "Actividad mediana aproximada",
        },
        title=(
            "Presencia y actividad aproximada por barrio"
            "<br><sup>Cada punto es un barrio con ≥100 anuncios; el tamaño representa su volumen</sup>"
        ),
    )
    figure.update_traces(
        marker={"line": {"width": 1, "color": "white"}, "opacity": 0.82},
        hovertemplate=(
            "<b>%{hovertext}</b><br>%{fullData.name}<br>"
            "Oferta local: %{x:.2f}%<br>Actividad mediana: %{y:.2f}<br>"
            "Anuncios: %{customdata[0]:,.0f}<br>"
            "Anuncios con reseñas: %{customdata[1]:.2f}%<extra></extra>"
        ),
    )
    return finish_figure(figure)


def candidate_records(data: pd.DataFrame) -> list[dict[str, object]]:
    """Prepara una fila por segmento priorizado para la tabla de negocio."""
    candidates = (
        data.loc[
            data["selected_candidate"],
            [
                "city",
                "neighbourhood",
                "room_type",
                "segment_listing_count",
                "segment_price_index",
                "segment_activity_difference",
                "segment_reviewed_listing_percentage",
                "candidate_evidence",
            ],
        ]
        .drop_duplicates(["city", "neighbourhood", "room_type"])
        .copy()
    )
    if candidates.empty:
        return []

    candidates["city_order"] = pd.Categorical(
        candidates["city"], categories=CITY_ORDER, ordered=True
    )
    candidates = candidates.sort_values(
        ["city_order", "segment_activity_difference", "segment_listing_count"],
        ascending=[True, False, False],
    )
    candidates["city"] = candidates["city"].map(CITY_LABELS)
    candidates["room_type"] = candidates["room_type"].map(ROOM_LABELS)
    candidates = candidates.rename(
        columns={
            "city": "city_label",
            "neighbourhood": "neighbourhood_label",
            "room_type": "room_type_label",
            "segment_listing_count": "listing_count",
            "segment_price_index": "price_index",
            "segment_activity_difference": "activity_difference",
            "segment_reviewed_listing_percentage": "reviewed_percentage",
            "candidate_evidence": "evidence",
        }
    )
    output_columns = [
        "city_label",
        "neighbourhood_label",
        "room_type_label",
        "listing_count",
        "price_index",
        "activity_difference",
        "reviewed_percentage",
        "evidence",
    ]
    return candidates[output_columns].to_dict("records")


def build_long_stay_figure(data: pd.DataFrame) -> go.Figure:
    """Compara el peso de anuncios que exigen más de ocho noches."""
    if data.empty:
        return empty_figure(
            "Anuncios con mínimo superior a ocho noches",
            "No existen anuncios para esta combinación de filtros.",
        )

    long_stay = data.groupby("city", as_index=False).agg(
        listing_count=("id", "nunique"),
        long_stay_count=("minimum_nights_over_8", "sum"),
    )
    long_stay["long_stay_percentage"] = (
        long_stay["long_stay_count"] / long_stay["listing_count"] * 100
    )
    long_stay["Ciudad"] = long_stay["city"].map(CITY_LABELS)

    figure = px.bar(
        long_stay,
        x="Ciudad",
        y="long_stay_percentage",
        custom_data=["long_stay_count", "listing_count"],
        category_orders={"Ciudad": [CITY_LABELS[city] for city in CITY_ORDER]},
        labels={"long_stay_percentage": "% de anuncios"},
        title=(
            "Anuncios con mínimo superior a ocho noches"
            "<br><sup>Porcentaje sobre los anuncios visibles de cada ciudad</sup>"
        ),
    )
    figure.update_traces(
        marker_color=RAUSCH,
        marker_line_color=INK,
        marker_line_width=0.6,
        hovertemplate=(
            "<b>%{x}</b><br>Anuncios: %{customdata[0]:,.0f}<br>"
            "Total visible: %{customdata[1]:,.0f}<br>"
            "Peso: %{y:.2f}%<extra></extra>"
        ),
    )
    return finish_figure(figure, y_suffix="%")


def build_anomaly_figure(data: pd.DataFrame) -> go.Figure:
    """Cuenta por ciudad las tres señales que requieren revisión."""
    if data.empty:
        return empty_figure(
            "Observaciones que requieren revisión",
            "No existen anuncios para esta combinación de filtros.",
        )

    metrics = list(ISSUE_LABELS)
    anomalies = data.groupby("city", as_index=False)[metrics].sum()
    anomalies = anomalies.melt(
        id_vars="city",
        value_vars=metrics,
        var_name="issue",
        value_name="listing_count",
    )
    anomalies["Ciudad"] = anomalies["city"].map(CITY_LABELS)
    anomalies["Observación"] = anomalies["issue"].map(ISSUE_LABELS)

    figure = px.bar(
        anomalies,
        x="Ciudad",
        y="listing_count",
        color="Observación",
        barmode="group",
        category_orders={
            "Ciudad": [CITY_LABELS[city] for city in CITY_ORDER],
            "Observación": list(ISSUE_LABELS.values()),
        },
        color_discrete_map=ISSUE_COLORS,
        labels={"listing_count": "Número de anuncios"},
        title=(
            "Observaciones que requieren revisión"
            "<br><sup>Conteos independientes; un anuncio puede presentar más de una señal</sup>"
        ),
    )
    figure.update_traces(
        marker_line_color="white",
        marker_line_width=0.6,
        hovertemplate=(
            "<b>%{x}</b><br>%{fullData.name}<br>"
            "Anuncios: %{y:,.0f}<extra></extra>"
        ),
    )
    return finish_figure(figure)


def quality_records(data: pd.DataFrame) -> list[dict[str, object]]:
    """Prepara el detalle de anuncios con alguna señal prioritaria."""
    details = data.loc[data["has_priority_quality_issue"]].copy()
    if details.empty:
        return []

    def describe_issues(row: pd.Series) -> str:
        issues: list[str] = []
        if row["non_positive_price"]:
            issues.append("Precio no positivo")
        if row["minimum_nights_1000_plus"]:
            issues.append("Mínimo de 1.000+ noches")
        if row["reviews_without_monthly_rate"]:
            issues.append("Reseñas sin frecuencia mensual")
        return " · ".join(issues)

    details["issue"] = details.apply(describe_issues, axis=1)
    details["city_order"] = pd.Categorical(
        details["city"], categories=CITY_ORDER, ordered=True
    )
    details = details.sort_values(
        ["city_order", "issue", "minimum_nights", "id"],
        ascending=[True, True, False, True],
    )
    details["id"] = details["id"].astype(str)
    details["city"] = details["city"].map(CITY_LABELS)
    details["room_type"] = details["room_type"].map(ROOM_LABELS)
    details = details.rename(
        columns={
            "city": "city_label",
            "neighbourhood": "neighbourhood_label",
            "room_type": "room_type_label",
            "number_of_reviews": "review_count",
        }
    )
    output_columns = [
        "id",
        "city_label",
        "neighbourhood_label",
        "room_type_label",
        "price",
        "minimum_nights",
        "review_count",
        "issue",
    ]
    return details[output_columns].to_dict("records")


def metric_card(title: str, value_id: str, note: str) -> html.Article:
    """Crea una tarjeta KPI reutilizable."""
    return html.Article(
        [
            html.P(title, className="metric-label"),
            html.H3(id=value_id, className="metric-value"),
            html.P(note, className="metric-note"),
        ],
        className="metric-card",
    )


TABLE_STYLE = {
    "style_table": {"overflowX": "auto", "minWidth": "100%"},
    "style_header": {
        "backgroundColor": "#f7f7f7",
        "color": INK,
        "fontWeight": "700",
        "border": "none",
        "padding": "11px 9px",
        "textAlign": "left",
    },
    "style_cell": {
        "border": "none",
        "borderBottom": "1px solid #ebebeb",
        "fontFamily": "Avenir Next, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
        "fontSize": 13,
        "padding": "10px 9px",
        "textAlign": "left",
        "whiteSpace": "normal",
        "height": "auto",
        "minWidth": "105px",
        "maxWidth": "230px",
    },
    "style_data_conditional": [
        {"if": {"row_index": "odd"}, "backgroundColor": "#fafafa"},
    ],
}


app = Dash(
    __name__,
    title="Oferta y calidad | Análisis exploratorio",
    assets_folder=str(Path(__file__).parent / "assets"),
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)
server = app.server


app.layout = html.Div(
    [
        html.Header(
            [
                html.Div(
                    [
                        html.Div(
                            "EDA",
                            className="brand-mark",
                            **{"aria-hidden": "true"},
                        ),
                        html.P(
                            "ANÁLISIS DE ALOJAMIENTOS · SEIS CIUDADES",
                            className="eyebrow",
                        ),
                    ],
                    className="hero-top",
                ),
                html.H1("Oferta, posicionamiento y calidad"),
                html.P(
                    "Exploramos anuncios publicados en Airbnb para priorizar "
                    "segmentos que merecen investigación y localizar observaciones "
                    "que requieren revisión.",
                    className="header-copy",
                ),
            ],
            className="hero",
        ),
        html.Main(
            [
                html.Section(
                    [
                        html.Div(
                            [
                                html.Label("Ciudad", htmlFor="city-filter"),
                                dcc.Dropdown(
                                    id="city-filter",
                                    options=[
                                        {"label": CITY_LABELS[city], "value": city}
                                        for city in CITY_ORDER
                                    ],
                                    value=[],
                                    multi=True,
                                    placeholder="Todas las ciudades",
                                    clearable=True,
                                ),
                            ],
                            className="filter-field",
                        ),
                        html.Div(
                            [
                                html.Label(
                                    "Tipo de alojamiento", htmlFor="room-filter"
                                ),
                                dcc.Dropdown(
                                    id="room-filter",
                                    options=[
                                        {"label": ROOM_LABELS[room], "value": room}
                                        for room in ROOM_ORDER
                                    ],
                                    value=[],
                                    multi=True,
                                    placeholder="Todos los tipos",
                                    clearable=True,
                                ),
                            ],
                            className="filter-field",
                        ),
                        html.P(id="selection-summary", className="selection-summary"),
                    ],
                    className="filter-panel",
                    **{"aria-label": "Filtros globales"},
                ),
                dcc.Tabs(
                    id="dashboard-tabs",
                    value="offer",
                    className="dashboard-tabs",
                    children=[
                        dcc.Tab(
                            label="Oferta y posicionamiento",
                            value="offer",
                            className="dashboard-tab",
                            selected_className="dashboard-tab--selected",
                            children=[
                                html.Section(
                                    [
                                        html.Div(
                                            [
                                                html.H2("¿Dónde conviene investigar la oferta?"),
                                                html.P(
                                                    "Primero dimensionamos la selección y después "
                                                    "comparamos composición, presencia local y "
                                                    "segmentos destacados."
                                                ),
                                            ],
                                            className="section-heading",
                                        ),
                                        html.Div(
                                            [
                                                metric_card(
                                                    "Anuncios",
                                                    "offer-listing-value",
                                                    "Registros únicos visibles",
                                                ),
                                                metric_card(
                                                    "Anuncios con reseñas",
                                                    "reviewed-value",
                                                    "% con al menos una reseña",
                                                ),
                                                metric_card(
                                                    "Segmentos destacados",
                                                    "candidate-value",
                                                    "Cumplen la regla exploratoria del EDA",
                                                ),
                                            ],
                                            className="metric-grid",
                                        ),
                                        html.Div(
                                            [
                                                dcc.Graph(
                                                    id="composition-chart",
                                                    config=GRAPH_CONFIG,
                                                ),
                                                dcc.Graph(
                                                    id="neighbourhood-chart",
                                                    config=GRAPH_CONFIG,
                                                ),
                                            ],
                                            className="chart-grid",
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.H3(
                                                            "Segmentos que merecen investigación"
                                                        ),
                                                        html.P(
                                                            "Hasta cinco por ciudad: ≥50 anuncios, "
                                                            "actividad superior a su referencia y "
                                                            "precio mediano no superior a la referencia "
                                                            "de su ciudad y tipo.",
                                                            className="table-description",
                                                        ),
                                                    ],
                                                    className="table-heading",
                                                ),
                                                dash_table.DataTable(
                                                    id="candidate-table",
                                                    columns=[
                                                        {"name": "Ciudad", "id": "city_label"},
                                                        {"name": "Barrio", "id": "neighbourhood_label"},
                                                        {"name": "Tipo de alojamiento", "id": "room_type_label"},
                                                        {
                                                            "name": "Anuncios",
                                                            "id": "listing_count",
                                                            "type": "numeric",
                                                            "format": Format(precision=0, scheme=Scheme.fixed),
                                                        },
                                                        {
                                                            "name": "Índice de precio",
                                                            "id": "price_index",
                                                            "type": "numeric",
                                                            "format": Format(precision=2, scheme=Scheme.fixed),
                                                        },
                                                        {
                                                            "name": "Dif. actividad",
                                                            "id": "activity_difference",
                                                            "type": "numeric",
                                                            "format": Format(precision=2, scheme=Scheme.fixed),
                                                        },
                                                        {
                                                            "name": "% con reseñas",
                                                            "id": "reviewed_percentage",
                                                            "type": "numeric",
                                                            "format": Format(precision=2, scheme=Scheme.fixed),
                                                        },
                                                        {"name": "Evidencia", "id": "evidence"},
                                                    ],
                                                    data=[],
                                                    page_size=10,
                                                    sort_action="native",
                                                    filter_action="native",
                                                    **TABLE_STYLE,
                                                ),
                                                html.P(
                                                    "El índice de precio compara cada segmento con "
                                                    "su misma ciudad y tipo de alojamiento; 100 es "
                                                    "la mediana de referencia. La actividad es una "
                                                    "aproximación basada en reseñas, no reservas ni "
                                                    "ocupación.",
                                                    className="caveat",
                                                ),
                                            ],
                                            className="table-card",
                                        ),
                                    ],
                                    className="tab-content",
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Calidad y restricciones",
                            value="quality",
                            className="dashboard-tab",
                            selected_className="dashboard-tab--selected",
                            children=[
                                html.Section(
                                    [
                                        html.Div(
                                            [
                                                html.H2("¿Qué anuncios requieren revisión prioritaria?"),
                                                html.P(
                                                    "Se conservan los datos originales y se señalan "
                                                    "casos que conviene verificar antes de decidir."
                                                ),
                                            ],
                                            className="section-heading",
                                        ),
                                        html.Div(
                                            [
                                                metric_card(
                                                    "Precios no positivos",
                                                    "non-positive-value",
                                                    "Precio igual o inferior a cero",
                                                ),
                                                metric_card(
                                                    "Mínimo de 1.000+ noches",
                                                    "extreme-stay-value",
                                                    "Restricción extrema, sin corregir",
                                                ),
                                                metric_card(
                                                    "Reseñas sin frecuencia",
                                                    "missing-rate-value",
                                                    "Tienen reseñas, pero falta el ritmo mensual",
                                                ),
                                            ],
                                            className="metric-grid",
                                        ),
                                        html.Div(
                                            [
                                                dcc.Graph(
                                                    id="long-stay-chart",
                                                    config=GRAPH_CONFIG,
                                                ),
                                                dcc.Graph(
                                                    id="anomaly-chart",
                                                    config=GRAPH_CONFIG,
                                                ),
                                            ],
                                            className="chart-grid",
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.H3("Anuncios que requieren revisión"),
                                                        html.P(
                                                            "La tabla permite localizar el ID, la "
                                                            "ciudad, el barrio y la señal detectada.",
                                                            className="table-description",
                                                        ),
                                                    ],
                                                    className="table-heading",
                                                ),
                                                dash_table.DataTable(
                                                    id="quality-table",
                                                    columns=[
                                                        {"name": "ID", "id": "id"},
                                                        {"name": "Ciudad", "id": "city_label"},
                                                        {"name": "Barrio", "id": "neighbourhood_label"},
                                                        {"name": "Tipo de alojamiento", "id": "room_type_label"},
                                                        {"name": "Precio local", "id": "price", "type": "numeric"},
                                                        {"name": "Mínimo de noches", "id": "minimum_nights", "type": "numeric"},
                                                        {"name": "Reseñas", "id": "review_count", "type": "numeric"},
                                                        {"name": "Observación", "id": "issue"},
                                                    ],
                                                    data=[],
                                                    page_size=10,
                                                    sort_action="native",
                                                    filter_action="native",
                                                    **TABLE_STYLE,
                                                ),
                                                html.P(
                                                    "Los precios conservan la moneda local de cada "
                                                    "ciudad porque la fuente no documenta un código "
                                                    "de moneda común. Tampoco se dispone de una fecha "
                                                    "de extracción verificable.",
                                                    className="caveat",
                                                ),
                                            ],
                                            className="table-card",
                                        ),
                                    ],
                                    className="tab-content",
                                )
                            ],
                        ),
                    ],
                ),
            ],
            className="content",
        ),
        html.Footer(
            [
                html.Strong("Proyecto educativo independiente."),
                " No está asociado, patrocinado ni respaldado por Airbnb, Inc.",
                html.Br(),
                "Fuente analítica: seis archivos CSV incluidos en el repositorio. "
                "El dashboard no sustituye una validación operativa.",
            ],
            className="footer",
        ),
    ],
    className="app-shell",
)


@app.callback(
    Output("selection-summary", "children"),
    Output("offer-listing-value", "children"),
    Output("reviewed-value", "children"),
    Output("candidate-value", "children"),
    Output("composition-chart", "figure"),
    Output("neighbourhood-chart", "figure"),
    Output("candidate-table", "data"),
    Output("non-positive-value", "children"),
    Output("extreme-stay-value", "children"),
    Output("missing-rate-value", "children"),
    Output("long-stay-chart", "figure"),
    Output("anomaly-chart", "figure"),
    Output("quality-table", "data"),
    Input("city-filter", "value"),
    Input("room-filter", "value"),
)
def update_dashboard(
    cities: list[str] | None,
    room_types: list[str] | None,
) -> tuple[object, ...]:
    """Recalcula todos los componentes dependientes de los filtros globales."""
    filtered = apply_filters(DASHBOARD_DATA, cities, room_types)
    neighbourhood_source = selected_cities_data(DASHBOARD_DATA, cities)

    listing_count = filtered["id"].nunique()
    reviewed_percentage = (
        filtered["number_of_reviews"].gt(0).mean() * 100
        if not filtered.empty
        else 0.0
    )
    candidates = candidate_records(filtered)
    candidate_count = len(candidates)

    selected_city_text = (
        ", ".join(CITY_LABELS[city] for city in cities)
        if cities
        else "todas las ciudades"
    )
    selected_room_text = (
        ", ".join(ROOM_LABELS[room] for room in room_types)
        if room_types
        else "todos los tipos de alojamiento"
    )
    selection_summary = (
        f"Selección activa: {selected_city_text} · {selected_room_text} · "
        f"{format_integer(listing_count)} anuncios."
    )

    return (
        selection_summary,
        format_integer(listing_count),
        format_percentage(reviewed_percentage),
        format_integer(candidate_count),
        build_composition_figure(filtered),
        build_neighbourhood_figure(neighbourhood_source),
        candidates,
        format_integer(int(filtered["non_positive_price"].sum())),
        format_integer(int(filtered["minimum_nights_1000_plus"].sum())),
        format_integer(int(filtered["reviews_without_monthly_rate"].sum())),
        build_long_stay_figure(filtered),
        build_anomaly_figure(filtered),
        quality_records(filtered),
    )


@server.get("/health")
def health() -> tuple[dict[str, object], int]:
    """Expone una comprobación pequeña para Docker y despliegues posteriores."""
    return {
        "status": "ok",
        "listings": int(DASHBOARD_DATA["id"].nunique()),
        "cities": int(DASHBOARD_DATA["city"].nunique()),
    }, 200


if __name__ == "__main__":
    app.run(debug=True)
