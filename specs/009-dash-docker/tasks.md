# Tareas: dashboard web portable con Dash y Docker

- [x] **TASK-001** — Definir el alcance portable sin sustituir Power BI. Cubre
  REQ-009, REQ-010 / AC-008.
  - Dependencias: dashboard de Power BI validado.
  - Validación: spec aprobada antes de crear la aplicación.
- [x] **TASK-002** — Instalar y registrar Dash y Plotly para ejecución local. Cubre
  REQ-007, REQ-010 / AC-004, AC-007.
  - Dependencias: TASK-001.
  - Validación: imports y versiones confirmados en el entorno virtual.
- [x] **TASK-003** — Crear y comprender la aplicación Dash mínima. Cubre REQ-002,
  REQ-006 / AC-001, AC-003.
  - Dependencias: TASK-002.
  - Validación: la página responde localmente con HTTP 200.
- [x] **TASK-004** — Conectar datos, métricas, filtros y visuales. Cubre REQ-001,
  REQ-002, REQ-003, REQ-004, REQ-005, REQ-006 / AC-001, AC-002, AC-003.
  - Dependencias: TASK-003.
  - Validación: recorridos y controles reconciliados.
- [x] **TASK-005** — Añadir dependencias, Dockerfile y exclusiones. Cubre REQ-007,
  REQ-008, REQ-009 / AC-004, AC-005, AC-006.
  - Dependencias: TASK-004.
  - Validación: imagen construida y contenedor saludable.
- [x] **TASK-006** — Documentar y validar la entrega. Cubre REQ-010 / AC-007, AC-008.
  - Dependencias: TASK-005.
  - Validación: README, SDD, tests, Git y tarjeta #23 revisados.

## Registro de progreso

- 2026-09-07: se confirma que el `.pbix` no es un proceso ejecutable en un contenedor
  Linux; se elige una extensión compacta con Dash que reutiliza el diseño y los datos.
- 2026-09-07: Docker 29.5.2 y Compose 5.1.3 están disponibles. Los seis CSV están
  versionados y ocupan aproximadamente 31 MB.
- 2026-09-07: se registran `dash==4.4.1` y `plotly==7.0.0` para desarrollo local.
- 2026-09-07: la aplicación Dash completa carga los datos una vez, expone las dos
  áreas de decisión y responde con HTTP 200 junto con su hoja de estilos.
- 2026-09-07: la prueba lógica reconcilia 220.031 anuncios, 75,35 % con reseñas,
  30 segmentos destacados y los controles 50/20/123. La combinación inexistente
  Tokio + habitación de hotel devuelve un estado vacío sin errores. Queda pendiente
  la revisión visual humana antes de cerrar TASK-004.
- 2026-09-07: tras la primera revisión visual, la interfaz adopta una estética limpia
  inspirada en el sitio de Airbnb —coral como acento, fondo blanco, tipografía oscura,
  filtros redondeados y tarjetas suaves— sin usar logotipos ni presentarse como un
  producto oficial. Los KPIs y el endpoint de salud continúan reconciliados.
- 2026-09-07: se crean `Dockerfile`, `.dockerignore` y
  `requirements-dashboard.txt`. La imagen queda limitada a la aplicación, la lógica
  compartida y los seis CSV originales; arranca con Gunicorn, un solo trabajador y
  un usuario sin privilegios.
- 2026-09-07: la imagen `airbnb-offer-dashboard:local` se construye, el contenedor
  publica `localhost:8050`, permanece saludable y `/health` devuelve seis ciudades,
  220.031 anuncios y estado `ok`.
- 2026-09-07: README documenta ejecución local y Docker, el validador revisa diez
  especificaciones correctamente y los cuatro tests pasan.
