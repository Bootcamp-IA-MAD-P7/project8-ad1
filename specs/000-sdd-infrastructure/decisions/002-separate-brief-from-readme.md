---
id: DEC-002
status: accepted
date: 2026-08-25
spec: 000
---

# Decisión: separar las consignas de la portada

## Contexto

El README original cumplía simultáneamente dos funciones: portada del repositorio y
contenedor de todas las consignas. Esto dificultaba distinguir una instrucción de
origen, posiblemente ambigua u opcional, de un requisito SDD aprobado.

## Opciones consideradas

1. Renombrar `README.md` como `Task_Project.md`: conserva el contenido, pero GitHub
   deja de mostrar automáticamente una portada y el nombre no expresa con precisión
   la naturaleza del documento.
2. Mantener todo en `README.md`: evita otro archivo, pero mezcla navegación, contexto
   de origen y alcance comprometido.
3. Mantener una portada breve y trasladar las consignas a `docs/project-brief.md`:
   añade un enlace, pero hace explícita la responsabilidad de cada documento.

## Decisión

Mantener `README.md` como portada y navegación; conservar las consignas en
`docs/project-brief.md`; utilizar exclusivamente `specs/` para aprobar alcance y
criterios verificables.

## Consecuencias

Las consignas permanecen accesibles y versionadas, pero ya no se confunden con una
spec. Los cambios futuros deben actualizar el documento que corresponda y mantener
los enlaces. El validador comprobará que el brief no desaparezca accidentalmente.

