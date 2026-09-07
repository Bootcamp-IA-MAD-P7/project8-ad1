# Plan: contraste estadístico de patrones de oferta

## Especificación relacionada

- `specs/008-statistical-analysis/spec.md`

## Situación actual

El EDA y el dashboard describen la composición de 220.031 anuncios y utilizan
`reviews_per_month` como aproximación limitada de actividad. Todavía no existe un
notebook inferencial ni una dependencia estadística declarada. La tarjeta #21 apunta
a `specs/006-statistical-analysis/`, pero ese identificador ya corresponde a la
entrega final; este incremento utiliza el siguiente identificador libre, 008.

## Enfoque propuesto

Crear un notebook independiente con dos familias de análisis predefinidas. La primera
utilizará chi-cuadrado y V de Cramér para evaluar ciudad y tipo de alojamiento. La
segunda utilizará Mann–Whitney por ciudad, ajuste de Holm y correlación biserial por
rangos para comparar actividad según la restricción de estancia.

Se reutilizará la lógica de carga y de actividad aproximada ya validada, pero el
notebook explicará cada concepto antes del código y limitará la conclusión a
asociaciones observacionales.

## Cambios previstos

| Archivo o área | Responsabilidad | Requisitos |
|---|---|---|
| `notebooks/04_statistical_analysis.ipynb` | Hipótesis, métodos, resultados e interpretación | REQ-001 a REQ-009 |
| `requirements.txt` | Dependencia estadística mínima y reproducible | REQ-009 |
| `README.md` | Ruta, propósito y comando de ejecución | REQ-009 |
| `specs/008-statistical-analysis/` | Alcance, trazabilidad y decisiones metodológicas | REQ-001 a REQ-009 |

## Estrategia de validación

| Comprobación | Resultado esperado | Criterios |
|---|---|---|
| Validar carga | 220.031 anuncios únicos y seis ciudades | AC-002 |
| Revisar tabla ciudad-tipo | Totales y proporciones coherentes con el EDA | AC-003, AC-004 |
| Revisar frecuencias esperadas | Cumplen los umbrales del chi-cuadrado | AC-003 |
| Revisar grupos por ciudad | Ambos grupos tienen datos y descriptivos visibles | AC-005 |
| Revisar Holm y efectos | Seis resultados ajustados, con signo y magnitud | AC-006 |
| Ejecutar notebook completo | Finaliza sin errores ni estado oculto | AC-008 |
| Validar repositorio | SDD y tests existentes pasan | AC-008 |

## Riesgos y alternativas

- Se añadirá únicamente la librería estadística necesaria; la corrección de Holm se
  implementará de forma explícita para no introducir otra dependencia pesada.
- No se usará una prueba t porque la actividad es asimétrica, contiene numerosos
  ceros y no cumple una forma normal plausible.
- No se usarán pruebas de precios entre ciudades por la ausencia de moneda común.
- Si los supuestos del chi-cuadrado fallan, se detendrá su interpretación antes de
  reagrupar categorías o elegir un método alternativo.

## Secuencia

1. Documentar las hipótesis y el plan antes de calcular resultados.
2. Crear el notebook con carga, controles y preparación mínima.
3. Ejecutar H1 y explicar chi-cuadrado y V de Cramér.
4. Ejecutar H2 y explicar Mann–Whitney, Holm y el tamaño del efecto.
5. Interpretar resultados, implicaciones y limitaciones.
6. Ejecutar todas las validaciones y publicar evidencia en la tarjeta #21.
