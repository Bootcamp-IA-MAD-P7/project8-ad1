# Tareas: análisis exploratorio esencial

- [x] **TASK-001** — Enlazar las tarjetas #12, #13 y #14 con la especificación 005
  y corregir el título de #12. Cubre REQ-011 / AC-008.
  - Validación: las tres tarjetas apuntan a `specs/005-exploratory-analysis/spec.md`.
- [x] **TASK-002** — Crear el esqueleto de
  `notebooks/03_exploratory_analysis.ipynb` y validar la carga reproducible. Cubre
  REQ-001, REQ-008, REQ-009 / AC-001, AC-006, AC-008.
  - Evidencia: `notebooks/03_exploratory_analysis.ipynb` carga las seis ciudades,
    añade su procedencia y construye una vista conjunta de 220.031 filas; los
    controles de cantidad y unicidad de `id` se ejecutan sin errores.
- [ ] **TASK-003** — Analizar las variables numéricas relevantes con preguntas,
  resúmenes y gráficos adecuados. Cubre REQ-002 a REQ-004, REQ-007 / AC-002, AC-003.
  - Dependencias: TASK-002.
  - Validación: precio, estancia mínima, reseñas, disponibilidad y concentración se
    interpretan según su cobertura y unidad.
- [ ] **TASK-004** — Analizar las variables categóricas relevantes y la composición
  de la oferta. Cubre REQ-002, REQ-003, REQ-007 / AC-002.
  - Dependencias: TASK-002.
  - Validación: ciudad, tipo de alojamiento y barrios tienen denominadores y límites.
- [ ] **TASK-005** — Integrar la interpretación univariante, investigar observaciones
  sospechosas y publicar #12. Cubre REQ-003, REQ-004, REQ-009 a REQ-011 / AC-002,
  AC-003, AC-006 a AC-008.
  - Dependencias: TASK-003, TASK-004.
  - Validación: notebook ejecutado, preguntas revisadas, hashes, SDD y tests correctos.
- [ ] **TASK-006** — Analizar relaciones, segmentos, confusores y anomalías para #13.
  Cubre REQ-005, REQ-009, REQ-010 / AC-004, AC-006, AC-007.
  - Dependencias: TASK-005.
  - Validación: cada relación responde una pregunta y separa asociación de causalidad.
- [ ] **TASK-007** — Consolidar narrativa, gráficos, insights y reproducibilidad para
  #14. Cubre REQ-001, REQ-006, REQ-007, REQ-011 / AC-001, AC-005, AC-008.
  - Dependencias: TASK-006.
  - Validación: ejecución completa sin errores ni outputs innecesarios y revisión humana.

## Registro de progreso

- 2026-08-31: se agruparon #12, #13 y #14 como checkpoints de una única fase de EDA
  esencial; #17 y #18 permanecen fuera por pertenecer al nivel medio.
- 2026-08-31: se priorizó un análisis univariante dirigido por preguntas y se excluyó
  la generación automática de gráficos para identificadores, nombres y coordenadas.
- 2026-09-01: se completó la carga reproducible y comenzó #12 con la composición de
  `room_type` y el resumen robusto de `price` por ciudad. Se añadió Matplotlib como
  dependencia directa para los gráficos del EDA; el notebook no contiene errores.
