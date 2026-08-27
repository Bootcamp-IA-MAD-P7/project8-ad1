---
id: 002
title: Entorno reproducible e inventario técnico de datos
status: in-progress
owner: desarrolladora del proyecto
created: 2026-08-27
updated: 2026-08-27
---

# Especificación: entorno reproducible e inventario técnico de datos

## Problema y contexto

Los seis CSV originales ya están versionados y verificados, pero todavía no existe
un entorno Python aislado ni un inventario reproducible de su estructura. El equipo
de desarrollo está formado por una sola persona y utilizará Bash para trabajar.

## Objetivos

- Crear un entorno virtual local y reproducible con Python 3.14.5.
- Instalar únicamente las dependencias necesarias para importar y explorar los CSV.
- Declarar las dependencias directas del proyecto.
- Verificar que Bash utiliza el intérprete del entorno virtual.
- Generar posteriormente un inventario comparable de las seis ciudades.

## Fuera de alcance

- Limpiar, transformar o concatenar los datasets.
- Resolver diferencias de esquemas.
- Crear visualizaciones o conclusiones de EDA.
- Instalar Conda o una segunda versión de Python.
- Instalar anticipadamente librerías de modelado o dashboard.

## Requisitos

- **REQ-001**: el entorno debe crearse en `.venv/` con el CPython 3.14.5 estándar.
- **REQ-002**: `.venv/` no debe incluirse en Git.
- **REQ-003**: Pandas y JupyterLab deben instalarse mediante `pip` dentro del entorno.
- **REQ-004**: las dependencias directas y la versión de Python deben documentarse.
- **REQ-005**: la activación debe verificarse desde Bash mediante la ruta del intérprete.
- **REQ-006**: el inventario técnico debe cubrir los seis CSV sin modificarlos.

## Criterios de aceptación

- **AC-001** (cubre REQ-001): `.venv/` existe y reporta Python 3.14.5.
- **AC-002** (cubre REQ-002): `git status` no propone archivos internos de `.venv/`.
- **AC-003** (cubre REQ-003): Python puede importar Pandas y JupyterLab desde `.venv/`.
- **AC-004** (cubre REQ-004): existe una declaración mínima de dependencias y el
  README explica cómo crear y activar el entorno desde Bash.
- **AC-005** (cubre REQ-005): `which python` apunta a `.venv/Scripts/python`.
- **AC-006** (cubre REQ-006): el inventario registra filas, columnas, cabeceras y
  diferencias de esquema para las seis ciudades.
- **AC-007** (cubre REQ-001 a REQ-006): las validaciones SDD y los tests pasan.

## Datos y supuestos

- El comando `python` resuelve al CPython estándar de 64 bits instalado en Windows.
- Pandas dispone de distribución precompilada compatible con CPython 3.14 en Windows.
- JupyterLab se distribuye como paquete Python independiente de plataforma.
- Git Bash está disponible y será la terminal utilizada por la desarrolladora.

## Riesgos y limitaciones

- Python 3.14 es reciente; una dependencia futura podría no ofrecer aún compatibilidad.
- La variante libre de GIL `python3.14t.exe` no se utilizará para evitar complejidad
  innecesaria en un proyecto educativo.
- Un archivo de dependencias directas no bloquea todas las dependencias transitivas;
  se prioriza claridad y se registrarán versiones verificadas.
- Las diferencias de esquema pueden exigir decisiones adicionales durante el inventario.

## Preguntas abiertas

No hay preguntas que bloqueen la creación del entorno. El formato final del inventario
se decidirá al comenzar la tarjeta #7, después de comprobar los datos con Pandas.

## Definition of Done

- [x] El entorno `.venv` está creado, activado y verificado desde Bash.
- [x] Las dependencias mínimas están instaladas y documentadas.
- [x] El entorno puede recrearse siguiendo el README.
- [ ] El inventario técnico de los seis CSV está generado e interpretado.
- [ ] Las validaciones pasan y los checkpoints están publicados en la rama remota.
