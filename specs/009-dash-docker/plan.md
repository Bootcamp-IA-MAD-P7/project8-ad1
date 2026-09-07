# Plan: dashboard web portable con Dash y Docker

## Especificación relacionada

- `specs/009-dash-docker/spec.md`

## Situación actual

Power BI contiene dos páginas validadas y `prepare_dashboard_data.py` genera una
fuente reconciliada desde seis CSV. Docker y Compose están instalados localmente, pero
no existen todavía una aplicación web, un `Dockerfile` ni exclusiones de contexto.
La referencia `specs/007-advanced-dashboard/` de la tarjeta #23 no existe; se adopta
el siguiente identificador correlativo, 009.

## Enfoque propuesto

Construir primero una aplicación Dash local y comprensible. Después de validar sus
datos y filtros, añadir una imagen Linux con Gunicorn, un usuario sin privilegios y
una comprobación de salud. El mismo código servirá posteriormente para la tarjeta de
despliegue público.

## Cambios previstos

| Archivo o área | Responsabilidad | Requisitos |
|---|---|---|
| `dashboard/dash_app.py` | Layout, gráficos, tablas, filtros y callbacks | REQ-001 a REQ-006 |
| `dashboard/assets/style.css` | Presentación responsive y legible | REQ-002, REQ-006 |
| `requirements.txt` | Ejecución local de Dash y Plotly | REQ-010 |
| `requirements-dashboard.txt` | Dependencias mínimas del contenedor | REQ-007 |
| `Dockerfile` | Imagen, usuario, puerto, salud y arranque | REQ-007 a REQ-009 |
| `.dockerignore` | Exclusión de secretos y artefactos innecesarios | REQ-008 |
| `README.md` | Guía local y Docker | REQ-010 |

## Estrategia de validación

| Comprobación | Resultado esperado | Criterios |
|---|---|---|
| Ejecutar Dash localmente | HTTP 200 y vista inicial completa | AC-001 |
| Probar filtros | Selecciones globales y vacías coherentes | AC-002, AC-003 |
| Reconciliar controles | 220.031, 50, 20 y 123 | AC-001 |
| Construir imagen | `docker build` finaliza sin errores | AC-004, AC-005 |
| Iniciar contenedor | Aplicación accesible en el puerto 8050 | AC-005 |
| Consultar salud y logs | HTTP 200 y proceso estable | AC-006 |
| Validar repositorio | SDD, tests y Git correctos | AC-007, AC-008 |

## Riesgos y alternativas

- Se evitará cargar un DataFrame por trabajador; el contenedor comenzará con un solo
  trabajador y varios hilos, suficiente para la demo.
- Se usarán copias explícitas en el `Dockerfile` y `.dockerignore` para mantener el
  contexto acotado.
- Si la carga desde los CSV excede el tiempo del servidor, se ampliará únicamente el
  timeout de inicio después de medirlo, sin ocultar callbacks lentos.

## Secuencia

1. Instalar y registrar Dash y Plotly.
2. Crear una aplicación mínima y comprobarla en el navegador.
3. Conectar la fuente y reconciliar indicadores.
4. Incorporar filtros y las dos áreas de negocio.
5. Añadir dependencias Linux, Dockerfile y exclusiones.
6. Construir, iniciar, verificar y documentar el contenedor.
