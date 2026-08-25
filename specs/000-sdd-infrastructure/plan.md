# Plan: infraestructura inicial de SDD

## Especificación relacionada

- `specs/000-sdd-infrastructure/spec.md`

## Situación actual

El repositorio inicial solo contiene `README.md` y una imagen. No hay carpeta de
especificaciones, automatización, código analítico ni dataset versionado visible.

## Enfoque propuesto

Adoptar documentos Markdown legibles en revisión de código y un validador pequeño
en Python. Evitamos una plataforma o librería específica hasta que exista una
necesidad demostrada.

## Cambios previstos

| Archivo o área | Responsabilidad | Requisitos |
|---|---|---|
| `AGENTS.md` | Reglas educativas y de alcance para asistentes | REQ-005 |
| `specs/README.md` | Convención y ciclo de vida | REQ-001 |
| `specs/templates/` | Plantillas de especificación, plan, tareas y decisiones | REQ-002, REQ-003 |
| `scripts/validate_specs.py` | Validación estructural local | REQ-004 |
| `tests/test_validate_specs.py` | Comportamiento esperado del validador | REQ-004 |
| `README.md` | Punto de entrada al flujo SDD | REQ-001 |
| `.github/pull_request_template.md` | Trazabilidad al revisar cambios | REQ-001, REQ-002 |
| `.gitignore` | Evitar artefactos locales y secretos accidentales | REQ-006 |
| `docs/project-brief.md` | Conservar las consignas originales fuera de la portada | REQ-007 |
| `README.md` | Resumir y enlazar documentación sin duplicar las consignas | REQ-007 |

## Estrategia de validación

| Comprobación | Resultado esperado | Criterios |
|---|---|---|
| `python scripts/validate_specs.py` | Specs y documentos obligatorios son válidos | AC-001 a AC-009 |
| `python -m unittest discover -s tests -v` | Tests del validador correctos | AC-004, AC-009 |
| Revisión de enlaces y `git diff --check` | Sin enlaces internos rotos ni errores de espacios | AC-006, AC-008 |

## Riesgos y alternativas

- YAML completo exigiría una dependencia; se usa un encabezado deliberadamente
  simple que el validador puede leer.
- Un único documento sería más corto, pero separarlo en intención, estrategia y
  ejecución permite revisar cambios de alcance sin confundirlos con tareas.

## Secuencia

1. Documentar convención y reglas.
2. Añadir plantillas y la especificación fundacional.
3. Implementar el validador y sus tests.
4. Integrar el flujo en README y revisiones.
5. Ejecutar validaciones e interpretar el resultado.
6. Separar la portada de las consignas y validar la nueva estructura documental.
