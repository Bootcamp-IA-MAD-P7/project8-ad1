# Plan: entorno reproducible e inventario técnico

## Especificación relacionada

- `specs/002-analysis-foundation/spec.md`

## Situación actual

Python 3.14.5 está instalado como CPython estándar y como variante libre de GIL. No
existe Conda ni un entorno virtual del proyecto. `.gitignore` ya excluye `.venv/`.

## Enfoque propuesto

Usar el módulo estándar `venv` y `pip` desde Git Bash. Crear `.venv/` con el comando
`python`, comprobar que la activación cambia el intérprete, actualizar las herramientas
de instalación e incorporar solo Pandas y JupyterLab. Después se documentará el proceso
y se utilizará el entorno para construir el inventario de los seis CSV.

## Cambios previstos

| Archivo o área | Responsabilidad | Requisitos |
|---|---|---|
| `.venv/` | Entorno local no versionado | REQ-001, REQ-002 |
| `requirements.txt` | Dependencias directas verificadas | REQ-003, REQ-004 |
| `README.md` | Creación y activación desde Bash | REQ-004, REQ-005 |
| `scripts/` o `notebooks/` | Inventario técnico reproducible | REQ-006 |

## Estrategia de validación

| Comprobación | Resultado esperado | Criterios |
|---|---|---|
| `python --version` con el entorno activo | Python 3.14.5 | AC-001 |
| `which python` | Ruta dentro de `.venv/Scripts/` | AC-005 |
| Importar dependencias | Pandas y JupyterLab disponibles | AC-003 |
| `git status --short` | Ningún archivo interno de `.venv/` | AC-002 |
| Recrear desde documentación | Proceso completo y comprensible | AC-004 |
| Ejecutar inventario | Seis archivos descritos sin modificación | AC-006 |
| Validador y tests | Ejecución correcta | AC-007 |

## Riesgos y alternativas

- Conda ofrece gestión completa de entornos, pero añadirlo no aporta valor inmediato.
- La variante libre de GIL es interesante, pero no resuelve una necesidad del proyecto.
- Se instalarán más librerías únicamente cuando una pregunta analítica las requiera.

## Secuencia

1. Verificar Bash, rama e intérprete.
2. Crear y activar `.venv/`.
3. Verificar aislamiento y exclusión de Git.
4. Actualizar herramientas de instalación.
5. Instalar y registrar dependencias mínimas.
6. Crear un checkpoint y hacer push.
7. Construir e interpretar el inventario técnico.

