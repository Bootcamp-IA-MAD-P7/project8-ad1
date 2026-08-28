# Plan: diccionario de variables y evaluación inicial de calidad

## Especificación relacionada

- `specs/003-data-understanding/spec.md`

## Situación actual

La especificación 002 está cerrada. El notebook de inventario registra 220.031
filas, 16 columnas distintas, 13 columnas comunes, diferencias de esquema, nulos,
consistencia de reseñas, duplicados y unicidad de `id`.

## Enfoque

Construir primero un diccionario humano y trazable en `docs/data-dictionary.md`.
Para cada variable se separará el tipo físico observado del tipo lógico esperado y
se registrarán disponibilidad, unidad o formato, función analítica, fuente y dudas.

Después se ampliará el notebook existente o se creará un notebook específico de
calidad si la separación mejora la lectura. La evaluación reutilizará los controles
válidos del inventario y añadirá únicamente comprobaciones necesarias de dominio,
rangos, consistencia y texto.

## Cambios previstos

| Archivo o área | Responsabilidad | Requisitos |
|---|---|---|
| `docs/data-dictionary.md` | Diccionario inicial de las 16 variables | REQ-001 a REQ-003 |
| `notebooks/` | Evidencia reproducible de calidad | REQ-004 a REQ-006 |
| `specs/003-data-understanding/` | Alcance, decisiones y trazabilidad | REQ-001 a REQ-006 |

## Estrategia de validación

- Comprobar que el diccionario cubre exactamente las 16 columnas observadas.
- Contrastar las definiciones con los valores reales y fuentes citadas.
- Verificar reglas de tipos, rangos, categorías, fechas y consistencia por ciudad.
- Distinguir ausencia estructural, ausencia esperada y posible defecto.
- Ejecutar los notebooks de principio a fin y confirmar que `data/raw/` no cambia.
- Ejecutar el validador SDD y los tests del repositorio.

## Secuencia

1. Confirmar en las tarjetas #9 y #28 la referencia a la especificación 003.
2. Documentar y revisar las 16 variables.
3. Validar y publicar el checkpoint de la tarjeta #9.
4. Reutilizar el inventario y completar la evaluación de calidad de la tarjeta #28.
5. Priorizar hallazgos, validar y publicar el cierre de la fase.
