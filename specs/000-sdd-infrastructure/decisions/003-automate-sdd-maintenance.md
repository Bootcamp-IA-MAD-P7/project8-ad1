---
id: DEC-003
status: accepted
date: 2026-08-27
spec: 000
---

# Decisión: automatizar el mantenimiento SDD

## Contexto

La creación manual y revisión individual de cada documento SDD consumió más tiempo
que el trabajo con datos. Para una única desarrolladora, repetir la misma información
en specs, tareas y Kanban reduce la fluidez y desvía energía del objetivo educativo.

El valor de SDD está en hacer visibles alcance, criterios y decisiones, no en que la
persona desarrolladora escriba manualmente cada artefacto de trazabilidad.

## Opciones consideradas

1. Mantener toda la documentación manual: maximiza la práctica documental, pero
   retrasa de forma desproporcionada el análisis.
2. Eliminar SDD: acelera el inicio, pero se pierde trazabilidad y control del alcance.
3. Automatizar el mantenimiento SDD con Codex: conserva la metodología y permite
   concentrar el aprendizaje manual en ETL, análisis e interpretación.

## Decisión

Codex creará, actualizará y validará los documentos SDD. La desarrolladora conservará
la autoridad sobre decisiones materiales y ejecutará de forma guiada los pasos con
valor educativo en ingeniería y análisis de datos.

Las specs se agruparán por fases coherentes. GitHub Project será la vista operativa
del progreso y `tasks.md` mantendrá una trazabilidad concisa, sin replicar cada detalle
del tablero.

## Consecuencias

- Se mantiene la trazabilidad sin exigir copiado manual de Markdown.
- Las revisiones documentales se agrupan en checkpoints.
- El aprendizaje detallado se concentra en entorno, ETL, calidad, EDA, estadística,
  visualización y modelado.
- Se realizarán commits pequeños y significativos, con push frecuente a la rama de
  fase después de validar cada resultado.
- Codex seguirá deteniéndose ante decisiones materiales; la automatización documental
  no autoriza cambios silenciosos de alcance.
