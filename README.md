# 🚀 PROYECTO DATA ANALYST: Análisis y visualización de datos

![DataAnalyst](https://github.com/user-attachments/assets/f9a0c97d-856b-4b33-b448-c20f0deb2979)

## 🧭 Forma de trabajo: Spec Driven Development

El proyecto avanza mediante incrementos pequeños definidos antes de su
implementación. Las especificaciones son la fuente de verdad y se encuentran en
[`specs/`](specs/README.md).

Antes de comenzar un cambio importante:

1. Crear `specs/NNN-nombre/` a partir de las plantillas.
2. Acordar alcance, requisitos y criterios de aceptación en `spec.md`.
3. Documentar la estrategia en `plan.md` y las unidades verificables en `tasks.md`.
4. Implementar una tarea cada vez, validar e interpretar el resultado.
5. Comprobar la estructura con:

> Requisito: Python 3.9 o superior disponible en el entorno activo.

```bash
python scripts/validate_specs.py
python -m unittest discover -s tests -v
```

La infraestructura inicial y sus decisiones están documentadas en
[`specs/000-sdd-infrastructure/`](specs/000-sdd-infrastructure/spec.md).

## 🐍 Entorno de desarrollo

El análisis utiliza **Python 3.14.5** y declara sus dependencias directas en
[`requirements.txt`](requirements.txt). Desde Git Bash, el entorno puede recrearse
con estos comandos:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
```

Para comprobar que la terminal está utilizando el entorno correcto y que las
dependencias principales están disponibles:

```bash
which python
python --version
python -c "import pandas, jupyterlab, notebook; print('pandas', pandas.__version__); print('jupyterlab', jupyterlab.__version__); print('notebook', notebook.__version__)"
```

`which python` debe apuntar a `.venv/Scripts/python` y la versión debe ser
Python 3.14.5. Para salir del entorno se utiliza `deactivate`. La carpeta `.venv/`
es local, está excluida mediante `.gitignore` y no debe subirse al repositorio.
El paquete `notebook` se conserva como dependencia directa para disponer también
de la interfaz clásica mediante `python -m jupyter notebook`.

## 📌 Sobre el proyecto

El proyecto parte de datos de alojamientos de Airbnb en distintas ciudades. Su
finalidad educativa es construir un análisis reproducible, obtener conclusiones
útiles para negocio y comunicar los resultados mediante un notebook, un dashboard
y una presentación técnica.

Las instrucciones entregadas originalmente se conservan, sin convertir
automáticamente todos sus niveles opcionales en requisitos aprobados, en
[`docs/project-brief.md`](docs/project-brief.md).

## 🗂️ Documentación

| Documento | Responsabilidad |
|---|---|
| [`docs/project-brief.md`](docs/project-brief.md) | Consignas originales y niveles de entrega |
| [`specs/README.md`](specs/README.md) | Convención y ciclo de vida SDD |
| [`specs/000-sdd-infrastructure/spec.md`](specs/000-sdd-infrastructure/spec.md) | Infraestructura SDD inicial |
| [`specs/002-analysis-foundation/spec.md`](specs/002-analysis-foundation/spec.md) | Entorno reproducible e inventario técnico |
| [`AGENTS.md`](AGENTS.md) | Reglas educativas y operativas del repositorio |

## 📍 Estado actual

La infraestructura SDD y el entorno Python reproducible están preparados. El
siguiente incremento será crear el inventario técnico de los seis CSV antes de
iniciar su limpieza o análisis exploratorio.
