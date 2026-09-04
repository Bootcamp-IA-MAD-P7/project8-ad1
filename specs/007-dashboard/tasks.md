# Tareas: dashboard de priorización de la oferta

- [x] **TASK-001** — Definir audiencia, decisión, preguntas, KPIs, filtros y boceto.
  Cubre REQ-001, REQ-003, REQ-004, REQ-005, REQ-006, REQ-007 / AC-001, AC-006.
  - Dependencias: EDA consolidado.
  - Validación: `docs/dashboard-design.md` asigna un propósito a cada elemento.
- [x] **TASK-002** — Preparar la fuente reproducible a nivel de anuncio. Cubre
  REQ-002, REQ-006 / AC-002, AC-003, AC-004.
  - Dependencias: TASK-001.
  - Validación: volumen, ciudades, indicadores y referencias coinciden con el EDA.
- [ ] **TASK-003** — Implementar la página de oferta y posicionamiento. Cubre
  REQ-003, REQ-005, REQ-006 / AC-001, AC-003, AC-005, AC-006.
  - Dependencias: TASK-002.
  - Validación: KPIs, composición, barrios y tabla de candidatos responden sus preguntas.
- [ ] **TASK-004** — Implementar la página de calidad y restricciones. Cubre
  REQ-004, REQ-005, REQ-006 / AC-001, AC-004, AC-005, AC-006.
  - Dependencias: TASK-002.
  - Validación: tarjetas, gráfico por ciudad y detalle de anomalías están reconciliados.
- [ ] **TASK-005** — Probar, documentar y capturar el dashboard. Cubre REQ-007,
  REQ-008 / AC-005, AC-006, AC-007.
  - Dependencias: TASK-003, TASK-004.
  - Validación: `.pbix`, capturas, recorridos, README, SDD y tests revisados.

## Registro de progreso

- 2026-09-04: se elige Power BI Desktop para el entregable oficial. Dash se conserva
  como extensión opcional para después de la entrega obligatoria.
- 2026-09-04: se limita el diseño a dos páginas y se excluyen métricas de ingresos,
  demanda, ocupación y tendencias que las fuentes no permiten calcular.
- 2026-09-04: `prepare_dashboard_data.py` genera 220.031 filas para seis ciudades y
  reproduce los controles del EDA: 50 precios no positivos, 20 estancias mínimas de
  al menos 1000 noches y 123 anuncios con reseñas sin frecuencia mensual. La fuente
  selecciona 30 segmentos, hasta cinco por ciudad.
