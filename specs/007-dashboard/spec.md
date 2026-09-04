---
id: 007
title: Dashboard de priorización de la oferta
status: in-progress
owner: desarrolladora del proyecto
created: 2026-09-04
updated: 2026-09-04
---

# Especificación: dashboard de priorización de la oferta

## Problema y contexto

El EDA identifica segmentos de oferta y anomalías relevantes, pero sus resultados
permanecen distribuidos en un notebook técnico. Las tarjetas #19 y #20 deben convertir
esa evidencia en un dashboard comprensible para negocio sin presentar las reseñas
como demanda ni comparar precios expresados en monedas diferentes.

La audiencia primaria inferida es el equipo de estrategia de oferta y operaciones de
mercado de Airbnb. La audiencia secundaria es el equipo responsable de calidad de
datos. El dashboard debe ayudarles a decidir qué segmentos y anomalías revisar antes,
no recomendar inversiones ni estimar rentabilidad.

## Objetivos

- Diseñar e implementar en Power BI Desktop un dashboard breve y navegable.
- Priorizar segmentos por escala, precio relativo y actividad aproximada de reseñas.
- Hacer visibles restricciones y observaciones sospechosas que requieren revisión.
- Mantener trazabilidad entre cada métrica, el EDA y los seis archivos originales.

## Fuera de alcance

- Medir reservas, demanda, ocupación, ingresos, rentabilidad o causalidad.
- Comparar precios absolutos entre ciudades o convertir monedas sin una fuente fiable.
- Mostrar tendencias temporales, porque no existen una serie histórica ni una fecha de
  extracción documentada.
- Resolver las extensiones opcionales sobre concentración de anfitriones o
  disponibilidad antes de completar el dashboard obligatorio.
- Implementar Dash, publicación web, Docker o filtros avanzados en este incremento.

## Requisitos

- **REQ-001**: el dashboard debe declarar su audiencia y facilitar la priorización de
  segmentos y observaciones para una revisión posterior.
- **REQ-002**: la fuente de Power BI debe ser una tabla reproducible a nivel de anuncio,
  derivada de los seis CSV sin modificar los originales y conservando `city`.
- **REQ-003**: la primera página debe resumir oferta y posicionamiento mediante KPIs,
  composición por tipo, actividad por barrio y una tabla de segmentos candidatos.
- **REQ-004**: la segunda página debe resumir calidad y restricciones mediante los
  precios no positivos, las estancias mínimas llamativas y la inconsistencia entre
  reseñas y frecuencia mensual.
- **REQ-005**: los filtros esenciales serán ciudad y tipo de alojamiento; barrio se
  utilizará como detalle cuando aporte a la decisión.
- **REQ-006**: cada métrica debe tener definición, población, unidad y cautela; el
  precio se expresará de forma relativa cuando se comparen ciudades.
- **REQ-007**: el dashboard debe indicar las seis fuentes, que la fecha de extracción
  no está disponible y que `reviews_per_month` es solo un indicador aproximado.
- **REQ-008**: el archivo de Power BI, sus capturas y las comprobaciones contra el
  notebook deben quedar identificados como evidencia reproducible.

## Criterios de aceptación

- **AC-001** (cubre REQ-001, REQ-003, REQ-004): las dos páginas responden preguntas
  de negocio distintas y permiten localizar segmentos o anomalías que revisar.
- **AC-002** (cubre REQ-002): la tabla de entrada se regenera desde los seis archivos
  originales mediante un comando documentado y contiene una fila por anuncio.
- **AC-003** (cubre REQ-003, REQ-006): los resultados principales coinciden con el
  notebook, incluidos los segmentos candidatos y sus referencias relativas.
- **AC-004** (cubre REQ-004, REQ-006): los controles globales reproducen 50 precios no
  positivos, 20 estancias mínimas de al menos 1000 noches y 123 anuncios con reseñas
  pero sin frecuencia mensual.
- **AC-005** (cubre REQ-005): los filtros de ciudad y tipo afectan de forma coherente
  a tarjetas, gráficos y tablas, y existe navegación clara entre páginas.
- **AC-006** (cubre REQ-006, REQ-007): títulos, unidades, fuentes y limitaciones evitan
  comparaciones entre monedas y afirmaciones sobre demanda, ocupación o rentabilidad.
- **AC-007** (cubre REQ-008): el `.pbix`, las capturas y una lista breve de recorridos
  probados permiten revisar la implementación.

## Datos y supuestos

- La unidad de análisis es un anuncio identificado por `id` dentro de su ciudad.
- Las fuentes son los seis CSV de `data/raw/airbnb/`; se descargaron el 27 de agosto
  de 2026, pero la fecha de extracción del proveedor no está disponible.
- La tabla preparada conservará los campos necesarios y añadirá indicadores y
  referencias calculadas documentadas en `docs/dashboard-design.md`.
- Un segmento elegible combina ciudad, barrio y tipo, tiene al menos 50 anuncios,
  precio mediano positivo no superior a su referencia ciudad-tipo y actividad mediana
  superior a dicha referencia. El dashboard selecciona hasta cinco por ciudad con el
  mismo orden utilizado en el EDA.
- Los segmentos con al menos 100 anuncios se consideran descriptivamente más estables;
  los de 50 a 99 se muestran como exploratorios.

## Riesgos y limitaciones

- `reviews_per_month` no equivale a reservas y puede estar afectado por la antigüedad
  del anuncio, que no está disponible.
- El precio carece de código de moneda y solo permite comparaciones internas o índices
  relativos respecto del mismo tipo y ciudad.
- Las coberturas y granularidades de los barrios difieren entre ciudades.
- El archivo `.pbix` es binario; sus cálculos críticos deben poder contrastarse con la
  fuente preparada, el notebook y capturas visibles.
- Tokio no contiene `availability_365` ni `calculated_host_listings_count`.

## Preguntas abiertas

No hay decisiones abiertas que bloqueen el diseño. La publicación o una versión
adicional en Dash solo se evaluarán después de completar la entrega obligatoria.

## Definition of Done

- [ ] El diseño de #19 está documentado y aprobado por la desarrolladora.
- [ ] El dashboard de #20 implementa el diseño con las métricas reconciliadas.
- [ ] Fuentes, definiciones, limitaciones, recorridos y evidencias están documentados.
- [ ] El validador SDD, los tests y el estado de Git son correctos.
