# Datos del proyecto

## Fuente

- Proveedor: datos entregados mediante las consignas del proyecto
- URL: https://drive.google.com/drive/folders/17sYr63LjEX30-3-KjXIaPP-bRwEmMqpf
- Fecha de descarga: 2026-08-27
- Formato seleccionado: CSV
- Número de ciudades: 6

## Autorización de uso

El responsable del proyecto ha confirmado que los datasets pueden redistribuirse
en un repositorio público con fines educativos y de portfolio.

Esta autorización no se interpreta como permiso para otros usos, especialmente
usos comerciales, salvo confirmación adicional.

## Alcance

Se descargaron los archivos CSV correspondientes a todas las ciudades
proporcionadas:

- Londres
- Madrid
- Milán
- Nueva York
- Sídney
- Tokio

Los archivos de Google Sheets no se seleccionaron porque no ofrecen una cobertura
uniforme para las seis ciudades y existen nombres duplicados.

## Archivos originales

| Ciudad | Archivo | Tamaño en bytes | Columnas preliminares |
|---|---|---:|---:|
| Londres | `london_airbnb.csv` | 11578155 | 16 |
| Madrid | `madrid_airbnb.csv` | 2801783 | 16 |
| Milán | `milan_airbnb.csv` | 2393568 | 15 |
| Nueva York | `NY_airbnb.csv` | 7077973 | 16 |
| Sídney | `sydney_airbnb.csv` | 5504518 | 16 |
| Tokio | `tokyo_airbnb.csv` | 1738173 | 14 |

## Campos que requieren precaución

Los archivos contienen campos como:

- `host_id`
- `host_name`
- `name`
- `latitude`
- `longitude`

Aunque su redistribución educativa está autorizada, estos campos deben tratarse
con cuidado. No se utilizarán para identificar, contactar o perfilar personas
individuales.

Las visualizaciones y conclusiones se presentarán preferentemente de manera
agregada.

## Reglas de conservación

Los archivos de `data/raw/airbnb/` se consideran datos originales e inmutables:

- No deben editarse manualmente.
- No deben abrirse y guardarse con Excel.
- No deben limpiarse directamente.
- No deben sobrescribirse.
- Toda transformación debe generar un archivo diferente.
- Los datos transformados se guardarán fuera de `data/raw/`.

## Observaciones iniciales

Los archivos no tienen el mismo número de columnas:

- Londres, Madrid, Nueva York y Sídney: 16 columnas.
- Milán: 15 columnas.
- Tokio: 14 columnas.

También proceden de fechas diferentes. Antes de consolidarlos será necesario
comparar esquemas, períodos, tipos de datos y unidad de análisis.

## Decisión de versionado

Los seis CSV originales se incluirán en Git porque:

- Su redistribución educativa y de portfolio está autorizada.
- El volumen total es aproximadamente 31,1 MB.
- Ningún archivo requiere Git LFS.
- Su inclusión permite reproducir el análisis directamente.
- Las huellas SHA-256 permitirán verificar su integridad.

Los archivos se incorporarán una sola vez y se considerarán inmutables.