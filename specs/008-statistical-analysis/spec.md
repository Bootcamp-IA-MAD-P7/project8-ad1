---
id: 008
title: Contraste estadístico de patrones de oferta
status: done
owner: desarrolladora del proyecto
created: 2026-09-07
updated: 2026-09-07
---

# Especificación: contraste estadístico de patrones de oferta

## Problema y contexto

El EDA describió diferencias en la composición de la oferta y señaló una posible
relación entre las restricciones de estancia y la actividad aproximada de reseñas.
Esas observaciones todavía son descriptivas: muestran patrones en los archivos, pero
no cuantifican la evidencia estadística ni su magnitud.

La tarjeta #21 debe introducir estadística inferencial de forma pedagógica y
reproducible. El análisis debe ayudar a Airbnb a distinguir una asociación detectable
de una diferencia material, sin convertir una asociación observacional en causalidad,
demanda, ocupación o rentabilidad.

## Objetivos

- Contrastar si la composición por tipo de alojamiento está asociada con la ciudad.
- Contrastar por ciudad si los anuncios con estancia mínima superior a ocho noches
  presentan una distribución diferente de actividad aproximada de reseñas.
- Informar tamaños del efecto además de significación estadística.
- Comprobar y documentar los supuestos de cada método y la multiplicidad.
- Explicar los métodos con suficiente detalle para que otra persona pueda reproducir
  e interpretar el análisis.

## Fuera de alcance

- Probar todas las relaciones encontradas en el EDA o seleccionar hipótesis después
  de mirar sus p-valores.
- Comparar precios absolutos entre ciudades o convertir monedas.
- Afirmar que la ciudad o la estancia mínima causan un tipo de oferta o una actividad.
- Presentar `reviews_per_month` como reservas, ocupación o demanda real.
- Crear un modelo predictivo, segmentación por clustering o prueba temporal.
- Eliminar valores extremos para conseguir significación estadística.

## Hipótesis predefinidas

### H1 — Ciudad y tipo de alojamiento

- **Pregunta de negocio**: ¿la composición de tipos de alojamiento cambia de manera
  relevante entre las seis ciudades?
- **Unidad de análisis**: anuncio.
- **H0**: la ciudad y el tipo de alojamiento son independientes; la distribución de
  `room_type` es la misma entre ciudades.
- **H1**: la ciudad y el tipo de alojamiento están asociados; al menos una ciudad
  presenta una distribución diferente.
- **Método**: prueba chi-cuadrado de independencia sobre la tabla de contingencia
  `city` × `room_type`.
- **Tamaño del efecto**: V de Cramér, calculado como
  `sqrt(chi2 / (n * min(filas - 1, columnas - 1)))`.

### H2 — Restricción de estancia y actividad aproximada

- **Pregunta de negocio**: ¿los anuncios con una estancia mínima superior a ocho
  noches presentan una actividad aproximada diferente dentro de cada ciudad?
- **Unidad de análisis**: anuncio dentro de su ciudad.
- **Grupo de referencia**: `minimum_nights <= 8`.
- **Grupo de interés**: `minimum_nights > 8`.
- **H0 por ciudad**: ambos grupos tienen la misma distribución de
  `review_activity_proxy`.
- **H1 por ciudad**: las distribuciones de `review_activity_proxy` son diferentes.
- **Método**: prueba bilateral U de Mann–Whitney por ciudad, con aproximación
  asintótica y corrección de empates.
- **Tamaño del efecto**: correlación biserial por rangos calculada como
  `2 * U / (n_interes * n_referencia) - 1`. Un signo positivo indica que el grupo de
  más de ocho noches tiende a valores superiores; un signo negativo indica valores
  inferiores.
- **Multiplicidad**: ajuste de Holm sobre los seis p-valores, uno por ciudad.

## Requisitos

- **REQ-001**: las preguntas, poblaciones, H0, H1, umbral `alpha = 0.05` y métodos
  deben quedar escritos antes de calcular resultados.
- **REQ-002**: el notebook debe cargar los seis CSV desde el manifiesto, conservar
  `city` y verificar el universo esperado de 220.031 anuncios.
- **REQ-003**: la prueba chi-cuadrado debe mostrar conteos observados, proporciones
  por ciudad, frecuencias esperadas, estadístico, grados de libertad y p-valor.
- **REQ-004**: la asociación ciudad-tipo debe acompañarse de V de Cramér y de una
  lectura práctica de su magnitud, no solo de su significación.
- **REQ-005**: las pruebas Mann–Whitney deben mostrar por ciudad el tamaño de ambos
  grupos, sus medianas y cuartiles, U, p-valor original, p-valor ajustado por Holm y
  correlación biserial por rangos.
- **REQ-006**: los supuestos deben comprobarse explícitamente y cualquier
  incumplimiento debe limitar la interpretación o detener la prueba afectada.
- **REQ-007**: la interpretación debe diferenciar significación estadística, tamaño
  del efecto y relevancia para negocio, sin lenguaje causal.
