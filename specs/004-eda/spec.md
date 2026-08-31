---
id: 004
title: Definición de preguntas de negocio para el EDA
status: done
owner: desarrolladora del proyecto
created: 2026-08-31
updated: 2026-08-31
---

# Especificación: definición de preguntas de negocio para el EDA

## Problema y contexto

La comprensión inicial confirmó 220.031 anuncios, 16 variables distintas y varias
limitaciones de comparabilidad entre las seis ciudades. Antes de limpiar o crear
visualizaciones es necesario convertir el briefing general en preguntas que orienten
decisiones y que puedan responderse con los datos disponibles.

La formulación inicial debe guiar el análisis sin impedir que la evidencia del EDA
revele preguntas más relevantes. Las reformulaciones se permitirán cuando estén
justificadas y conserven la trazabilidad con el objetivo de negocio.

## Objetivos

- Definir una pregunta principal que proporcione un hilo conductor al EDA.
- Priorizar preguntas analíticas respondibles con las variables disponibles.
- Asociar cada pregunta con métricas, dimensiones, límites y posibles decisiones.
- Separar preguntas descriptivas de hipótesis estadísticas.
- Permitir reformulaciones justificadas a medida que avance el análisis.

## Fuera de alcance

- Limpiar, transformar, armonizar o concatenar los datos.
- Crear visualizaciones o calcular resultados del EDA.
- Elegir o ejecutar pruebas estadísticas.
- Inferir demanda, ocupación, reservas, ingresos, rentabilidad o causalidad.
- Comparar precios absolutos entre ciudades sin armonizar monedas y períodos.

## Requisitos

- **REQ-001**: debe existir una pregunta principal vinculada con una necesidad y
  una posible decisión de negocio.
- **REQ-002**: cada pregunta priorizada debe indicar variables, métricas,
  comparaciones y limitaciones necesarias para responderla.
- **REQ-003**: las preguntas descriptivas y las hipótesis estadísticas deben
  distinguirse explícitamente.
- **REQ-004**: las métricas proxy deben nombrar qué representan y qué no permiten
  concluir.
- **REQ-005**: el EDA debe poder reformular, añadir o descartar preguntas cuando
  aparezca evidencia, registrando el motivo y el impacto sobre el alcance.
- **REQ-006**: las preguntas fuera del alcance de los datos deben quedar registradas
  para evitar conclusiones no respaldadas.
- **REQ-007**: la definición debe ser coherente con el diccionario, la evaluación de
  calidad y la tarjeta #11.

## Criterios de aceptación

- **AC-001** (cubre REQ-001): existe una pregunta principal que identifica el
  segmento analítico, las señales observables y la utilidad esperada.
- **AC-002** (cubre REQ-002, REQ-004): cada pregunta priorizada tiene métricas y
  variables disponibles, y documenta las cautelas de interpretación.
- **AC-003** (cubre REQ-003): las hipótesis aparecen separadas de las preguntas
  descriptivas y no se confunden asociaciones con causalidad.
- **AC-004** (cubre REQ-005): existe un protocolo ligero para registrar preguntas
  revisadas, emergentes o descartadas durante el EDA.
- **AC-005** (cubre REQ-006): las preguntas sobre demanda, ocupación, rentabilidad y
  comparación monetaria directa quedan fuera de alcance o formuladas como proxies.
- **AC-006** (cubre REQ-007): el validador SDD y los tests pasan, y la evidencia se
  publica en la rama de fase.

## Datos y supuestos

- La unidad de análisis inicial es el anuncio identificado por `id`.
- El segmento principal combina ciudad, `neighbourhood` y `room_type`.
- `reviews_per_month`, `number_of_reviews` y `last_review` describen actividad de
  reseñas; no miden directamente demanda, reservas u ocupación.
- `price` está expresado en moneda local no identificada y solo se comparará en
  valores absolutos dentro de cada ciudad.
- La fecha de extracción no está disponible y limita la interpretación temporal.
- Tokio no contiene `availability_365` ni `calculated_host_listings_count`.

## Riesgos y limitaciones

- Una pregunta demasiado amplia puede producir gráficos desconectados en lugar de
  una conclusión accionable.
- Combinar indicadores de oferta, precio y actividad no crea por sí mismo una medida
  válida de atractivo o rentabilidad.
- Los valores extremos y ceros de `price` requieren una regla de tratamiento antes
  de calcular resúmenes definitivos.
- Las diferencias de cobertura pueden exigir análisis por ciudad en lugar de una
  tabla completamente homogénea.

## Preguntas abiertas

No existen decisiones que bloqueen esta definición inicial. Las preguntas podrán
revisarse durante el EDA mediante el protocolo descrito en
`docs/eda-business-questions.md`.

## Definition of Done

- [x] La pregunta principal y las preguntas priorizadas están documentadas.
- [x] Cada pregunta tiene métricas, variables y limitaciones identificadas.
- [x] Las hipótesis estadísticas están separadas del análisis descriptivo.
- [x] Existe un mecanismo trazable de reformulación.
- [x] La revisión humana confirma que las preguntas resultan comprensibles y útiles.
- [x] Las validaciones pasan y el checkpoint se publica en la rama de fase.
