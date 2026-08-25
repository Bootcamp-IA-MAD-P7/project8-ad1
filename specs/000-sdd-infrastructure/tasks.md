# Tareas: infraestructura inicial de SDD

- [x] **TASK-001** — Documentar estructura, estados y flujo. Cubre REQ-001 / AC-001.
  - Dependencias: ninguna.
  - Validación: revisión de `specs/README.md`.
- [x] **TASK-002** — Crear plantillas trazables. Cubre REQ-002, REQ-003 / AC-002, AC-003.
  - Dependencias: TASK-001.
  - Validación: existen las cuatro plantillas y contienen identificadores de ejemplo.
- [x] **TASK-003** — Añadir reglas educativas raíz. Cubre REQ-005 / AC-005.
  - Dependencias: TASK-001.
  - Validación: revisión de `AGENTS.md`.
- [x] **TASK-004** — Implementar y probar el validador. Cubre REQ-004 / AC-004.
  - Dependencias: TASK-002.
  - Validación: validador y tests finalizan con código cero.
- [x] **TASK-005** — Integrar SDD en README y PR. Cubre REQ-001 / AC-006.
  - Dependencias: TASK-001.
  - Validación: los puntos de entrada enlazan la convención y la especificación.
- [x] **TASK-006** — Excluir artefactos locales. Cubre REQ-006 / AC-007.
  - Dependencias: ninguna.
  - Validación: `git status` no propone cachés, entornos virtuales ni `.env`.
- [x] **TASK-007** — Separar portada, consignas y specs. Cubre REQ-007 / AC-008, AC-009.
  - Dependencias: TASK-001, TASK-004.
  - Validación: el README enlaza el brief y las specs; el validador exige el brief.

## Registro de progreso

Infraestructura creada y validada el 2026-08-25. La portada, las consignas originales
y las especificaciones tienen responsabilidades separadas. El siguiente incremento
debe crear una especificación propia en vez de ampliar silenciosamente la `000`.
