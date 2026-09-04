# Plan: dashboard de priorización de la oferta

## Especificación relacionada

- `specs/007-dashboard/spec.md`

## Situación actual

El notebook `03_exploratory_analysis.ipynb` contiene resultados validados sobre
220.031 anuncios y una selección reproducible de segmentos. No existe todavía una
fuente preparada para Power BI ni un archivo `.pbix`. Las tarjetas #19 y #20 señalan
una ruta de spec antigua que colisiona con otra fase; este incremento adopta el
identificador correlativo `007-dashboard`.

## Enfoque propuesto

Utilizar Power BI Desktop para cumplir literalmente el entregable obligatorio. Un
script pequeño generará una tabla enriquecida a nivel de anuncio con los indicadores
y referencias ya definidos en el EDA. El dashboard tendrá solo dos páginas: una para
priorización de oferta y otra para calidad y restricciones.

Dash queda como posible extensión posterior. Esta separación permite reutilizar la
misma fuente sin retrasar el entregable oficial.

## Cambios previstos

| Archivo o área | Responsabilidad | Requisitos |
|---|---|---|
| `docs/dashboard-design.md` | Audiencia, preguntas, KPIs, boceto y validación | REQ-001, REQ-003 a REQ-007 |
| `scripts/prepare_dashboard_data.py` | Regenerar la fuente unificada para Power BI | REQ-002, REQ-006 |
| `data/processed/airbnb_dashboard.csv` | Fuente generada a nivel de anuncio | REQ-002 |
| `dashboard/airbnb_offer_dashboard.pbix` | Implementación funcional en Power BI | REQ-003 a REQ-008 |
| `docs/images/dashboard/` | Capturas de las dos páginas | REQ-008 |
| `README.md` | Comandos, entregables y ruta de apertura | REQ-002, REQ-008 |

## Estrategia de validación

| Comprobación | Resultado esperado | Criterios |
|---|---|---|
| Regenerar la fuente | 220.031 filas y una ciudad válida por anuncio | AC-002 |
| Reconciliar controles | 50, 20 y 123 observaciones en los tres controles críticos | AC-003, AC-004 |
| Comparar segmentos | Coinciden candidatos, volúmenes e índices clave del notebook | AC-003 |
| Probar filtros | Ciudad y tipo actualizan todos los elementos aplicables | AC-005 |
| Revisar contenido | Fuentes, fecha desconocida, unidades y cautelas visibles | AC-006 |
| Abrir y recorrer el `.pbix` | Dos páginas legibles y navegación comprensible | AC-007 |
| Validar repositorio | SDD y cuatro tests pasan; Git no incluye artefactos temporales | AC-007 |

## Riesgos y alternativas

- Para reducir errores y tiempo, los cálculos complejos se prepararán en Python y
  Power BI se concentrará en medidas simples, filtros y visualización.
- No se utilizará un gráfico temporal ni un mapa: los datos no contienen una serie
  histórica y el barrio ya funciona como dimensión operativa más clara.
- Si el `.pbix` supera los límites prácticos de Git, se documentará una ubicación de
  entrega recuperable sin sacrificar el script ni las capturas versionadas.

## Secuencia

1. Aprobar y cerrar el diseño de #19.
2. Generar y validar una única fuente enriquecida.
3. Construir las dos páginas en Power BI siguiendo el boceto.
4. Reconciliar métricas, probar filtros y capturar evidencia para cerrar #20.
