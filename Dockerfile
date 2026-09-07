# syntax=docker/dockerfile:1

FROM python:3.14.7-slim-trixie

LABEL org.opencontainers.image.title="Dashboard exploratorio de alojamientos"
LABEL org.opencontainers.image.description="Aplicación Dash portable del proyecto de análisis"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PORT=8050

WORKDIR /app

RUN addgroup --system --gid 10001 dashboard \
    && adduser --system --uid 10001 --ingroup dashboard --no-create-home dashboard

COPY requirements-dashboard.txt ./requirements-dashboard.txt

RUN python -m pip install \
    --no-cache-dir \
    --requirement requirements-dashboard.txt

COPY --chown=dashboard:dashboard scripts/prepare_dashboard_data.py ./scripts/prepare_dashboard_data.py
COPY --chown=dashboard:dashboard data/manifest.csv ./data/manifest.csv
COPY --chown=dashboard:dashboard data/raw/airbnb/ ./data/raw/airbnb/
COPY --chown=dashboard:dashboard dashboard/dash_app.py ./dashboard/dash_app.py
COPY --chown=dashboard:dashboard dashboard/assets/ ./dashboard/assets/

USER dashboard

EXPOSE 8050

HEALTHCHECK --interval=30s --timeout=5s --start-period=45s --retries=3 \
    CMD python -c "import os, urllib.request; urllib.request.urlopen('http://127.0.0.1:' + os.getenv('PORT', '8050') + '/health', timeout=4)"

CMD ["sh", "-c", "exec gunicorn --bind 0.0.0.0:${PORT:-8050} --workers 1 --threads 4 --timeout 120 --access-logfile - dashboard.dash_app:server"]
