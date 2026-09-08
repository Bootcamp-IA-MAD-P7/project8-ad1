# 🚀 PROYECTO DATA ANALYST: Análisis y visualización de datos

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
python -c "import pandas, scipy, jupyterlab, notebook; print('pandas', pandas.__version__); print('scipy', scipy.__version__); print('jupyterlab', jupyterlab.__version__); print('notebook', notebook.__version__)"
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
├── dashboard/      # Dashboard de Power BI y aplicación web Dash
├── data/           # Datos originales, manifiesto y derivados reproducibles
├── docs/           # Brief, diccionario, preguntas y diseño del dashboard
├── notebooks/      # Inventario, comprensión de datos y EDA consolidado
├── scripts/        # Validación SDD y preparación de la fuente del dashboard
├── specs/          # Requisitos, planes, tareas y decisiones SDD
├── tests/          # Tests del validador SDD
├── requirements.txt
├── requirements-dashboard.txt
└── Dockerfile
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
4. `notebooks/04_statistical_analysis.ipynb`: hipótesis, supuestos y tamaños del efecto.

Para comprobar su reproducibilidad sin utilizar la interfaz gráfica:

```bash
python -m jupyter nbconvert --execute --to notebook --inplace notebooks/01_data_inventory.ipynb --ExecutePreprocessor.timeout=600
python -m jupyter nbconvert --execute --to notebook --inplace notebooks/02_data_understanding.ipynb --ExecutePreprocessor.timeout=600
python -m jupyter nbconvert --execute --to notebook --inplace notebooks/03_exploratory_analysis.ipynb --ExecutePreprocessor.timeout=600
python -m jupyter nbconvert --execute --to notebook --inplace notebooks/04_statistical_analysis.ipynb --ExecutePreprocessor.timeout=600
```

Los avisos de ZMQ sobre el bucle de eventos o el transporte local del kernel en
Windows no representan fallos si la ejecución finaliza y `nbconvert` escribe el
notebook sin outputs de error.

## 📊 Abrir y reproducir el dashboard

El dashboard se encuentra en
[`dashboard/airbnb_offer_dashboard.pbix`](dashboard/airbnb_offer_dashboard.pbix) y
se abre con Power BI Desktop. Contiene dos páginas:

1. **Oferta y posicionamiento**: composición de la oferta, actividad aproximada por
   barrio y segmentos seleccionados para investigación.
2. **Calidad y restricciones**: precios no positivos, estancias mínimas llamativas e
   inconsistencias en la frecuencia mensual de reseñas.

La fuente derivada se regenera desde los seis CSV originales mediante:

```bash
python scripts/prepare_dashboard_data.py
```

El comando crea `data/processed/airbnb_dashboard.csv`, que está excluido de Git por
ser un archivo generado. Los CSV se descargaron el 27 de agosto de 2026; la fecha de
extracción del proveedor y las monedas no están documentadas. La actividad de reseñas
es un indicador aproximado y no equivale a reservas, demanda u ocupación.

### Versión web con Dash

La versión web portable reutiliza la misma preparación validada y conserva las áreas
de **oferta y posicionamiento** y **calidad y restricciones**. Con el entorno virtual
activo se inicia mediante:

```bash
python dashboard/dash_app.py
```

La aplicación queda disponible en `http://localhost:8050`. Los datos se cargan una
vez al iniciar el proceso; si cambia alguno de los CSV, es necesario reiniciarlo.

### Ejecutar el dashboard con Docker

Requisito: Docker Desktop debe estar iniciado. Desde la raíz del repositorio:

```bash
docker build -t airbnb-offer-dashboard:local .
docker run --detach --name airbnb-offer-dashboard -p 8050:8050 airbnb-offer-dashboard:local
```

La primera orden construye la imagen. La segunda inicia el contenedor en segundo
plano y publica el dashboard en `http://localhost:8050`. Su estado y la reconciliación
básica pueden comprobarse con:

```bash
docker ps --filter name=airbnb-offer-dashboard
curl http://localhost:8050/health
docker logs --tail 50 airbnb-offer-dashboard
```

La comprobación de salud debe devolver `status: ok`, seis ciudades y 220.031
anuncios. Para detenerlo y volver a iniciarlo sin crear otro contenedor:

```bash
docker stop airbnb-offer-dashboard
docker start airbnb-offer-dashboard
```

Cuando ya no se necesite ese contenedor, se puede eliminar después de detenerlo:

```bash
docker rm airbnb-offer-dashboard
```

La imagen utiliza Gunicorn con un único trabajador para no duplicar en memoria el
DataFrame de 220.031 filas. Se ejecuta con un usuario sin privilegios y solo incorpora
la aplicación, las dependencias web, la preparación compartida y los seis CSV
originales. `.dockerignore` excluye el entorno virtual, Git, secretos locales,
notebooks, tests, el archivo `.pbix` y datos procesados.

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
| [`specs/007-dashboard/spec.md`](specs/007-dashboard/spec.md) | Diseño, implementación y validación del dashboard |
| [`specs/008-statistical-analysis/spec.md`](specs/008-statistical-analysis/spec.md) | Hipótesis y métodos para el contraste estadístico |
| [`specs/009-dash-docker/spec.md`](specs/009-dash-docker/spec.md) | Versión web portable del dashboard con Dash y Docker |
| [`specs/010-public-deployment/spec.md`](specs/010-public-deployment/spec.md) | Despliegue público reproducible del dashboard Dash |
| [`notebooks/03_exploratory_analysis.ipynb`](notebooks/03_exploratory_analysis.ipynb) | EDA esencial ejecutado, interpretado y consolidado |
| [`notebooks/04_statistical_analysis.ipynb`](notebooks/04_statistical_analysis.ipynb) | Contrastes estadísticos ejecutados e interpretados |
| [`docs/dashboard-design.md`](docs/dashboard-design.md) | Audiencia, preguntas, KPIs y boceto del dashboard |
| [`docs/dashboard-validation.md`](docs/dashboard-validation.md) | Reconciliación y revisión técnica del archivo de Power BI |
| [`AGENTS.md`](AGENTS.md) | Reglas educativas y operativas del repositorio |

## 📍 Estado actual

La infraestructura SDD, el entorno reproducible, el inventario técnico, el
diccionario de variables, la evaluación inicial de calidad y las preguntas de
negocio están validados. El EDA esencial está completado mediante tres checkpoints:
análisis univariante, relaciones y segmentos, y consolidación del notebook. Las
preguntas sobre disponibilidad y concentración por anfitrión permanecen como
extensiones opcionales. El dashboard de Power BI está implementado y validado. El
análisis estadístico identifica una asociación pequeña entre ciudad y tipo de
alojamiento y menor actividad aproximada en estancias superiores a ocho noches en
las seis ciudades. Además, el dashboard dispone de una versión web reproducible con
Dash y Docker, validada localmente con un contenedor saludable. La presentación y la
demo final permanecen pendientes hasta cerrar los incrementos que se puedan completar
dentro del calendario.
