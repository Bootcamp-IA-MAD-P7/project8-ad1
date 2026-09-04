# Diseño del dashboard de oferta de Airbnb

## Audiencia y decisión

La audiencia primaria es el equipo de estrategia de oferta y operaciones de mercado
de Airbnb. Como no existe un interlocutor real que haya confirmado el rol, se trata
de una audiencia inferida a partir del briefing. La segunda audiencia es el equipo de
calidad de datos.

El dashboard debe facilitar una decisión concreta:

> Priorizar qué combinaciones de ciudad, barrio y tipo de alojamiento, y qué
> observaciones sospechosas, merecen una revisión posterior.

No decidirá dónde invertir ni afirmará demanda o rentabilidad.

## Herramienta y fuente

- Herramienta oficial: Power BI Desktop.
- Fuente: una tabla generada desde los seis CSV de `data/raw/airbnb/`.
- Granularidad: una fila por anuncio y ciudad.
- Actualización: instantánea; la fecha de extracción del proveedor no está disponible.
- Dash: posible prototipo posterior, no parte de las tarjetas #19 y #20.

La tabla preparada conservará los campos de identificación y análisis necesarios e
incorporará indicadores booleanos y referencias de barrio y segmento. De este modo,
Power BI representa cálculos ya contrastados en el notebook y evita duplicar lógica
compleja en varias visualizaciones.

## Preguntas que responde

1. ¿Cómo se distribuye la oferta por ciudad y tipo de alojamiento?
2. ¿Qué barrios combinan presencia local y mayor actividad aproximada de reseñas?
3. ¿Qué segmentos reúnen escala, precio relativo no superior a su referencia y
   actividad superior a esa referencia?
4. ¿En qué ciudades y anuncios aparecen precios no positivos, estancias mínimas
   llamativas o inconsistencias en la actividad de reseñas?

## Definición de indicadores

| Indicador | Definición y población | Utilidad | Cautela |
|---|---|---|---|
| Anuncios | Recuento distinto de `id` dentro de su ciudad | Dimensiona la oferta observada | No representa cuota real de mercado |
| Anuncios con reseñas (%) | Anuncios con `number_of_reviews > 0` / anuncios filtrados | Contextualiza la cobertura de la señal de actividad | No equivale a reservas ni demanda |
| Actividad mediana | Mediana de `reviews_per_month`; cero solo cuando también hay cero reseñas | Compara actividad aproximada entre grupos | 123 casos con reseñas y frecuencia ausente siguen nulos |
| Segmentos seleccionados | Hasta cinco combinaciones por ciudad que cumplen: al menos 50 anuncios, actividad mediana superior y precio mediano positivo no superior a la referencia ciudad-tipo | Crea una cola reproducible de investigación | Es una regla descriptiva, no un ranking de rentabilidad |
| Índice de precio | Precio mediano positivo del segmento / precio mediano positivo de su ciudad-tipo × 100 | Permite posición relativa sin cruzar importes de monedas distintas | 100 es la referencia; no convierte monedas |
| Precio no positivo | Anuncios con `price <= 0` | Señala datos o configuraciones que revisar | No se corrige ni se interpreta como gratuito |
| Estancia superior a 8 noches | Anuncios con `minimum_nights > 8` / anuncios filtrados | Muestra restricciones poco compatibles con viajes cortos | El umbral es analítico, no una regla de Airbnb |
| Estancia extrema | Anuncios con `minimum_nights >= 1000` | Aísla configuraciones excepcionalmente largas | No demuestra por sí solo un error |
| Reseñas sin frecuencia | Anuncios con reseñas y `reviews_per_month` ausente | Detecta una inconsistencia útil para calidad | No debe sustituirse automáticamente por cero |

## Página 1: Oferta y posicionamiento

**Objetivo:** localizar segmentos que merecen investigación comercial u operativa.

```text
+--------------------------------------------------------------------------+
| Oferta y posicionamiento              Filtros: Ciudad | Tipo             |
+------------------+------------------+------------------+------------------+
| Anuncios         | % con reseñas    | Segmentos seleccionados            |
+------------------+------------------+-------------------------------------+
| Composición de la oferta por ciudad y tipo (barra 100 % apilada)         |
+--------------------------------------+-----------------------------------+
| Barrios: presencia local vs actividad| Segmentos candidatos              |
| (dispersión; tamaño = anuncios)       | (tabla priorizada)                |
+--------------------------------------+-----------------------------------+
| Nota: actividad = proxy; precios relativos; moneda no identificada       |
+--------------------------------------------------------------------------+
```

