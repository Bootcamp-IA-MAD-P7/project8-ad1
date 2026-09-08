# 🚀 PROYECTO DATA ANALYST: Análisis y visualización de datos

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

## 🗂️ Estructura del repositorio

```text
project-ai-data-analyst/
├── dashboard/      # Dashboard de Power BI y aplicación web Dash
├── data/           # Datos originales, manifiesto y derivados reproducibles
├── docs/           # Diccionario, preguntas, validación y guion de demo
├── notebooks/      # Inventario, comprensión de datos y EDA consolidado
├── presentation/   # Presentación final editable
├── scripts/        # Preparación reproducible de la fuente del dashboard
├── requirements.txt
├── requirements-dashboard.txt
├── Dockerfile
└── render.yaml
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

### Dashboard público en Render

La versión desplegada está disponible en:

> **[Abrir el dashboard público](https://project8-airbnb-dashboard.onrender.com)**

Render construye el `Dockerfile` mediante el Blueprint versionado en `render.yaml` y
comprueba la ruta [`/health`](https://project8-airbnb-dashboard.onrender.com/health).
El servicio está conectado a la rama `feat/010-public-deployment`; para publicar un
cambio se debe hacer commit y push en esa rama, esperar a que finalice la nueva
construcción y volver a validar la página principal y el endpoint de salud.

Se utiliza el plan gratuito, sin base de datos, disco persistente ni variables
secretas. Este plan puede suspender la instancia después de un periodo sin tráfico,
por lo que la primera visita puede tardar 50 segundos o más. Sus recursos son
limitados y no ofrecen disponibilidad de producción. Para una demo conviene abrir la
URL con antelación. Los datos forman parte de la imagen y no se actualizan solos: un
cambio en los CSV requiere un nuevo despliegue.

## 🗂️ Documentación

| Documento | Responsabilidad |
|---|---|
| [`docs/data-dictionary.md`](docs/data-dictionary.md) | Definición y alcance de las variables utilizadas |
| [`docs/eda-business-questions.md`](docs/eda-business-questions.md) | Preguntas de negocio que orientan el análisis |
| [`notebooks/03_exploratory_analysis.ipynb`](notebooks/03_exploratory_analysis.ipynb) | EDA esencial ejecutado, interpretado y consolidado |
| [`notebooks/04_statistical_analysis.ipynb`](notebooks/04_statistical_analysis.ipynb) | Contrastes estadísticos ejecutados e interpretados |
| [`docs/dashboard-design.md`](docs/dashboard-design.md) | Audiencia, preguntas, KPIs y boceto del dashboard |
| [`docs/dashboard-validation.md`](docs/dashboard-validation.md) | Reconciliación y revisión técnica del archivo de Power BI |
| [`presentation/airbnb_offer_analysis_final.pptx`](presentation/airbnb_offer_analysis_final.pptx) | Presentación final editable con evidencia y notas del orador |
| [`docs/final-demo-guide.md`](docs/final-demo-guide.md) | Guion, ruta de demo, contingencia y checklist de ensayo |

## 📍 Estado actual

El entorno reproducible, el inventario técnico, el diccionario de variables, la
evaluación inicial de calidad y las preguntas de negocio están documentados. El EDA
esencial está completado mediante tres etapas:
análisis univariante, relaciones y segmentos, y consolidación del notebook. Las
preguntas sobre disponibilidad y concentración por anfitrión permanecen como
extensiones opcionales. El dashboard de Power BI está implementado y validado. El
análisis estadístico identifica una asociación pequeña entre ciudad y tipo de
alojamiento y menor actividad aproximada en estancias superiores a ocho noches en
las seis ciudades. Además, el dashboard dispone de una versión web reproducible con
Dash y Docker, validada localmente y desplegada públicamente en Render. La
presentación final y el guion de demo ya están preparados con evidencia del EDA,
los contrastes y el dashboard. Para cerrar la entrega queda realizar y registrar el
ensayo humano completo.
