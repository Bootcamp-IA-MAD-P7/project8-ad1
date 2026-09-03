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

## 🗂️ Estructura del repositorio

```text
project-ai-data-analyst/
├── data/           # Datos originales y manifiesto de integridad
├── docs/           # Brief, diccionario y preguntas de negocio
├── notebooks/      # Inventario, comprensión de datos y EDA consolidado
├── scripts/        # Validación automática de especificaciones
├── specs/          # Requisitos, planes, tareas y decisiones SDD
├── tests/          # Tests del validador SDD
└── requirements.txt
```

Los CSV originales se conservan en `data/raw/airbnb/`. Su procedencia, reglas de
conservación y hashes están documentados en [`data/README.md`](data/README.md) y
[`data/manifest.csv`](data/manifest.csv).

## ▶️ Ejecutar el análisis

Con el entorno virtual activado, JupyterLab se inicia con:

```bash
python -m jupyter lab
```

Los notebooks deben leerse y ejecutarse en este orden:

1. `notebooks/01_data_inventory.ipynb`: inventario técnico.
2. `notebooks/02_data_understanding.ipynb`: diccionario y calidad de los datos.
3. `notebooks/03_exploratory_analysis.ipynb`: EDA e insights consolidados.

Para comprobar su reproducibilidad sin utilizar la interfaz gráfica:

```bash
python -m jupyter nbconvert --execute --to notebook --inplace notebooks/01_data_inventory.ipynb --ExecutePreprocessor.timeout=600
python -m jupyter nbconvert --execute --to notebook --inplace notebooks/02_data_understanding.ipynb --ExecutePreprocessor.timeout=600
python -m jupyter nbconvert --execute --to notebook --inplace notebooks/03_exploratory_analysis.ipynb --ExecutePreprocessor.timeout=600
```

Los avisos de ZMQ sobre el bucle de eventos o el transporte local del kernel en
Windows no representan fallos si la ejecución finaliza y `nbconvert` escribe el
notebook sin outputs de error.

## 🗂️ Documentación

| Documento | Responsabilidad |
|---|---|
| [`docs/project-brief.md`](docs/project-brief.md) | Consignas originales y niveles de entrega |
| [`specs/README.md`](specs/README.md) | Convención y ciclo de vida SDD |
| [`specs/000-sdd-infrastructure/spec.md`](specs/000-sdd-infrastructure/spec.md) | Infraestructura SDD inicial |
| [`specs/002-analysis-foundation/spec.md`](specs/002-analysis-foundation/spec.md) | Entorno reproducible e inventario técnico |
| [`specs/003-data-understanding/spec.md`](specs/003-data-understanding/spec.md) | Diccionario y evaluación inicial de calidad |
| [`specs/004-eda/spec.md`](specs/004-eda/spec.md) | Preguntas de negocio para orientar el EDA |
| [`specs/005-exploratory-analysis/spec.md`](specs/005-exploratory-analysis/spec.md) | Ejecución del EDA esencial y notebook consolidado |
| [`specs/006-project-delivery/spec.md`](specs/006-project-delivery/spec.md) | Revisión técnica, presentación y demo final |
| [`notebooks/03_exploratory_analysis.ipynb`](notebooks/03_exploratory_analysis.ipynb) | EDA esencial ejecutado, interpretado y consolidado |
| [`AGENTS.md`](AGENTS.md) | Reglas educativas y operativas del repositorio |

## 📍 Estado actual

La infraestructura SDD, el entorno reproducible, el inventario técnico, el
diccionario de variables, la evaluación inicial de calidad y las preguntas de
negocio están validados. El EDA esencial está completado mediante tres checkpoints:
análisis univariante, relaciones y segmentos, y consolidación del notebook. Las
preguntas sobre disponibilidad y concentración por anfitrión permanecen como
extensiones opcionales.
