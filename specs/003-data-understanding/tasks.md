# Tareas: diccionario de variables y evaluación inicial de calidad

- [x] **TASK-001** — Confirmar las 16 columnas y localizar fuentes de definición.
  Cubre REQ-001, REQ-002 / AC-001, AC-002.
  - Evidencia: 16 columnas confirmadas en el inventario; diccionario técnico y
    supuestos de Inside Airbnb localizados como fuente secundaria contrastable.
- [x] **TASK-002** — Documentar significado, tipo lógico, función, unidad, formato,
  disponibilidad y ambigüedades. Cubre REQ-001 a REQ-003 / AC-001, AC-002.
  - Evidencia: `docs/data-dictionary.md` cubre las 16 variables y separa tipos
    físicos, tipos lógicos, cobertura, fuentes y ambigüedades.
- [ ] **TASK-003** — Validar y publicar el diccionario inicial. Cubre REQ-001 a
  REQ-003, REQ-006 / AC-001, AC-002, AC-005, AC-006.
- [ ] **TASK-004** — Completar los controles de calidad todavía no cubiertos por el
  inventario. Cubre REQ-004, REQ-006 / AC-003, AC-005.
- [ ] **TASK-005** — Interpretar y priorizar problemas con evidencia, impacto y
  recomendación. Cubre REQ-005 / AC-004.
- [ ] **TASK-006** — Validar y publicar la evaluación inicial de calidad. Cubre
  REQ-001 a REQ-006 / AC-001 a AC-006.

## Registro de progreso

- 2026-08-28: se abrió la fase 003 a partir del inventario técnico validado.
- 2026-08-28: se decidió ejecutar primero la tarjeta #9 y mantener la #28 en espera;
  la issue #10 fue cerrada y reemplazada para corregir su incorporación al Project.
- 2026-08-28: se perfilaron `id`, `host_id`, `name` y `host_name` en las seis
  ciudades y se confirmó la diferencia entre identificadores y etiquetas textuales.
- 2026-08-28: se documentaron las variables geográficas y de oferta; se registraron
  diferencias de cobertura, precisión, moneda y fecha de referencia.
- 2026-08-28: para reducir trabajo documental repetitivo, las cuatro variables de
  actividad restantes se completaron reutilizando el inventario y las fuentes ya
  validadas; el diccionario alcanzó 16 de 16 variables.