- **REQ-008**: los datos originales no deben modificarse y las observaciones extremas
  no deben eliminarse automáticamente.
- **REQ-009**: el notebook debe ejecutarse de principio a fin y las dependencias,
  comandos, resultados y limitaciones deben quedar documentados.

## Criterios de aceptación

- **AC-001** (cubre REQ-001): el notebook presenta ambas hipótesis y el umbral de
  decisión antes de cualquier resultado inferencial.
- **AC-002** (cubre REQ-002, REQ-008): la carga reproduce seis ciudades y 220.031
  identificadores de anuncio únicos sin modificar `data/raw/`.
- **AC-003** (cubre REQ-003, REQ-006): se verifica que las frecuencias esperadas del
  chi-cuadrado son adecuadas; si alguna es menor que 1 o más del 20 % son menores que
  5, el resultado no se interpreta sin reformular el método.
- **AC-004** (cubre REQ-004, REQ-007): el resultado ciudad-tipo informa p-valor y V de
  Cramér, y explica que una asociación detectable puede ser pequeña.
- **AC-005** (cubre REQ-005, REQ-006): cada ciudad contiene observaciones en ambos
  grupos, se reconocen asimetría y empates, y se aplica Mann–Whitney sin asumir
  normalidad.
- **AC-006** (cubre REQ-005, REQ-007): los seis resultados muestran p-valores
  ajustados por Holm y un tamaño del efecto con dirección y magnitud.
- **AC-007** (cubre REQ-007, REQ-008): las conclusiones hablan de asociación o
  diferencia observada, conservan los valores extremos y señalan posibles confusores.
- **AC-008** (cubre REQ-009): `notebooks/04_statistical_analysis.ipynb` se ejecuta sin
  errores y el validador SDD y los tests del repositorio son correctos.

## Datos y supuestos

- Las fuentes son los seis CSV declarados en `data/manifest.csv` y la unidad primaria
  es el anuncio identificado por `id` dentro de su ciudad.
- `review_activity_proxy` conserva `reviews_per_month` cuando está disponible y solo
  asigna cero cuando `number_of_reviews == 0` y la frecuencia mensual es nula.
- Los 123 anuncios con reseñas acumuladas pero sin `reviews_per_month` permanecen
  como actividad desconocida y se excluyen únicamente de H2, informando el conteo.
- `minimum_nights > 8` es un umbral exploratorio definido antes del contraste porque
  representa una restricción superior a una semana; no es un límite oficial de Airbnb.
- Se usa una significación bilateral con `alpha = 0.05`.
- Para V de Cramér se describirá la magnitud de manera contextual; como guía no rígida,
  valores próximos a 0 indican asociación débil y valores próximos a 1 asociación fuerte.
- Para la correlación biserial se usarán como guía `|r| < 0.10` despreciable,
  `0.10–0.29` pequeño, `0.30–0.49` moderado y `>= 0.50` grande.

## Comprobación de supuestos

- **Chi-cuadrado**: categorías mutuamente excluyentes, una fila por anuncio y
  frecuencias esperadas suficientes. Los ceros observados son admisibles si las
  frecuencias esperadas cumplen el criterio.
- **Mann–Whitney**: variable al menos ordinal, grupos disjuntos y observaciones
  independientes. La fuerte asimetría, los ceros y los empates justifican el método
  no paramétrico y obligan a interpretar tendencia distributiva, no diferencia causal
  ni necesariamente diferencia de medianas.
- La independencia es aproximada porque un anfitrión puede aportar varios anuncios;
  `host_id` se documentará como posible agrupación no modelada.

## Riesgos y limitaciones

- El gran tamaño muestral puede producir p-valores pequeños para efectos triviales.
- La actividad basada en reseñas no equivale a reservas, ocupación ni demanda.
- La antigüedad del anuncio, el barrio, el tipo de alojamiento, la capacidad y las
  políticas locales pueden confundir la relación de H2.
- Mann–Whitney no demuestra por sí solo una diferencia entre medianas cuando las
  formas de las distribuciones difieren.
- La elección de ocho noches es interpretable para negocio, pero sigue siendo un
  umbral analítico y deberá permanecer visible.
- Las observaciones de un mismo anfitrión pueden estar correlacionadas.

## Preguntas abiertas

No existen decisiones abiertas que impidan comenzar. Cualquier hipótesis adicional
requerirá justificar su valor para negocio y actualizar el alcance antes de probarla.

## Definition of Done

- [x] Las dos hipótesis predefinidas están ejecutadas y sus supuestos documentados.
- [x] P-valores, correcciones y tamaños del efecto están interpretados conjuntamente.
- [x] El notebook diferencia evidencia, implicación para negocio y limitaciones.
- [x] La tarjeta #21 contiene método, resultados, interpretación y evidencia.
- [x] Notebook, dependencias, README, especificación y tests son coherentes.
