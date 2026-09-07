# Validación del dashboard de Power BI

## Resultado

El archivo `dashboard/airbnb_offer_dashboard.pbix` implementa el diseño aprobado para
las tarjetas #19 y #20. La revisión del paquete se realizó en modo lectura el 7 de
septiembre de 2026 y no modificó el dashboard.

## Fuente y alcance

- Fuente: seis CSV de `data/raw/airbnb/` declarados en `data/manifest.csv`.
- Descarga local: 27 de agosto de 2026.
- Fecha de extracción del proveedor: no disponible.
- Granularidad: una fila por anuncio y ciudad.
- Herramienta: Power BI Desktop.
- Archivo preparado: `data/processed/airbnb_dashboard.csv`, reproducible mediante
  `python scripts/prepare_dashboard_data.py` y excluido de Git.

## Inventario del archivo

- Tamaño del `.pbix`: aproximadamente 5,4 MB.
- Formato de página: 1920 × 1080.
- Páginas: 2.
- Objetos visuales: 20, incluidos navegadores, filtros, tarjetas, gráficos, tablas y
  notas de interpretación.
- Tema: `Frontier`, con fondo claro y paleta consistente.

### Oferta y posicionamiento

- Tres tarjetas: anuncios, porcentaje con reseñas y segmentos seleccionados.
- Filtros desplegables de ciudad y tipo de alojamiento.
- Composición de la oferta por ciudad y tipo mediante columnas apiladas al 100 %.
- Relación entre presencia y actividad aproximada por barrio mediante dispersión.
- Tabla de segmentos seleccionados con escala, índice base 100 y diferencia de
  actividad.
- Nota que limita la interpretación de precio y reseñas.

### Calidad y restricciones

- Tres tarjetas: precios no positivos, estancias mínimas extremas y reseñas sin
  frecuencia mensual.
- Filtros desplegables de ciudad y tipo de alojamiento.
- Porcentaje de anuncios con más de ocho noches por ciudad.
- Observaciones prioritarias por ciudad.
- Tabla a nivel de anuncio filtrada por observación prioritaria.
- Nota que evita clasificar automáticamente las señales como errores.

## Reconciliación con el EDA

La fuente preparada detiene su generación si no reproduce estos controles:

| Control | Resultado |
|---|---:|
| Anuncios | 220.031 |
| Ciudades | 6 |
| Precios no positivos | 50 |
| Estancias mínimas de al menos 1000 noches | 20 |
| Anuncios con reseñas sin frecuencia mensual | 123 |
| Tipos `Entire home/apt` y `Private room` | 97,56 % |
| Segmentos seleccionados | 30 |

La selección incluye los alojamientos completos de Tower Hamlets, Embajadores,
Centrale y Auburn destacados en el notebook. El índice de precio se conserva como
índice base 100 y no como porcentaje adicional, evitando multiplicarlo otra vez por
100 en Power BI.

## Filtros y recorridos

- Los filtros de ciudad y tipo están sincronizados entre las dos páginas.
- Ciudad filtra todos los elementos aplicables.
- La interacción de tipo de alojamiento con el gráfico general de barrios está
  desactivada, porque ese agregado describe el barrio completo.
- La navegación entre páginas se implementa mediante navegador de páginas.
- La desarrolladora confirmó en Power BI que las columnas de la tabla de detalle se
  muestran sin resumir y que las dimensiones siguen un orden coherente.

## Limitaciones comunicadas

- Los precios no se comparan de forma absoluta entre ciudades porque las monedas no
  están identificadas.
- `reviews_per_month` es un indicador aproximado de actividad y no equivale a reservas,
  demanda, ocupación o rentabilidad.
- El umbral de más de ocho noches es analítico y no convierte automáticamente un
  anuncio en erróneo.
- La fuente y su fecha se mantienen en esta documentación y en la evidencia de la
  tarjeta #20 para evitar sobrecargar el lienzo.

## Estado de entrega

La implementación es adecuada para cerrar la tarjeta #20 con las limitaciones
anteriores. La captura y el recorrido narrado del dashboard se prepararán una sola vez
en la presentación y demo final de la tarjeta #16.
