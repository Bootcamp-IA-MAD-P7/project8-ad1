# Tareas: diccionario de variables y evaluación inicial de calidad

- [x] **TASK-001** — Confirmar las 16 columnas y localizar fuentes de definición.
  Cubre REQ-001, REQ-002 / AC-001, AC-002.
  - Evidencia: 16 columnas confirmadas en el inventario; diccionario técnico y
    supuestos de Inside Airbnb localizados como fuente secundaria contrastable.
- [x] **TASK-002** — Documentar significado, tipo lógico, función, unidad, formato,
  disponibilidad y ambigüedades. Cubre REQ-001 a REQ-003 / AC-001, AC-002.
  - Evidencia: `docs/data-dictionary.md` cubre las 16 variables y separa tipos
    físicos, tipos lógicos, cobertura, fuentes y ambigüedades.
- [x] **TASK-003** — Validar y publicar el diccionario inicial. Cubre REQ-001 a
  REQ-003, REQ-006 / AC-001, AC-002, AC-005, AC-006.
  - Evidencia: commit `b3b97e4` en la rama `feat/003-data-understanding`; validador
    SDD correcto, cuatro tests aprobados y árbol de trabajo limpio.
- [x] **TASK-004** — Completar los controles de calidad todavía no cubiertos por el
  inventario. Cubre REQ-004, REQ-006 / AC-003, AC-005.
  - Evidencia: `notebooks/02_data_understanding.ipynb` ejecuta 59 controles de
    dominio y consistencia; 42 pasan y 17 requieren revisión.
- [x] **TASK-005** — Interpretar y priorizar problemas con evidencia, impacto y
  recomendación. Cubre REQ-005 / AC-004.
  - Evidencia: el notebook interpreta y prioriza precios atípicos o nulos,
    estancias superiores a 365 noches, formatos de fecha por ciudad y un defecto
    puntual de codificación, sin modificar los datos originales.
- [x] **TASK-006** — Validar y publicar la evaluación inicial de calidad. Cubre
  REQ-001 a REQ-006 / AC-001 a AC-006.
  - Evidencia: notebook sin salidas de error, validador SDD y tests correctos; el
    checkpoint se publica en la rama de fase.

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
- 2026-08-28: el diccionario se validó y publicó en el commit `b3b97e4`; la tarjeta
  #9 queda terminada y comienza la evaluación compacta de calidad de la tarjeta #28.
- 2026-08-28: la evaluación compacta confirmó 42 de 59 controles sin observaciones
  y agrupó los 17 restantes en problemas accionables para el ETL. Se comprobó que
  Milán usa `DD/MM/YY` y las otras ciudades `YYYY-MM-DD` en `last_review`, y que el
  único indicio de codificación afecta a `AllÃ´ Housing` en Londres.
