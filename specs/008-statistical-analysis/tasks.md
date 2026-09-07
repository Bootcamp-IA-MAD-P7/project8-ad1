# Tareas: contraste estadístico de patrones de oferta

- [x] **TASK-001** — Definir preguntas, H0, H1, poblaciones, métodos y umbral de
  significación antes del análisis. Cubre REQ-001 / AC-001.
  - Dependencias: EDA consolidado.
  - Validación: `spec.md` contiene ambas hipótesis sin resultados anticipados.
- [x] **TASK-002** — Crear la carga reproducible y los controles de población. Cubre
  REQ-002, REQ-008 / AC-002.
  - Dependencias: TASK-001.
  - Validación: seis ciudades y 220.031 anuncios únicos.
- [x] **TASK-003** — Ejecutar chi-cuadrado y calcular V de Cramér. Cubre REQ-003,
  REQ-004, REQ-006 / AC-003, AC-004.
  - Dependencias: TASK-002.
  - Validación: observados, esperados, estadístico, p-valor y efecto visibles.
- [x] **TASK-004** — Ejecutar Mann–Whitney por ciudad con Holm y tamaño del efecto.
  Cubre REQ-005, REQ-006 / AC-005, AC-006.
  - Dependencias: TASK-002.
  - Validación: seis comparaciones completas y ajustadas.
- [x] **TASK-005** — Interpretar evidencia y límites sin causalidad. Cubre REQ-007,
  REQ-008 / AC-004, AC-006, AC-007.
  - Dependencias: TASK-003, TASK-004.
  - Validación: cada resultado diferencia significación, magnitud e implicación.
- [x] **TASK-006** — Ejecutar notebook y validaciones y documentar la entrega. Cubre
  REQ-009 / AC-008.
  - Dependencias: TASK-005.
  - Validación: notebook, SDD y tests finalizan sin errores.

## Registro de progreso

- 2026-09-07: se predefinen dos contrastes conectados con el EDA y el dashboard. Se
  descartan comparaciones monetarias entre ciudades y una batería amplia de pruebas
  para reducir problemas de interpretación y selección de resultados.
- 2026-09-07: se reserva un notebook independiente porque los métodos inferenciales
  son nuevos en el proyecto y requieren explicar supuestos, p-valores, tamaños del
  efecto y multiplicidad sin sobrecargar el EDA ya cerrado.
- 2026-09-07: el notebook reproduce 220.031 anuncios únicos y seis ciudades, sin
  valores ausentes en la ciudad, y deja lista la población para los contrastes.
- 2026-09-07: chi-cuadrado rechaza la independencia entre ciudad y tipo
  (`chi2(15) = 8767,45`, `p < 0,001`), pero V de Cramér (`0,1152`) sitúa la
  asociación en una magnitud pequeña.
- 2026-09-07: las seis comparaciones Mann–Whitney conservan significación tras Holm
  y presentan efectos negativos: pequeños en Madrid y Milán y moderados en Londres,
  Nueva York, Sídney y Tokio. El resultado indica menor actividad aproximada en el
  grupo de más de ocho noches, sin demostrar causalidad.
- 2026-09-07: `scipy==1.18.1` queda declarada; el notebook contiene 22 celdas, nueve
  celdas de cálculo ejecutadas y ningún output de error. README y SDD documentan su
  ruta, ejecución, resultados y limitaciones.
