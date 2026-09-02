# Preguntas de negocio para el EDA

## Decisión que debe apoyar el análisis

El EDA debe ayudar a Airbnb a identificar qué segmentos de su oferta merecen una
investigación o actuación diferenciada. En esta fase, un segmento es una combinación
de ciudad, barrio y tipo de alojamiento.

La evidencia disponible permite describir el posicionamiento observado de los
segmentos. No permite recomendar inversiones ni afirmar rentabilidad o demanda real.

## Pregunta principal

> ¿Qué segmentos de oferta —ciudad, barrio y tipo de alojamiento— presentan el
> posicionamiento más interesante según el tamaño de la oferta, el precio y la
> actividad observada, y qué características los diferencian?

`Posicionamiento más interesante` no es todavía una puntuación ni una conclusión.
Es un marco para localizar segmentos que destaquen en una o varias dimensiones y
que merezcan análisis posterior. Cualquier priorización final deberá explicar qué
dimensión se valora y por qué.

## Preguntas priorizadas

| Prioridad | Pregunta | Decisión que puede informar | Métricas iniciales | Variables y dimensiones | Cautelas |
|---|---|---|---|---|---|
| P1 | ¿Qué segmentos concentran la oferta y cuáles están poco representados? | Identificar mercados dominantes, nichos y necesidades de segmentación. | Número de anuncios y porcentaje de la oferta local. | Ciudad, `neighbourhood`, `room_type`, `id`. | Poca oferta no implica automáticamente una oportunidad; puede reflejar baja demanda o restricciones externas no observadas. |
| P1 | ¿Qué características diferencian los precios dentro de cada ciudad? | Entender el posicionamiento relativo de precios y localizar segmentos premium o económicos. | Mediana, cuartiles, IQR y precio relativo a la mediana de su ciudad. | `price`, ciudad, `neighbourhood`, `room_type`, `minimum_nights` y perfil del anfitrión. | No comparar importes absolutos entre ciudades; los ceros y extremos requieren una regla previa. Las asociaciones no prueban causalidad. |
| P1 | ¿Qué segmentos muestran mayor actividad observada en reseñas? | Priorizar segmentos para investigar su posible tracción o dinamismo. | Mediana de `reviews_per_month`, porcentaje sin reseñas, distribución de `number_of_reviews` y fecha de última reseña. | Ciudad, `neighbourhood`, `room_type`, `reviews_per_month`, `number_of_reviews`, `last_review`. | Las reseñas son un proxy: no equivalen a reservas, ocupación o demanda. El acumulado depende de la antigüedad no disponible. |
| P2 | ¿Hasta qué punto la oferta está concentrada en anfitriones con varios anuncios? | Diferenciar posibles anfitriones particulares y operadores de múltiples alojamientos. | Anuncios por `host_id`, porcentaje de anuncios de anfitriones múltiples y distribución del tamaño de cartera. | `host_id`, `calculated_host_listings_count`, ciudad, `room_type`, `price`. | Una cuenta no equivale necesariamente a una persona. Tokio no incluye el conteo calculado, aunque puede agregarse `host_id` dentro de su archivo. |
| P2 | ¿Dónde predominan restricciones de estancia mínima que limitan la oferta de corta duración? | Detectar segmentos con políticas de reserva diferenciadas y anomalías relevantes. | Mediana, percentiles y porcentaje por bandas de `minimum_nights`. | `minimum_nights`, ciudad, `neighbourhood`, `room_type`. | Los umbrales deben justificarse; valores superiores a 365 pueden ser reglas reales o defectos y no se corregirán sin evidencia. |
| P3 | ¿Cómo se relaciona la disponibilidad publicada con el resto del perfil del anuncio? | Generar hipótesis sobre calendarios y estrategias operativas. | Mediana y distribución de `availability_365` por segmento. | `availability_365`, ciudad, `room_type`, precio y actividad observada. | Disponibilidad no equivale a ocupación: un día no disponible puede estar reservado o bloqueado. Tokio no contiene la variable. |

## Hipótesis iniciales para una fase posterior

Estas hipótesis no se consideran demostradas y su prueba estadística no pertenece a
la tarjeta #11:

1. La distribución de tipos de alojamiento difiere entre ciudades y barrios.
2. El precio presenta diferencias relevantes según tipo de alojamiento y barrio
   dentro de cada ciudad.
3. Los anuncios de anfitriones con varias propiedades muestran perfiles distintos de
   precio, restricción y actividad observada.
4. Las restricciones de estancia mínima se relacionan con diferencias en la actividad
   observada de los anuncios.

Antes de contrastarlas deberán definirse población, prueba, supuestos, tamaño del
efecto y tratamiento de valores extremos.

## Preguntas que estos datos no pueden responder directamente

- ¿Qué ciudad o segmento es más rentable?
- ¿Dónde existe más demanda o mayor ocupación?
- ¿Cuántas reservas o ingresos genera cada anuncio?
- ¿Qué causa las diferencias de precio?
- ¿Qué ciudad tiene precios absolutos más altos en una moneda común?
- ¿Cómo ha evolucionado el mercado a lo largo del tiempo?

Estas preguntas requerirían datos adicionales de reservas, ingresos, costes,
ocupación, moneda, fecha de extracción o series históricas.

## Protocolo de reformulación durante el EDA

Las preguntas son un marco inicial y podrán cambiar cuando la evidencia lo justifique.
Cada cambio se anotará en el registro inferior con:

1. estado: `activa`, `reformulada`, `emergente` o `descartada`;
2. evidencia que motiva el cambio;
3. nueva formulación o motivo de descarte;
4. variables y métricas afectadas;
5. impacto sobre el alcance y la especificación.

Una reformulación pequeña y reversible se documentará en este archivo. Si cambia el
objetivo, incorpora nuevos datos o amplía materialmente el alcance, la especificación
volverá a `draft` o se abrirá un incremento nuevo.

## Registro de revisiones

| Fecha | Pregunta | Estado | Evidencia y decisión | Impacto |
|---|---|---|---|---|
| 2026-08-31 | Pregunta principal | activa | Se adopta como hilo conductor inicial, con revisión permitida durante el EDA. | Ninguno; abre la fase de análisis. |
| 2026-09-02 | Pregunta principal | reformulada | El análisis relacional mostró que “posicionamiento interesante” necesita una referencia explícita. Se define un candidato exploratorio como un segmento de ciudad, barrio y tipo con al menos 50 anuncios, actividad mediana superior y precio mediano no superior a los de su mismo tipo dentro de la ciudad. | La selección de #13 es reproducible, pero no se interpreta como demanda, rentabilidad ni recomendación de inversión. |
