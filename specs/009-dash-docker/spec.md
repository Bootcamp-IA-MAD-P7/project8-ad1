---
id: 009
title: Dashboard web portable con Dash y Docker
status: done
owner: desarrolladora del proyecto
created: 2026-09-07
updated: 2026-09-07
---

# Especificación: dashboard web portable con Dash y Docker

## Problema y contexto

El dashboard oficial está implementado en Power BI Desktop, pero un archivo `.pbix`
no puede iniciarse como aplicación dentro de un contenedor Linux. La tarjeta #23 pide
una versión portable cuyo contenedor inicie el dashboard.

Se construirá una extensión web compacta con Dash, reutilizando la fuente, las
métricas y las decisiones ya validadas. No se repetirá el EDA ni se buscará una copia
visual exacta de Power BI.

## Objetivos

- Crear una aplicación Dash comprensible que se ejecute localmente.
- Conservar los filtros de ciudad y tipo de alojamiento.
- Representar las dos decisiones del dashboard: priorización de oferta y revisión de
  calidad o restricciones.
- Empaquetar la aplicación y sus datos necesarios en una imagen Docker reproducible.
- Documentar construcción, ejecución, comprobación y limitaciones.

## Fuera de alcance

- Ejecutar o convertir el `.pbix` dentro del contenedor.
- Reproducir cada detalle visual de Power BI.
- Añadir nuevas métricas, fuentes externas, autenticación o base de datos.
- Corregir los CSV originales o almacenar secretos en la imagen.
- Publicar la aplicación en internet; el despliegue corresponde a la tarjeta #27.

## Requisitos

- **REQ-001**: la aplicación debe regenerar su fuente desde los seis CSV originales
  mediante la lógica existente y conservar una fila por anuncio y ciudad.
- **REQ-002**: la vista inicial debe mostrar el volumen de anuncios y las señales
  principales sin exigir interacción previa.
- **REQ-003**: los filtros globales de ciudad y tipo deben actualizar los componentes
  aplicables y permitir volver al conjunto completo.
- **REQ-004**: la sección de oferta debe incluir composición por tipo y segmentos o
  barrios útiles para investigación.
- **REQ-005**: la sección de calidad debe mostrar precios no positivos, estancias
  extremas y reseñas sin frecuencia mensual.
- **REQ-006**: las etiquetas deben conservar las cautelas sobre moneda, fecha de
  extracción y actividad aproximada.
- **REQ-007**: el contenedor debe usar una imagen oficial de Python, dependencias
  mínimas y fijadas, un usuario sin privilegios y un servidor apropiado para Linux.
- **REQ-008**: el contexto de construcción no debe incluir `.env`, `.git`, `.venv`,
  notebooks, el `.pbix` ni datos procesados innecesarios.
- **REQ-009**: la imagen debe construirse, iniciar el dashboard y responder mediante
  HTTP en un puerto configurable, con una comprobación de salud.
- **REQ-010**: README y la tarjeta #23 deben conservar comandos, resultados y rutas
  suficientes para reproducir la prueba.

## Criterios de aceptación

- **AC-001** (cubre REQ-001, REQ-002): la aplicación local inicia y reconcilia
  220.031 anuncios, 50 precios no positivos, 20 estancias de al menos 1000 noches y
  123 reseñas sin frecuencia.
- **AC-002** (cubre REQ-003, REQ-004, REQ-005): ciudad y tipo actualizan tarjetas,
  gráficos y tablas aplicables sin mostrar datos de otra selección.
- **AC-003** (cubre REQ-004, REQ-005, REQ-006): las dos áreas responden preguntas de
  negocio distintas y no presentan reseñas como demanda ni comparan monedas.
- **AC-004** (cubre REQ-007, REQ-008): `Dockerfile`, `.dockerignore` y el archivo de
  dependencias del contenedor son pequeños, legibles y no incorporan secretos.
- **AC-005** (cubre REQ-009): `docker build` termina correctamente y `docker run`
  publica la aplicación en `localhost:8050`.
- **AC-006** (cubre REQ-009): la comprobación de salud devuelve HTTP 200 y el
  contenedor permanece en ejecución sin errores.
- **AC-007** (cubre REQ-010): README documenta ejecución local, construcción,
  arranque, parada y verificación del contenedor.
- **AC-008** (cubre REQ-010): validador SDD, tests y estado Git quedan revisados antes
  del cierre.

## Datos y supuestos

- La fuente controladora son los seis CSV registrados en `data/manifest.csv`.
- La aplicación reutilizará `scripts/prepare_dashboard_data.py` para evitar dos
  definiciones de las métricas.
- Los datos se cargarán una vez al iniciar el proceso; cualquier cambio de los CSV
  requerirá reiniciar la aplicación.
- Dash y Plotly se usarán localmente; Gunicorn se utilizará únicamente dentro del
  contenedor Linux.
- El puerto predeterminado será 8050 y podrá configurarse mediante `PORT`.
- Power BI continúa siendo el entregable oficial; Dash aporta portabilidad y prepara
  el posible despliegue público.

## Riesgos y limitaciones

- Cargar 220.031 filas en memoria puede aumentar el tiempo de arranque; se usará un
  solo proceso de datos y tablas de salida limitadas.
- Los CSV originales añaden aproximadamente 31 MB al contexto necesario de la imagen.
- Los filtros no resuelven combinaciones inexistentes; deben producir un estado vacío
  comprensible.
- `reviews_per_month` sigue siendo una aproximación y no mide reservas u ocupación.
- El precio no tiene código de moneda común entre ciudades.
- El `.pbix` es un artefacto binario independiente y no debe modificarse como efecto
  lateral de esta implementación.

## Preguntas abiertas

No existen decisiones abiertas que bloqueen el inicio. El despliegue y la URL pública
se tratarán únicamente después de validar el contenedor.

## Definition of Done

- [x] La aplicación Dash funciona localmente con sus filtros y dos áreas de decisión.
- [x] La imagen Docker se construye y el contenedor responde con HTTP 200.
- [x] Dependencias, datos, configuración y exclusiones están documentados.
- [x] README, tarjeta #23, código, specs y tests son coherentes.
