# Tareas: entrega técnica y comunicación final

- [x] **TASK-001** — Definir el alcance conjunto de #15 y #16. Cubre REQ-005 a
  REQ-007 / AC-004 a AC-006.
  - Validación: `spec.md`, `plan.md` y `tasks.md` comparten trazabilidad.
- [x] **TASK-002** — Completar y revisar el README. Cubre REQ-001, REQ-002 / AC-001.
  - Dependencias: TASK-001.
  - Validación: objetivo, estructura, instalación, ejecución y controles son claros.
- [x] **TASK-003** — Auditar Git, secretos, artefactos y enlaces. Cubre REQ-003,
  REQ-004 / AC-002, AC-003.
  - Dependencias: TASK-001.
  - Validación: controles de archivos versionados, patrones y enlaces sin fallos.
- [x] **TASK-004** — Ejecutar notebooks, SDD y tests y preparar el cierre de #15. Cubre REQ-005 /
  AC-004.
  - Dependencias: TASK-002, TASK-003.
  - Validación: ejecuciones correctas y árbol de trabajo limpio tras el commit.
- [ ] **TASK-005** — Preparar presentación, demo, checklist y ensayo de #16. Cubre
  REQ-006, REQ-007 / AC-005, AC-006.
  - Dependencias: dashboard obligatorio completado.
  - Validación: recorrido ensayado con enlaces y archivos funcionales.

## Registro de progreso

- 2026-09-03: se inicia #15 y se detecta que la ruta 004 indicada en las issues
  colisiona con la especificación existente del EDA. Se adopta el siguiente
  identificador correlativo, `006-project-delivery`, para #15 y #16.
- 2026-09-03: el README incorpora estructura, orden y comandos de ejecución. Los
  cuatro paquetes instalados coinciden con `requirements.txt`; los enlaces internos,
  patrones sensibles y artefactos locales versionados pasan la revisión. El historial
  contiene commits incrementales y descriptivos. Los notebooks 01, 02 y 03 se
  ejecutaron sin errores; se descartó únicamente el ruido de outputs regenerados en
  01 y 02 porque su código y Markdown no habían cambiado.
