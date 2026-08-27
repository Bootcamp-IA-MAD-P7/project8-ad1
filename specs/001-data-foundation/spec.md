---
id: 001
title: Adquisición y registro de los datos originales
status: done
owner: desarrolladora del proyecto
created: 2026-08-27
updated: 2026-08-27
---

# Especificación: adquisición y registro de los datos originales

## Problema y contexto

Las consignas proporcionan datos de Airbnb mediante una carpeta compartida de
Google Drive, pero los archivos no estaban incluidos inicialmente en el
repositorio.

El proyecto analizará todas las ciudades disponibles. Antes de comenzar el EDA
necesitamos conservar los datos originales, documentar su procedencia y comprobar
que no se modifican accidentalmente.

## Objetivos

- Obtener los CSV originales de todas las ciudades proporcionadas.
- Conservar los archivos sin modificaciones.
- Documentar fuente, autorización y reglas de utilización.
- Registrar tamaños y huellas SHA-256.
- Incluir los datos en Git de forma trazable y reproducible.

## Fuera de alcance

- Limpiar o transformar los datos.
- Concatenar los archivos de las ciudades.
- Corregir diferencias entre columnas.
- Crear un entorno virtual o instalar Pandas.
- Realizar análisis exploratorio.
- Utilizar el archivo `Todas_ciudades.pbix`.
- Analizar las versiones disponibles como Google Sheets.

## Requisitos

- **REQ-001**: deben conservarse los CSV originales de las seis ciudades
  proporcionadas.
- **REQ-002**: los archivos originales deben almacenarse en una carpeta `raw` y
  considerarse inmutables.
- **REQ-003**: la procedencia, fecha de descarga y autorización de uso deben estar
  documentadas.
- **REQ-004**: cada archivo debe disponer de tamaño y huella SHA-256 verificables.
- **REQ-005**: solo deben versionarse los archivos fuente seleccionados, excluyendo
  copias de Google Sheets y artefactos derivados de Power BI.
- **REQ-006**: la decisión de incluir los CSV en Git debe estar justificada por su
  tamaño, autorización y finalidad educativa.

## Criterios de aceptación

- **AC-001** (cubre REQ-001): existen seis CSV correspondientes a Londres, Madrid,
  Milán, Nueva York, Sídney y Tokio.
- **AC-002** (cubre REQ-002): los CSV están almacenados en
  `data/raw/airbnb/` y se documenta que no deben modificarse.
- **AC-003** (cubre REQ-003): `data/README.md` registra fuente, fecha de descarga,
  autorización y precauciones de uso.
- **AC-004** (cubre REQ-004): `data/manifest.csv` contiene una fila por archivo con
  ruta relativa, tamaño y huella SHA-256.
- **AC-005** (cubre REQ-004): una segunda comprobación de las huellas produce los
  mismos valores registrados.
- **AC-006** (cubre REQ-005): el cambio no incluye Google Sheets ni
  `Todas_ciudades.pbix`.
- **AC-007** (cubre REQ-006): ningún archivo requiere Git LFS y la decisión de
  versionado está documentada.
- **AC-008** (cubre REQ-001 a REQ-006): Git prepara únicamente el README, el
  manifiesto, los seis CSV y los documentos SDD relacionados.

## Datos y supuestos

- La redistribución pública está autorizada para fines educativos y de portfolio.
- Los nombres y contenidos descargados se consideran los originales entregados.
- Las seis ciudades forman parte del alcance de adquisición.
- Los archivos pueden proceder de períodos diferentes.
- La compatibilidad entre esquemas todavía no está demostrada.

## Riesgos y limitaciones

- Los archivos tienen entre 14 y 16 columnas y no pueden concatenarse sin una
  validación posterior.
- Las fechas de origen pueden afectar la comparabilidad entre ciudades.
- Existen campos como `host_name`, `host_id`, `name`, `latitude` y `longitude`
  que requieren un uso responsable.
- La autorización educativa no implica autorización para usos comerciales.
- Git conservará los CSV en el historial, por lo que futuras sustituciones
  aumentarían el tamaño del repositorio.

## Preguntas abiertas

No existen preguntas que bloqueen la adquisición.

La compatibilidad de esquemas, la unidad de análisis y la comparación temporal se
resolverán en una especificación posterior de inventario técnico.

## Definition of Done

- [x] Se descargaron los seis CSV.
- [x] Se documentaron procedencia y autorización.
- [x] Se creó el manifiesto de integridad.
- [x] Se comprobaron tamaños y huellas SHA-256.
- [x] Existen `plan.md` y `tasks.md`.
- [x] La especificación pasa el validador SDD.
- [x] El cambio se revisó, se registró en Git y se publicó en la rama remota.
