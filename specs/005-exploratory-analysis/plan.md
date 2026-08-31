# Plan: análisis exploratorio esencial

## Especificación relacionada

- `specs/005-exploratory-analysis/spec.md`

## Situación actual

Los seis CSV originales, el inventario técnico, el diccionario, la evaluación de
calidad y las preguntas de negocio están validados. Existen dos notebooks de soporte,
pero ninguno realiza todavía el EDA requerido por las tarjetas #12 a #14.

## Enfoque propuesto

Crear un único `notebooks/03_exploratory_analysis.ipynb` que crezca mediante tres
checkpoints. Primero se construirá una carga reproducible y un análisis univariante
breve. Después se añadirán únicamente las relaciones y segmentos que puedan cambiar
las conclusiones. Finalmente se reorganizarán y depurarán los outputs para obtener el
notebook entregable.

Para #12, cada variable comenzará con una pregunta y un contrato visual mínimo:

| Tipo o variable | Pregunta inicial | Evidencia prevista |
|---|---|---|
| Ciudad y `room_type` | ¿Cómo se compone la oferta? | Conteos, porcentajes y barras ordenadas |
| `neighbourhood` | ¿Qué zonas concentran la oferta local? | Cardinalidad y top de barrios con denominador |
| `price` | ¿Cuál es el nivel, dispersión y asimetría del precio dentro de cada ciudad? | Mediana, cuartiles, histograma y vista de extremos |
| `minimum_nights` | ¿Qué restricciones son habituales y cuáles son excepcionales? | Mediana, percentiles, bandas e histograma |
| Variables de reseñas | ¿Cómo se distribuye la actividad observada? | Ceros, mediana, percentiles y distribución |
| `availability_365` | ¿Cómo se distribuye la disponibilidad publicada donde existe? | Resumen e histograma por ciudad |
| Conteo de anuncios del anfitrión | ¿Qué indica la distribución sobre concentración de oferta? | Mediana, percentiles y cola de la distribución |

Los histogramas mostrarán forma; los boxplots se utilizarán solo cuando aporten una
comparación de dispersión. Los gráficos categóricos usarán barras, y las tablas se
reservarán para valores exactos o controles.

## Cambios previstos

| Archivo o área | Responsabilidad | Requisitos |
|---|---|---|
| `notebooks/03_exploratory_analysis.ipynb` | EDA reproducible y notebook final | REQ-001 a REQ-011 |
| `docs/eda-business-questions.md` | Reformulaciones respaldadas por evidencia | REQ-010 |
| `specs/005-exploratory-analysis/` | Alcance y trazabilidad de #12, #13 y #14 | REQ-001 a REQ-011 |
| `README.md` | Estado de la fase y ruta del notebook | REQ-011 |

## Estrategia de validación

| Comprobación | Resultado esperado | Criterios |
|---|---|---|
| Ejecución top-to-bottom con `nbconvert` | Notebook sin errores ni estado oculto | AC-001, AC-005, AC-008 |
| Revisión pregunta-gráfico-interpretación | Cada salida analítica tiene propósito y conclusión | AC-002 a AC-005 |
| Revisión de escalas, unidades y denominadores | Visualizaciones honestas y legibles | AC-003, AC-005, AC-006 |
| Comprobación del manifiesto de datos | Los hashes de `data/raw/` no cambian | AC-008 |
| Validador SDD y tests | Estructura y comportamiento correctos | AC-008 |

## Riesgos y alternativas

- Se evitará un gráfico por columna: una tabla será preferible cuando el gráfico no
  responda una comparación o distribución útil.
- Para colas largas se conservará una vista completa y se añadirá una vista central
  o escala alternativa claramente etiquetada.
- Los análisis con cobertura desigual se facetarán por ciudad o se limitarán a las
  ciudades comparables, indicando el universo utilizado.
- Si el notebook se vuelve difícil de ejecutar, las funciones reutilizables podrán
  extraerse a un módulo pequeño sin separar las conclusiones de su evidencia.

## Secuencia

1. Actualizar las tarjetas #12 a #14 para enlazar la especificación 005.
2. Crear el esqueleto reproducible y validar la carga sin modificar datos.
3. Completar variables numéricas y categóricas de #12, una pregunta cada vez.
4. Interpretar distribuciones y outliers, ejecutar y publicar el checkpoint #12.
5. Incorporar relaciones, segmentos y anomalías de #13.
6. Consolidar narrativa, outputs e insights para cerrar #14 y la fase.
