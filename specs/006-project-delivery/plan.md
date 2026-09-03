# Plan: entrega técnica y comunicación final

## Especificación relacionada

- `specs/006-project-delivery/spec.md`

## Situación actual

El EDA esencial está ejecutado y documentado. El README ya explica el entorno y SDD,
pero debe completar la estructura y los comandos de ejecución. La presentación final
debe esperar al dashboard obligatorio para no preparar dos veces la misma evidencia.

## Enfoque propuesto

Cerrar primero #15 con una auditoría breve y automatizable del repositorio. Después de
construir el dashboard, reutilizar sus visuales y los resultados del notebook para
preparar #16, el guion de demo y un único ensayo final.

## Cambios previstos

| Archivo o área | Responsabilidad | Requisitos |
|---|---|---|
| `README.md` | Objetivo, estructura, instalación, ejecución y validación | REQ-001, REQ-002 |
| `.gitignore` y archivos versionados | Higiene y ausencia de artefactos locales | REQ-003 |
| `specs/006-project-delivery/` | Alcance y evidencia de #15 y #16 | REQ-005 a REQ-007 |
| Presentación y guion de demo | Comunicación y recorrido final | REQ-006, REQ-007 |

## Estrategia de validación

| Comprobación | Resultado esperado | Criterios |
|---|---|---|
| Ejecución de notebooks | Los tres notebooks terminan sin errores | AC-001, AC-004 |
| Revisión de links Markdown | Ninguna ruta interna rota | AC-003 |
| Revisión de Git y patrones sensibles | Sin secretos ni artefactos locales | AC-002, AC-004 |
| Validador SDD y tests | Todos los controles pasan | AC-004 |
| Ensayo de presentación y demo | Recorrido completo y reproducible | AC-005, AC-006 |

## Riesgos y alternativas

- La revisión se limitará a controles que protejan un criterio; no se añadirá pulido
  sin impacto en la entrega.
- La presentación se hará una vez terminado el dashboard para evitar retrabajo.

## Secuencia

1. Auditar y corregir README, dependencias, enlaces y archivos versionados.
2. Ejecutar validaciones y publicar el cierre de #15.
3. Completar el dashboard obligatorio.
4. Preparar presentación, demo y ensayo para cerrar #16.
