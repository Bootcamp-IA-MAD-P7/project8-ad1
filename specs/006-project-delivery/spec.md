---
id: 006
title: Entrega técnica y comunicación final
status: in-progress
owner: desarrolladora del proyecto
created: 2026-09-03
updated: 2026-09-03
---

# Especificación: entrega técnica y comunicación final

## Problema y contexto

El EDA esencial está completo, pero el proyecto todavía necesita una revisión de
documentación y reproducibilidad antes de preparar su presentación y demostración.
Las tarjetas #15 y #16 forman el cierre técnico y comunicativo del proyecto.

## Objetivos

- Dejar el repositorio comprensible, reproducible y libre de artefactos innecesarios.
- Verificar que README, dependencias, enlaces, especificaciones y resultados coinciden.
- Preparar una presentación y una demo breves respaldadas por evidencia visible.

## Fuera de alcance

- Añadir análisis, datos o conclusiones que no estén validados.
- Convertir preguntas pendientes en resultados demostrados.
- Publicar secretos, archivos locales o artefactos generados innecesarios.
- Sustituir el dashboard pendiente por capturas o resultados inventados.

## Requisitos

- **REQ-001**: el README debe explicar objetivo, estructura, instalación, ejecución y
  validación del proyecto.
- **REQ-002**: las dependencias directas deben estar fijadas y documentadas.
- **REQ-003**: Git no debe versionar secretos, entornos locales, cachés ni outputs
  ajenos a los entregables.
- **REQ-004**: los enlaces internos y las rutas de ejecución deben funcionar.
- **REQ-005**: las especificaciones, el trabajo realizado y el estado declarado deben
  ser coherentes; el validador SDD y los tests deben pasar.
- **REQ-006**: la presentación final debe explicar objetivos, datos, método, insights,
  decisiones y limitaciones mediante evidencia validada.
- **REQ-007**: la demo debe seguir un recorrido preparado, comprobar enlaces y
  archivos y registrar al menos un ensayo completo.

## Criterios de aceptación

- **AC-001** (cubre REQ-001, REQ-002): una persona puede recrear el entorno y ejecutar
  los notebooks siguiendo únicamente el README.
- **AC-002** (cubre REQ-003): la revisión de archivos versionados y patrones sensibles
  no encuentra secretos ni artefactos locales innecesarios.
- **AC-003** (cubre REQ-004): todos los enlaces internos Markdown resuelven a archivos
  o secciones existentes.
- **AC-004** (cubre REQ-005): `git status`, el historial, las specs, el validador SDD,
  los tests y la ejecución de los notebooks quedan revisados y documentados.
- **AC-005** (cubre REQ-006): la presentación utiliza los resultados definitivos y
  comunica sus límites sin causalidad ni recomendaciones no respaldadas.
- **AC-006** (cubre REQ-007): existe un guion de demo, un checklist final y evidencia
  de un ensayo completo.

## Datos y supuestos

- Los notebooks `01`, `02` y `03` y los seis CSV versionados son las fuentes locales
  reproducibles del análisis.
- El dashboard se incorporará antes de cerrar la presentación y la demo de #16.
- Los datos no incluyen moneda, fecha de extracción, reservas, ingresos ni ocupación.

## Riesgos y limitaciones

- Una instalación exacta puede depender de la disponibilidad de Python 3.14.5 y de
  los paquetes fijados en `requirements.txt`.
- Los notebooks incluyen outputs como parte de la evidencia, por lo que no todo
  archivo generado es prescindible.
- La presentación quedaría incompleta si se cerrara antes del dashboard obligatorio.

## Preguntas abiertas

No hay preguntas que bloqueen #15. El formato final de la presentación se decidirá
al iniciar #16, después de disponer del dashboard.

## Definition of Done

- [x] La revisión técnica reproducible correspondiente a la tarjeta #15 está documentada.
- [ ] La tarjeta #16 entrega presentación, guion, checklist y ensayo.
- [ ] README, specs, dependencias, enlaces y entregables finales son coherentes.
- [ ] Todas las validaciones aplicables pasan y Git queda limpio.
