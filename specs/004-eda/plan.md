# Plan: definición de preguntas de negocio para el EDA

## Especificación relacionada

- `specs/004-eda/spec.md`

## Situación actual

La fase 003 documentó las 16 variables y completó 59 controles de calidad sobre
220.031 anuncios de seis ciudades. Los datos permiten estudiar estructura de oferta,
precios, restricciones, anfitriones y señales de actividad, pero no contienen
reservas, ocupación, ingresos, costes, valoraciones ni moneda explícita.

## Enfoque propuesto

Utilizar una pregunta principal como marco revisable y descomponerla en preguntas
priorizadas. Cada pregunta tendrá una decisión asociada, unidad de análisis,
dimensiones, métricas y cautelas. Durante el EDA se analizarán primero los cortes que
puedan cambiar la interpretación y se registrarán las reformulaciones justificadas.

## Cambios previstos

| Archivo o área | Responsabilidad | Requisitos |
|---|---|---|
| `docs/eda-business-questions.md` | Preguntas, métricas, hipótesis y protocolo de revisión | REQ-001 a REQ-006 |
| `specs/004-eda/` | Alcance, estrategia y trazabilidad de la tarjeta #11 | REQ-001 a REQ-007 |
| `README.md` | Estado actual y siguiente incremento | REQ-007 |

## Estrategia de validación

| Comprobación | Resultado esperado | Criterios |
|---|---|---|
| Contraste con `docs/data-dictionary.md` | Todas las variables citadas existen y sus límites se respetan | AC-002, AC-005 |
| Revisión de trazabilidad | Cada pregunta enlaza decisión, métricas, variables y cautelas | AC-001 a AC-004 |
| `python scripts/validate_specs.py` | Estructura y referencias SDD válidas | AC-006 |
| `python -m unittest discover -s tests -v` | Tests del repositorio correctos | AC-006 |

## Riesgos y alternativas

- No se construirá un índice único de oportunidad en esta fase porque exigiría
  ponderaciones de negocio todavía no justificadas.
- Si una señal de actividad resulta insuficiente, la pregunta se reformulará en vez
  de presentar el proxy como demanda real.
- Si la comparación conjunta oculta diferencias de cobertura o moneda, el análisis
  se realizará dentro de cada ciudad y se compararán patrones relativos.

## Secuencia

1. Definir y revisar la pregunta principal y las preguntas priorizadas.
2. Confirmar métricas, variables, proxies y preguntas fuera de alcance.
3. Validar y publicar el checkpoint de la tarjeta #11.
4. Especificar el siguiente incremento de preparación y EDA sin anticipar sus
   transformaciones.
