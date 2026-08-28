# Diccionario inicial de variables

## Alcance

Este documento describe las 16 variables observadas en los seis datasets de
Airbnb. Se distingue entre el tipo físico inferido por Pandas y el tipo lógico
que corresponde al significado analítico de la variable.

Las definiciones se consideran iniciales: no sustituyen la validación de los
valores ni autorizan todavía transformaciones.

## Fuentes

1. Evidencia observada en los CSV versionados del proyecto.
2. [Inside Airbnb Data Dictionary](https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit?usp=sharing).
3. [Inside Airbnb: Data Assumptions](https://insideairbnb.com/data-assumptions/).

Inside Airbnb es un proyecto independiente y no está respaldado oficialmente
por Airbnb. Cuando una definición no pueda verificarse se indicará como
ambigua, en lugar de completarla por intuición.

## Variables

| Variable | Descripción inicial | Tipo físico observado | Tipo lógico | Función analítica | Unidad o formato | Cobertura observada | Fuente y confianza | Ambigüedades |
|---|---|---|---|---|---|---|---|---|
| `id` | Identificador único del anuncio de Airbnb. | `int64` | Identificador | Clave candidata del alojamiento y enlace entre datos relacionados. | Entero sin unidad. | 100 % en las seis ciudades; 220.031 valores distintos. | Datos observados + Inside Airbnb. Confianza alta. | La unicidad está validada para esta extracción, no para cualquier entrega futura. |
| `host_id` | Identificador de la cuenta del anfitrión o usuario. | `int64` | Identificador | Agrupar anuncios administrados por una misma cuenta. | Entero sin unidad. | 100 % en las seis ciudades; puede repetirse entre anuncios. | Datos observados + Inside Airbnb. Confianza alta. | Una cuenta no debe interpretarse automáticamente como una única persona física. |
| `name` | Título o nombre público del anuncio. | `str` | Texto descriptivo | Etiquetar e identificar visualmente anuncios; posible análisis textual posterior. | Texto libre. | Entre 99,95 % y 100 % según la ciudad. | Datos observados + Inside Airbnb. Confianza alta. | Puede repetirse, cambiar o faltar; no funciona como clave. |
| `host_name` | Nombre público mostrado para el anfitrión. | `str` | Texto descriptivo | Etiqueta de presentación; no identifica de forma fiable una cuenta. | Texto libre. | Entre 97,31 % y 99,99 % según la ciudad. | Datos observados + Inside Airbnb. Confianza alta sobre el campo. | Puede ser nombre personal, conjunto de nombres o denominación comercial; no es único ni siempre está informado. |
| `neighbourhood_group` | Agrupación territorial de nivel superior al barrio cuando está disponible. | `str`, `float64` cuando está completamente vacía, o columna ausente. | Categórica nominal geográfica | Comparar grandes zonas dentro de una ciudad cuando la variable tenga contenido. | Etiqueta territorial local. | Completa en Nueva York y Madrid; vacía en Londres, Sídney y Tokio; ausente en Milán. | Datos observados + referencia de Inside Airbnb. Confianza media. | El nivel territorial y sus límites no están documentados para estos CSV y no son comparables directamente entre ciudades. |
| `neighbourhood` | Nombre del barrio o zona local asociada al alojamiento. | `str` | Categórica nominal geográfica | Segmentar alojamientos dentro de cada ciudad. | Etiqueta territorial local. | 100 % en las seis ciudades; entre 33 y 221 categorías según la ciudad. | Datos observados + referencia de Inside Airbnb. Confianza media. | La fuente y granularidad de los límites territoriales no están documentadas; una categoría de una ciudad no equivale a la de otra. |
| `latitude` | Coordenada geográfica norte-sur del alojamiento. | `float64` | Coordenada geográfica numérica | Localización cartográfica, análisis espacial y validación territorial. | Grados decimales; WGS84 como referencia pendiente de confirmación. | 100 % en las seis ciudades. | Datos observados + diccionario de Inside Airbnb. Confianza media. | No está confirmado el sistema geodésico ni el grado de anonimización de esta entrega; Sídney usa mayor precisión y Tokio presenta ubicaciones alejadas del núcleo urbano. |
| `longitude` | Coordenada geográfica este-oeste del alojamiento. | `float64` | Coordenada geográfica numérica | Localización cartográfica, análisis espacial y validación territorial. | Grados decimales; WGS84 como referencia pendiente de confirmación. | 100 % en las seis ciudades. | Datos observados + diccionario de Inside Airbnb. Confianza media. | No está confirmado el sistema geodésico ni el grado de anonimización de esta entrega; existen diferencias de precisión entre ciudades. |
| `room_type` | Modalidad de espacio ofrecido en el anuncio. | `str` | Categórica nominal | Segmentar la oferta por tipo de alojamiento. | `Entire home/apt`, `Private room`, `Shared room` y, en algunas ciudades, `Hotel room`. | 100 % en las seis ciudades; tres o cuatro categorías según la ciudad. | Datos observados + Inside Airbnb. Confianza alta. | `Hotel room` no aparece en Nueva York, Sídney ni Tokio; su ausencia puede reflejar la oferta o el criterio de extracción. |
| `price` | Precio diario publicado para el alojamiento. | `int64` | Numérica continua monetaria | Comparar niveles y distribuciones de precio dentro de una moneda comparable. | Importe por noche; Inside Airbnb lo define en moneda local. | 100 % en las seis ciudades. | Datos observados + Inside Airbnb. Confianza media. | El CSV no incluye código de moneda ni fecha de referencia; no deben compararse ciudades ni agregarse importes sin armonizar moneda. Se observan ceros y máximos extremos pendientes de validar. |
| `minimum_nights` | Estancia mínima exigida por el anuncio. | `int64` | Numérica discreta | Analizar restricciones de reserva y perfiles de corta o larga estancia. | Noches. | 100 % en las seis ciudades; medianas entre 1 y 3 noches. | Datos observados + Inside Airbnb. Confianza alta. | Inside Airbnb advierte que las reglas del calendario pueden diferir; máximos entre 180 y 1.250 noches requieren evaluación de calidad. |
| `availability_365` | Cantidad de días marcados como disponibles en los 365 días posteriores al momento de extracción. | `int64` o columna ausente. | Numérica discreta | Analizar disponibilidad futura observada del anuncio. | Días, rango esperado de 0 a 365. | 100 % y rango 0–365 en cinco ciudades; ausente en Tokio. | Datos observados + Inside Airbnb. Confianza alta sobre el significado y media sobre la fecha de referencia. | No distingue entre una noche reservada y una bloqueada por el anfitrión; el CSV no informa la fecha de extracción. |
| `number_of_reviews` | Número acumulado de reseñas registradas para el anuncio. | `int64` | Numérica discreta de conteo | Medir actividad histórica observada y segmentar anuncios según volumen de reseñas. | Reseñas. | 100 % en las seis ciudades. | Datos observados + Inside Airbnb. Confianza alta. | No equivale directamente a número de reservas y puede estar afectado por reseñas eliminadas o estancias sin reseña. |
| `last_review` | Fecha de la reseña más reciente registrada para el anuncio. | `str` con valores nulos. | Temporal | Analizar recencia de actividad y construir ventanas temporales después de convertirla de forma controlada. | Fecha textual; formato pendiente de validar. | Entre 67,44 % y 85,37 % según la ciudad. | Datos observados + Inside Airbnb. Confianza alta sobre el significado. | Los nulos son esperables cuando no hay reseñas; Sídney contiene 123 anuncios con reseñas pero sin fecha. La fecha de corte de la extracción no está incluida. |
| `reviews_per_month` | Promedio mensual calculado de reseñas durante la vida observada del anuncio. | `float64` con valores nulos. | Numérica continua derivada | Aproximar intensidad o frecuencia histórica de reseñas. | Reseñas por mes. | Entre 67,44 % y 85,37 % según la ciudad. | Datos observados + Inside Airbnb. Confianza alta sobre la definición general. | Es una métrica derivada, no una tasa de reservas; comparte nulos con `last_review` y presenta la misma anomalía de 123 filas en Sídney. |
| `calculated_host_listings_count` | Cantidad de anuncios del anfitrión observados en la extracción para la ciudad o región. | `int64` o columna ausente. | Numérica discreta derivada | Analizar concentración de anuncios por cuenta anfitriona. | Anuncios por anfitrión dentro de la geografía de extracción. | Presente en cinco ciudades y ausente en Tokio. | Datos observados + Inside Airbnb. Confianza alta sobre el significado general. | Depende del alcance geográfico y del momento de extracción; no representa necesariamente todos los anuncios globales de la cuenta. |

## Evidencia reproducible

- `notebooks/01_data_inventory.ipynb`: esquema, tipos, nulos, consistencia de
  reseñas, duplicados y unicidad de identificadores.
- `notebooks/02_data_understanding.ipynb`: perfiles comparables utilizados para
  contrastar las definiciones del diccionario.
