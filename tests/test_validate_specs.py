import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_specs.py"
MODULE_SPEC = importlib.util.spec_from_file_location("validate_specs", MODULE_PATH)
assert MODULE_SPEC is not None and MODULE_SPEC.loader is not None
validate_specs = importlib.util.module_from_spec(MODULE_SPEC)
MODULE_SPEC.loader.exec_module(validate_specs)


VALID_SPEC = """---
id: 001
title: Ejemplo
status: approved
owner: equipo
created: 2026-08-25
updated: 2026-08-25
---
# Especificación
## Problema y contexto
Contexto.
## Objetivos
Objetivo.
## Fuera de alcance
Límite.
## Requisitos
- **REQ-001**: requisito.
## Criterios de aceptación
- **AC-001** (cubre REQ-001): criterio.
## Datos y supuestos
Datos.
## Riesgos y limitaciones
Riesgos.
## Preguntas abiertas
Ninguna.
## Definition of Done
- [ ] Validado.
"""


class ValidateSpecificationTests(unittest.TestCase):
    def create_specification(self, root: Path, spec_text: str = VALID_SPEC) -> Path:
        spec_directory = root / "001-ejemplo"
        spec_directory.mkdir()
        (spec_directory / "spec.md").write_text(spec_text, encoding="utf-8")
        (spec_directory / "plan.md").write_text("# Plan\n", encoding="utf-8")
        (spec_directory / "tasks.md").write_text(
            "- [ ] **TASK-001** — Cubre REQ-001 / AC-001.\n", encoding="utf-8"
        )
        return spec_directory

    def test_valid_specification_has_no_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            spec_directory = self.create_specification(Path(temporary_directory))
            self.assertEqual(validate_specs.validate_specification(spec_directory), [])

    def test_missing_required_file_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            spec_directory = self.create_specification(Path(temporary_directory))
            (spec_directory / "plan.md").unlink()
            errors = validate_specs.validate_specification(spec_directory)
            self.assertTrue(any("falta plan.md" in error for error in errors))

    def test_directory_id_must_match_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            invalid_spec = VALID_SPEC.replace("id: 001", "id: 999")
            spec_directory = self.create_specification(
                Path(temporary_directory), invalid_spec
            )
            errors = validate_specs.validate_specification(spec_directory)
            self.assertTrue(any("id no coincide" in error for error in errors))

    def test_repository_reports_missing_project_brief(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            repository_root = Path(temporary_directory)
            specs_root = repository_root / "specs"
            specs_root.mkdir()
            (specs_root / "README.md").write_text("# Specs\n", encoding="utf-8")
            self.create_specification(specs_root)

            errors = validate_specs.validate_repository(repository_root)

            self.assertTrue(
                any("falta el documento de consignas" in error for error in errors)
            )


if __name__ == "__main__":
    unittest.main()