| Elemento | Pregunta | Campos principales |
|---|---|---|
| Tres tarjetas | ¿Qué tamaño y cobertura tiene la selección? | anuncios, porcentaje con reseñas, segmentos seleccionados |
| Barra 100 % apilada | ¿Cómo se compone la oferta local? | ciudad, tipo, porcentaje de anuncios |
| Dispersión | ¿Qué barrios combinan presencia y actividad? | porcentaje local, actividad mediana, anuncios; solo barrios con al menos 100 anuncios |
| Tabla | ¿Qué segmentos revisar primero? | ciudad, barrio, tipo, anuncios, índice de precio, diferencia de actividad y nivel de evidencia |

La tabla se ordenará primero por nivel de evidencia y después por volumen. Un segmento
con al menos 100 anuncios se etiqueta como `más estable`; entre 50 y 99, como
`exploratorio`.

## Página 2: Calidad y restricciones

**Objetivo:** localizar datos o configuraciones que deben revisarse antes de utilizarlos
en decisiones posteriores.

```text
+--------------------------------------------------------------------------+
| Calidad y restricciones               Filtros: Ciudad | Tipo             |
+----------------------+----------------------+----------------------------+
| Precio <= 0          | Mínimo >= 1000      | Reseñas sin frecuencia     |
+----------------------+----------------------+----------------------------+
| % con estancia > 8 noches por ciudad | Observaciones por ciudad          |
| (barras)                             | (barras por tipo de anomalía)     |
+--------------------------------------+-----------------------------------+
| Detalle: id | ciudad | barrio | tipo | precio | mínimo | reseñas | señal  |
+--------------------------------------------------------------------------+
```

La tabla de detalle solo mostrará anuncios con al menos una señal prioritaria. Los
valores permanecen sin corregir para que la revisión conserve trazabilidad.

## Jerarquía, filtros e interacciones

1. Título y filtros globales de ciudad y tipo.
2. Tarjetas para orientación inmediata.
3. Un gráfico comparativo que responde la pregunta principal de la página.
4. Un gráfico diagnóstico y una tabla de detalle para actuar.
5. Una nota breve con las limitaciones indispensables.

La selección de ciudad y tipo debe afectar a todos los elementos para los que esos
campos sean aplicables. El tipo no afectará al gráfico de barrios porque sus métricas
describen el barrio completo; esta interacción se desactivará explícitamente. La
navegación tendrá dos botones con los nombres de las páginas. Barrio no será un filtro
global: ya aparece como nivel de diagnóstico y añadirlo al encabezado haría más lenta
la exploración.

## Visualizaciones que se descartan

- Serie temporal: no existe histórico ni fecha de extracción documentada.
- Mapa: añade geocodificación y complejidad sin mejorar la priorización por barrio.
- Precio absoluto entre ciudades: mezclaría monedas diferentes.
- Gráficos separados para cada KPI: las tarjetas y dos visualizaciones diagnósticas
  comunican lo necesario sin repetir información.

## Criterios de validación

- Los controles globales muestran 220.031 anuncios, 50 precios no positivos, 20
  estancias mínimas de al menos 1000 noches y 123 reseñas sin frecuencia mensual.
- `Entire home/apt` y `Private room` suman 97,56 % de la oferta sin filtros.
- La tabla reproduce, entre otros, Tower Hamlets, Embajadores, Centrale y Auburn como
  segmentos candidatos de alojamientos completos.
- Los filtros muestran las seis ciudades y actualizan tarjetas, gráficos y tablas.
- Ningún visual compara importes absolutos entre ciudades.
- Las etiquetas distinguen claramente porcentaje, recuento, noches e índice base 100.
- Las notas visibles indican que las reseñas son un proxy y que la moneda y la fecha
  de extracción no están documentadas.
- Se prueba un recorrido global, uno filtrado por ciudad, otro por tipo y la navegación
  completa entre ambas páginas.

## Evidencia que se conservará

- `dashboard/airbnb_offer_dashboard.pbix`.
- Una captura legible de cada página en `docs/images/dashboard/`.
- Comando y resultado de generación de la fuente.
- Comparación de los controles y segmentos anteriores con el notebook.
