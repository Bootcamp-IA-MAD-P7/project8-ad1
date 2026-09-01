---
id: 005
title: Análisis exploratorio esencial
status: in-progress
owner: desarrolladora del proyecto
created: 2026-08-31
updated: 2026-09-01
---

# Especificación: análisis exploratorio esencial

## Problema y contexto

Las preguntas de negocio ya están priorizadas, pero todavía no existe un análisis
que describa las variables, estudie sus relaciones y convierta los resultados en un
notebook final. Las tarjetas #12, #13 y #14 forman una secuencia coherente: análisis
univariante, análisis de relaciones y consolidación de insights.

El EDA debe partir de los 220.031 anuncios de las seis ciudades, respetar los
problemas de calidad conocidos y evitar tanto los gráficos automáticos sin pregunta
como las correcciones de datos no justificadas.

## Objetivos

- Comprender las distribuciones de las variables relevantes para las preguntas de
  negocio.
- Analizar relaciones, segmentos y anomalías que puedan cambiar la interpretación.
- Crear un notebook reproducible, ordenado y comprensible para otra persona.
- Respaldar cada insight con evidencia, interpretación y limitaciones.
- Reformular las preguntas iniciales cuando los resultados lo justifiquen.

## Fuera de alcance

- Modificar los archivos de `data/raw/` o sobrescribir notebooks anteriores.
- Analizar todas las columnas solo por estar disponibles.
- Eliminar, imputar o winsorizar outliers automáticamente.
- Inferir causalidad, demanda, ocupación, reservas, ingresos o rentabilidad.
- Comparar precios absolutos entre ciudades sin una moneda común.
- Ejecutar pruebas de hipótesis, construir el dashboard o realizar modelado.

## Requisitos

- **REQ-001**: debe existir un notebook de EDA con una ruta de ejecución
  determinista desde la carga hasta las conclusiones.
- **REQ-002**: el análisis univariante debe cubrir las variables numéricas y
  categóricas relevantes, no todas las columnas indiscriminadamente.
- **REQ-003**: cada tabla o gráfico debe responder una pregunta explícita y terminar
  con una interpretación de distribución, frecuencia o dispersión.
- **REQ-004**: los valores atípicos y observaciones sospechosas deben identificarse,
  cuantificarse e interpretarse sin eliminarlos automáticamente.
- **REQ-005**: las relaciones y segmentos deben derivarse de preguntas de negocio,
  considerar posibles variables de confusión y no presentar correlación como
  causalidad.
- **REQ-006**: el notebook consolidado debe explicar objetivo, método, evidencia,
  insights, limitaciones y preguntas sin resolver mediante Markdown legible.
- **REQ-007**: los gráficos deben tener título descriptivo, unidades, etiquetas,
  denominador y contexto suficientes para interpretarse sin adivinar.
- **REQ-008**: cualquier preparación debe ser mínima, reproducible, separada del
  análisis y justificada por una necesidad concreta.
- **REQ-009**: las diferencias de esquema, moneda, fecha y cobertura entre ciudades,
  así como las métricas proxy, deben permanecer visibles en la interpretación.
- **REQ-010**: las reformulaciones de preguntas deben registrarse en
  `docs/eda-business-questions.md` con la evidencia que las motiva.
- **REQ-011**: cada checkpoint debe ejecutar el notebook sin errores, conservar
  `data/raw/` y superar el validador SDD y los tests.

## Criterios de aceptación

- **AC-001** (cubre REQ-001, REQ-008): existe
  `notebooks/03_exploratory_analysis.ipynb`, con parámetros, carga, preparación,
  análisis e interpretación separados y ejecutables en orden.
- **AC-002** (cubre REQ-002, REQ-003): el checkpoint #12 analiza las variables
  seleccionadas con preguntas, resúmenes y gráficos apropiados para su tipo.
- **AC-003** (cubre REQ-004): los ceros y extremos de `price`, las estancias mínimas
  atípicas y otras observaciones sospechosas permanecen identificables y se evalúa
  su influencia sin borrarlas.
- **AC-004** (cubre REQ-005): el checkpoint #13 compara relaciones y segmentos
  relevantes, investiga anomalías y documenta confusores y límites causales.
- **AC-005** (cubre REQ-006, REQ-007): el checkpoint #14 produce un notebook limpio,
  ejecutado, con gráficos legibles e insights respaldados por resultados visibles.
- **AC-006** (cubre REQ-009): los análisis monetarios absolutos se realizan dentro
  de cada ciudad y las variables ausentes no se presentan como ceros.
- **AC-007** (cubre REQ-010): cualquier pregunta emergente, revisada o descartada
  queda trazada antes de ampliar el análisis.
- **AC-008** (cubre REQ-011): los archivos originales conservan sus hashes, no hay
  outputs de error y todas las validaciones del repositorio pasan.

## Datos y supuestos

- La unidad primaria es el anuncio identificado por `id` y la ciudad se añadirá como
  metadato derivado del archivo de origen.
- La preparación inicial podrá construir una vista conjunta en memoria, conservando
  como nulas las columnas ausentes y sin generar todavía un dataset procesado.
- Las variables numéricas principales de #12 son `price` y `minimum_nights`.
  `number_of_reviews` y `reviews_per_month` se resumirán únicamente para evaluar su
  cobertura y dispersión; su utilidad para negocio se estudiará en #13 al
  relacionarlas con los segmentos de oferta.
- `availability_365` y `calculated_host_listings_count` se analizarán en #13,
  únicamente en las ciudades donde existen, porque aisladas no representan demanda,
  ocupación ni concentración efectiva.
- Las categóricas principales de #12 son ciudad y `room_type`. Debido a su alta
  cardinalidad y distinta granularidad, `neighbourhood` se analizará en #13 dentro
  de cada ciudad y con un denominador explícito.
- `last_review` podrá analizarse después de convertir sus formatos de forma explícita,
  pero no se calculará recencia contra una fecha de extracción desconocida.
- `id`, `host_id`, nombres y coordenadas se utilizarán como claves o dimensiones
  cuando aporten valor; no necesitan una distribución univariante por defecto.

## Riesgos y limitaciones

- La escala y los extremos pueden ocultar la forma central de `price` y otras
  variables; se usarán vistas complementarias o análisis de sensibilidad sin borrar
  observaciones.
- Los barrios presentan alta cardinalidad y distinta granularidad entre ciudades.
- Los conteos históricos de reseñas dependen de una antigüedad del anuncio que no
  está disponible.
- `availability_365` no distingue reservas de bloqueos y no existe para Tokio.
- Un notebook demasiado extenso puede perjudicar el aprendizaje y la comunicación;
  se priorizarán resultados que respondan las preguntas definidas.

## Preguntas abiertas

No existen decisiones que bloqueen el checkpoint #12. La selección podrá reducirse
si un resumen demuestra que una variable no aporta evidencia a las preguntas P1.

## Definition of Done

- [x] La tarjeta #12 está completada, interpretada y publicada.
- [ ] La tarjeta #13 está completada, interpretada y publicada.
- [ ] La tarjeta #14 entrega el notebook consolidado y reproducible.
- [ ] Las preguntas reformuladas y limitaciones están documentadas.
- [ ] Los datos originales conservan su integridad y todas las validaciones pasan.
