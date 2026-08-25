# Especificaciones del proyecto

Esta carpeta es la fuente de verdad para los requisitos y las decisiones del
proyecto. El código explica **cómo** funciona una solución; una especificación
explica **qué** problema resuelve, **por qué** y **cómo sabremos** que está resuelto.

## Estructura

Cada incremento importante vive en una carpeta con el formato `NNN-nombre-corto`:

```text
specs/
├── README.md
├── templates/
│   ├── spec-template.md
│   ├── plan-template.md
│   ├── tasks-template.md
│   └── decision-template.md
└── NNN-nombre-corto/
    ├── spec.md
    ├── plan.md
    ├── tasks.md
    └── decisions/          # Solo si hay decisiones materiales
```

Los identificadores son correlativos y no se reutilizan. Los documentos enlazan
requisitos (`REQ-*`), criterios (`AC-*`) y tareas (`TASK-*`) para conservar la
trazabilidad.

## Ciclo de vida

1. **draft**: se exploran problema, alcance y preguntas abiertas.
2. **approved**: el alcance y los criterios permiten comenzar la implementación.
3. **in-progress**: existe al menos una tarea de implementación en curso.
4. **done**: criterios y validaciones están completos y los resultados interpretados.
5. **superseded**: otra especificación enlazada la reemplaza.

Un cambio material de alcance vuelve la especificación a `draft` o genera una
nueva especificación. Una decisión técnica que no cambia el objetivo se registra
en `decisions/NNN-titulo.md`.

## Flujo mínimo

1. Copiar las tres plantillas obligatorias a una carpeta nueva.
2. Completar `spec.md` y resolver las preguntas que bloqueen el alcance.
3. Marcar la especificación como `approved`.
4. Completar `plan.md` y dividir el trabajo en `tasks.md`.
5. Implementar una tarea, validarla y actualizar su estado.
6. Ejecutar `python scripts/validate_specs.py`.
7. Cerrar como `done` únicamente cuando todos los criterios estén satisfechos.

El validador comprueba estructura y trazabilidad básica. No puede decidir si una
explicación es pedagógica ni si una conclusión analítica es correcta; esas siguen
siendo revisiones humanas.

