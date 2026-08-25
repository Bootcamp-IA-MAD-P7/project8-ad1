---
id: DEC-001
status: accepted
date: 2026-08-25
spec: 000
---

# Decisión: separar especificación, plan y tareas

## Contexto

Necesitamos distinguir el resultado deseado de la solución técnica y del progreso
diario. Mezclarlos hace difícil detectar cuándo una implementación cambia requisitos.

## Opciones consideradas

1. Un único documento por incremento: menos archivos, pero mezcla intención,
   estrategia y estado de ejecución.
2. Tres documentos: añade una estructura pequeña, pero permite revisar cada tipo de
   cambio y conservar trazabilidad.
3. Una plataforma SDD externa: aporta automatización, pero introduce dependencia y
   complejidad antes de conocer las necesidades reales.

## Decisión

Usar `spec.md`, `plan.md` y `tasks.md` como únicos documentos obligatorios. Registrar
decisiones separadas solo cuando sean materiales.

## Consecuencias

Cada incremento requiere una pequeña disciplina documental. A cambio, alcance,
implementación y progreso se pueden revisar por separado. La decisión debe revisarse
si el coste de mantener los tres documentos supera su valor educativo.

