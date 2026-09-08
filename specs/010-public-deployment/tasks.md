# Tareas: despliegue público del dashboard Dash

- [x] **TASK-001** — Elegir y justificar la plataforma. Cubre REQ-001, REQ-004,
  REQ-008 / AC-001, AC-002, AC-005.
  - Validación: requisitos oficiales, coste y límites documentados.
- [x] **TASK-002** — Añadir el Blueprint reproducible. Cubre REQ-001, REQ-002,
  REQ-003, REQ-004 / AC-001, AC-002.
  - Dependencias: TASK-001.
  - Validación: configuración mínima y coherente con `Dockerfile`.
- [x] **TASK-003** — Publicar y validar el servicio. Cubre REQ-005, REQ-006,
  REQ-007 / AC-003, AC-004.
  - Dependencias: TASK-002 y autorización de acceso a Render.
  - Validación: URL pública, salud y recorridos principales.
- [x] **TASK-004** — Documentar y cerrar la entrega. Cubre REQ-008, REQ-009 /
  AC-005, AC-006.
  - Dependencias: TASK-003.
  - Validación: README, issue, SDD, tests, commit y push.

## Registro de progreso

- 2026-09-08: se selecciona Render Web Service con runtime Docker y plan gratuito.
  La aplicación no necesita base de datos, disco persistente ni secretos.
- 2026-09-08: se identifica como riesgo principal el límite gratuito de 512 MB y se
  conserva un trabajador para no duplicar el DataFrame.
- 2026-09-08: `render.yaml` declara un único servicio Docker gratuito y `/health`.
  La prueba con `PORT=10000` responde correctamente y utiliza aproximadamente 182
  MiB en reposo. Se desactiva el socket de control opcional de Gunicorn porque el
  usuario seguro del contenedor no tiene directorio personal escribible.
- 2026-09-08: Render publica el commit `86b6a1e` desde
  `feat/010-public-deployment` en
  `https://project8-airbnb-dashboard.onrender.com`. El servicio aparece como Docker,
  gratuito y gestionado por Blueprint.
- 2026-09-08: la URL pública reproduce los controles globales, el filtro de Madrid,
  la navegación hacia calidad y el estado vacío de Tokio con habitación de hotel.
  `/health` confirma seis ciudades, 220.031 anuncios y `status: ok`.
