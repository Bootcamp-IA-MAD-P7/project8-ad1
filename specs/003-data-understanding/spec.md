---
id: 003
title: Diccionario de variables y evaluación inicial de calidad
status: approved
owner: desarrolladora del proyecto
created: 2026-08-28
updated: 2026-08-28
---

# Especificación: diccionario de variables y evaluación inicial de calidad

## Problema y contexto

El inventario técnico confirmó 16 columnas distintas en seis datasets, diferencias
de esquema, patrones de nulos y una clave candidata. Antes de limpiar o integrar los
datos es necesario documentar qué representa cada variable y evaluar si sus valores
son suficientemente fiables para iniciar el EDA.

Esta especificación agrupa las tarjetas #9 y #28 como una fase coherente de
comprensión de datos. La tarjeta #9 se ejecutará primero y la #28 reutilizará tanto
el diccionario como el notebook de inventario.

## Objetivos

- Documentar las 16 variables sin inventar significados no respaldados.
- Clasificar su función analítica y tipo lógico esperado.
- Registrar unidades, formatos, disponibilidad por ciudad y ambigüedades.
- Evaluar tipos, nulos, duplicados, validez, consistencia y posibles problemas de
  codificación antes de limpiar.
- Priorizar los problemas según su impacto sobre el EDA.

## Fuera de alcance

- Modificar los seis CSV originales.
- Imputar, eliminar, recodificar o convertir valores.
- Armonizar o concatenar los datasets.
- Realizar visualizaciones o conclusiones de negocio del EDA.
- Incorporar variables derivadas o realizar feature engineering.

## Requisitos

- **REQ-001**: todas las columnas deben tener descripción inicial, tipo lógico,
  función analítica, unidad o formato y disponibilidad documentados.
- **REQ-002**: cada definición debe distinguir evidencia observada, fuente externa
  y supuestos pendientes de confirmación.
- **REQ-003**: deben identificarse variables numéricas, categóricas, temporales,
  geográficas e identificadores.
- **REQ-004**: la evaluación de calidad debe cubrir los seis archivos y reutilizar
  las evidencias válidas del inventario técnico.
- **REQ-005**: los problemas deben registrar evidencia, impacto, severidad y acción
  recomendada sin aplicar todavía la corrección.
- **REQ-006**: el trabajo debe ser reproducible y no modificar `data/raw/`.

## Criterios de aceptación

- **AC-001** (cubre REQ-001 a REQ-003): existe `docs/data-dictionary.md` con las
  16 columnas y los campos documentales exigidos.
- **AC-002** (cubre REQ-002): las definiciones ambiguas quedan señaladas como tales
  y no se presentan inferencias como hechos.
- **AC-003** (cubre REQ-004): la evaluación registra tipos observados, nulos,
  duplicados, valores imposibles o inconsistentes y posibles problemas de texto.
- **AC-004** (cubre REQ-005): cada problema material incluye evidencia, riesgo,
  severidad y recomendación para la futura limpieza o el EDA.
- **AC-005** (cubre REQ-006): los CSV originales conservan sus hashes y el análisis
  puede ejecutarse de principio a fin.
- **AC-006** (cubre REQ-001 a REQ-006): el validador SDD y los tests pasan y los
  checkpoints se publican en la rama de fase.

## Datos y supuestos

- Los encabezados, tipos inferidos, valores observados y diferencias entre ciudades
  son la evidencia primaria del repositorio.
- Las definiciones externas se citarán únicamente cuando describan de forma fiable
  estas variables de Airbnb.
- Cuando una definición no pueda verificarse, se documentará como ambigua o
  pendiente en lugar de completarla por intuición.

## Riesgos y limitaciones

- Los archivos entregados no incluyen un diccionario oficial adjunto.
- Un mismo nombre de columna puede tener disponibilidad o calidad distinta por ciudad.
- Los tipos inferidos por Pandas describen el almacenamiento observado, no siempre
  el significado lógico de la variable.
- La evaluación es válida para la extracción versionada y no garantiza futuras
  entregas con el mismo esquema o calidad.

## Preguntas abiertas

- Confirmar la fuente documental más fiable para las definiciones de las columnas.
- Determinar durante la tarjeta #28 qué reglas de validez son estables y merecen
  convertirse después en tests automatizados.

## Definition of Done

- [ ] Las 16 variables están documentadas y clasificadas con fuentes y ambigüedades.
- [ ] La calidad inicial de las seis ciudades está evaluada e interpretada.
- [ ] Los problemas están priorizados sin transformar los datos.
- [ ] Las validaciones pasan y los checkpoints están publicados.
