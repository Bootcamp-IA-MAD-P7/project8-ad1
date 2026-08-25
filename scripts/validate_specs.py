"""Valida la estructura mínima de las especificaciones SDD del repositorio."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = ("spec.md", "plan.md", "tasks.md")
REQUIRED_METADATA = ("id", "title", "status", "owner", "created", "updated")
ALLOWED_STATUSES = {"draft", "approved", "in-progress", "done", "superseded"}
REQUIRED_SPEC_SECTIONS = (
    "## Problema y contexto",
    "## Objetivos",
    "## Fuera de alcance",
    "## Requisitos",
    "## Criterios de aceptación",
    "## Datos y supuestos",
    "## Riesgos y limitaciones",
    "## Preguntas abiertas",
    "## Definition of Done",
)
SPEC_DIRECTORY_PATTERN = re.compile(r"^(?P<id>\d{3})-[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_front_matter(text: str) -> dict[str, str]:
    """Lee el encabezado clave-valor deliberadamente simple de ``spec.md``."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    metadata: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return metadata
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()
    return {}


def specification_directories(specs_root: Path) -> list[Path]:
    """Devuelve solo carpetas de incrementos, nunca la de plantillas."""
    if not specs_root.is_dir():
        return []
    return sorted(
        path
        for path in specs_root.iterdir()
        if path.is_dir() and path.name != "templates"
    )


def validate_specification(spec_directory: Path) -> list[str]:
    """Devuelve errores legibles; una lista vacía representa una spec válida."""
    errors: list[str] = []
    directory_match = SPEC_DIRECTORY_PATTERN.fullmatch(spec_directory.name)
    if directory_match is None:
        errors.append(
            f"{spec_directory}: el nombre debe seguir NNN-nombre-en-minusculas"
        )

    for filename in REQUIRED_FILES:
        if not (spec_directory / filename).is_file():
            errors.append(f"{spec_directory}: falta {filename}")

    spec_path = spec_directory / "spec.md"
    if not spec_path.is_file():
        return errors

    spec_text = spec_path.read_text(encoding="utf-8")
    metadata = parse_front_matter(spec_text)
    for field in REQUIRED_METADATA:
        if not metadata.get(field):
            errors.append(f"{spec_path}: falta metadata '{field}'")

    status = metadata.get("status")
    if status and status not in ALLOWED_STATUSES:
        errors.append(f"{spec_path}: status no permitido '{status}'")

    if directory_match and metadata.get("id") != directory_match.group("id"):
        errors.append(f"{spec_path}: el id no coincide con el nombre de la carpeta")

    for section in REQUIRED_SPEC_SECTIONS:
        if section not in spec_text:
            errors.append(f"{spec_path}: falta la sección '{section}'")

    requirements = set(re.findall(r"REQ-\d{3}", spec_text))
    acceptance_criteria = set(re.findall(r"AC-\d{3}", spec_text))
    if not requirements:
        errors.append(f"{spec_path}: no contiene requisitos REQ-NNN")
    if not acceptance_criteria:
        errors.append(f"{spec_path}: no contiene criterios AC-NNN")

    tasks_path = spec_directory / "tasks.md"
    if tasks_path.is_file():
        tasks_text = tasks_path.read_text(encoding="utf-8")
        if not re.search(r"- \[[ xX]\] \*\*TASK-\d{3}\*\*", tasks_text):
            errors.append(f"{tasks_path}: no contiene tareas TASK-NNN con checkbox")
        for requirement in requirements:
            if requirement not in tasks_text:
                errors.append(f"{tasks_path}: no referencia {requirement}")
        for criterion in acceptance_criteria:
            if criterion not in tasks_text:
                errors.append(f"{tasks_path}: no referencia {criterion}")

    return errors


def validate_repository(repository_root: Path) -> list[str]:
    """Valida la infraestructura y todas las carpetas de especificación."""
    specs_root = repository_root / "specs"
    errors: list[str] = []
    project_brief = repository_root / "docs" / "project-brief.md"
    if not project_brief.is_file():
        errors.append(f"{project_brief}: falta el documento de consignas originales")
    if not (specs_root / "README.md").is_file():
        errors.append(f"{specs_root}: falta README.md")

    directories = specification_directories(specs_root)
    if not directories:
        errors.append(f"{specs_root}: no hay ninguna especificación")
    for directory in directories:
        errors.extend(validate_specification(directory))
    return errors


def main() -> int:
    repository_root = Path(__file__).resolve().parents[1]
    errors = validate_repository(repository_root)
    if errors:
        print("Validación SDD fallida:")
        for error in errors:
            print(f"- {error}")
        return 1

    count = len(specification_directories(repository_root / "specs"))
    print(f"Validación SDD correcta: {count} especificación(es) revisada(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
