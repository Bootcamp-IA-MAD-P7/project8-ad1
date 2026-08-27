# Tareas: adquisición y registro de los datos originales

## Ejecución

- [x] **TASK-001** — Revisar la fuente original y seleccionar los archivos adecuados.
  Cubre REQ-001, REQ-005 / AC-001, AC-006.
  - Dependencias: ninguna.
  - Validación: la fuente contiene CSV para las seis ciudades.
  - Resultado: se seleccionaron los seis CSV y se excluyeron las copias de Google
    Sheets y `Todas_ciudades.pbix`.

- [x] **TASK-002** — Descargar y conservar los seis CSV originales.
  Cubre REQ-001, REQ-002 / AC-001, AC-002.
  - Dependencias: TASK-001.
  - Validación: existen seis archivos no vacíos en `data/raw/airbnb/`.
  - Resultado: se conservaron los nombres y contenidos originales.

- [x] **TASK-003** — Documentar procedencia, autorización y reglas de uso.
  Cubre REQ-002, REQ-003, REQ-006 / AC-002, AC-003, AC-007.
  - Dependencias: TASK-001.
  - Validación: revisión de `data/README.md`.
  - Resultado: la fuente, fecha, autorización, precauciones y decisión de
    versionado están documentadas.

- [x] **TASK-004** — Crear y verificar el manifiesto de integridad.
  Cubre REQ-004 / AC-004, AC-005.
  - Dependencias: TASK-002.
  - Validación: recalcular SHA-256 y comparar las seis huellas.
  - Resultado: tamaños y huellas coinciden en dos comprobaciones independientes.

- [x] **TASK-005** — Preparar exclusivamente los datos previstos en Git.
  Cubre REQ-005, REQ-006 / AC-006, AC-007, AC-008.
  - Dependencias: TASK-002, TASK-003, TASK-004.
  - Validación: revisar `git status --short` y `git diff --cached --stat`.
  - Resultado: el área de preparación contiene un README, un manifiesto y seis CSV.

- [x] **TASK-006** — Completar y validar la documentación SDD.
  Cubre REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006 /
  AC-001, AC-002, AC-003, AC-004, AC-005, AC-006, AC-007, AC-008.
  - Dependencias: TASK-001 a TASK-005.
  - Validación: ejecutar `python scripts/validate_specs.py`.
  - Resultado: validación SDD correcta; se revisaron 2 especificaciones.

- [ ] **TASK-007** — Revisar y crear el commit de adquisición de datos.
  Cubre REQ-001, REQ-002, REQ-003, REQ-004, REQ-005, REQ-006 /
  AC-001, AC-002, AC-003, AC-004, AC-005, AC-006, AC-007, AC-008.
  - Dependencias: TASK-006.
  - Validación: revisar archivos preparados y resultado del commit.
  - Resultado esperado: el commit contiene únicamente datos, documentación y
    trazabilidad SDD de este incremento.

## Registro de progreso

- 2026-08-27: se descargaron y verificaron los seis CSV.
- 2026-08-27: se documentaron procedencia y autorización.
- 2026-08-27: se creó y verificó `data/manifest.csv`.
- 2026-08-27: se detectó que la adquisición había comenzado sin spec previa.
- 2026-08-27: se corrigió la desviación antes de crear el commit.
