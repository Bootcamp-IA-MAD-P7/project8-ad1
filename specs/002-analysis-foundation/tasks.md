# Tareas: entorno reproducible e inventario técnico

- [x] **TASK-001** — Detectar intérpretes disponibles. Cubre REQ-001 / AC-001.
  - Evidencia: CPython 3.14.5 estándar y variante 3.14t instalados; Conda ausente.
- [x] **TASK-002** — Crear y activar `.venv/` desde Bash. Cubre REQ-001, REQ-002,
  REQ-005 / AC-001, AC-002, AC-005.
  - Evidencia: Python 3.14.5; `which python` apunta a `.venv/Scripts/python`;
    `pip` está instalado dentro del entorno y Git ignora `.venv/`.
- [x] **TASK-003** — Instalar dependencias mínimas. Cubre REQ-003 / AC-003.
  - Evidencia: Pandas 3.0.5 y JupyterLab 4.6.3 se importan desde `.venv/`.
- [x] **TASK-004** — Documentar la recreación del entorno. Cubre REQ-004 / AC-004.
  - Evidencia: `requirements.txt` fija las dependencias directas y el README
    documenta creación, activación, instalación, comprobación y desactivación.
- [x] **TASK-005** — Crear y publicar el checkpoint del entorno. Cubre REQ-001 a
  REQ-005 / AC-001 a AC-005, AC-007.
  - Evidencia: validaciones correctas y commit `152f0de` publicado en
    `origin/feat/001-data-foundation`.
- [ ] **TASK-006** — Generar el inventario de los seis CSV. Cubre REQ-006 / AC-006.
  - Validación: resultados reproducibles e interpretados para todas las ciudades.
- [ ] **TASK-007** — Validar y publicar el inventario. Cubre REQ-001 a REQ-006 /
  AC-001 a AC-007.
  - Validación: revisión de evidencia, commit y push.

## Registro de progreso

- 2026-08-27: se confirmó Python 3.14.5 y se eligió el intérprete estándar.
- 2026-08-27: se adoptó Git Bash como terminal de trabajo.
- 2026-08-27: se creó y verificó `.venv/` sin añadirlo a Git.
- 2026-08-27: se instalaron Pandas 3.0.5 y JupyterLab 4.6.3 y se documentó la
  recreación completa del entorno.
- 2026-08-27: se publicó el checkpoint reproducible del entorno (`152f0de`).
- 2026-08-27: se eligió un notebook ejecutable como soporte del inventario técnico.
