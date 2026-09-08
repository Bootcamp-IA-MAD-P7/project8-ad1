---
id: 010
title: Despliegue público del dashboard Dash
status: approved
owner: desarrolladora del proyecto
created: 2026-09-08
updated: 2026-09-08
---

# Especificación: despliegue público del dashboard Dash

## Problema y contexto

La tarjeta #23 dejó una aplicación Dash reproducible y una imagen Docker saludable
en local. La tarjeta #27 exige que una versión quede accesible mediante una URL
pública, sin exponer secretos y con límites operativos documentados.

## Decisión de plataforma

Se selecciona **Render Web Service** con runtime Docker y plan gratuito porque:

- puede construir directamente el `Dockerfile` versionado;
- proporciona una URL pública con HTTPS administrado;
- admite una ruta HTTP de salud y despliegues desde GitHub;
- no requiere base de datos, almacenamiento persistente ni credenciales de la app;
- permite describir la infraestructura en `render.yaml`.

No se selecciona un hosting estático porque Dash ejecuta callbacks en el servidor.
Tampoco se introduce un registro de imágenes: Render construirá desde el repositorio
para conservar la relación entre código y versión desplegada.

## Objetivos

- Publicar la versión Dash ya validada sin cambiar sus métricas.
- Mantener la configuración de despliegue pequeña, versionada y reproducible.
- Validar la página inicial, las dos áreas, los filtros y `/health` desde internet.
- Documentar versión, mantenimiento, coste y limitaciones del plan gratuito.

## Fuera de alcance

- Comprar capacidad, dominio, almacenamiento o disponibilidad garantizada.
- Añadir autenticación, analítica de usuarios o una base de datos.
- Publicar el archivo `.pbix` como aplicación web.
- Incorporar secretos al repositorio o a la imagen.
- Ejecutar las tarjetas de Machine Learning o enriquecimiento de datos.

## Requisitos

- **REQ-001**: `render.yaml` debe declarar un único servicio web Docker en el plan
  gratuito y reutilizar el `Dockerfile` de la raíz.
- **REQ-002**: el proceso debe escuchar en `0.0.0.0` y en el puerto proporcionado por
  la variable `PORT` de Render.
- **REQ-003**: Render debe comprobar la disponibilidad mediante `GET /health`.
- **REQ-004**: no se deben declarar secretos, credenciales, discos ni servicios
  adicionales porque la aplicación solo utiliza datos públicos versionados.
- **REQ-005**: la URL pública debe devolver HTTP 200 para `/` y `/health`.
- **REQ-006**: la versión pública debe reconciliar seis ciudades y 220.031 anuncios.
- **REQ-007**: se deben comprobar la navegación entre áreas, los filtros globales y
  al menos una combinación vacía ya prevista por el dashboard.
- **REQ-008**: README debe incluir la URL, la plataforma, el flujo de actualización y
  las limitaciones relevantes del servicio gratuito.
- **REQ-009**: la evidencia de la tarjeta debe identificar commit, pruebas, coste y
  mantenimiento sin publicar datos de cuenta ni credenciales.

## Criterios de aceptación

- **AC-001** (cubre REQ-001, REQ-002, REQ-003): Render acepta la configuración,
  construye la imagen e inicia el proceso sin sustituir el comando seguro existente.
- **AC-002** (cubre REQ-004): repositorio, Blueprint, imagen y logs no contienen
  secretos ni credenciales.
- **AC-003** (cubre REQ-005, REQ-006): `/` y `/health` son accesibles públicamente;
  salud devuelve `status: ok`, seis ciudades y 220.031 anuncios.
- **AC-004** (cubre REQ-007): las pestañas, filtros y estados vacíos funcionan en la
  URL pública sin errores visibles.
- **AC-005** (cubre REQ-008, REQ-009): README e issue documentan URL, plataforma,
  versión, pruebas, coste, arranque en frío, mantenimiento y procedimiento de cambio.
- **AC-006** (cubre REQ-009): validador SDD y tests pasan, Git queda limpio y la rama
  de la fase se publica antes del cierre.

## Datos y supuestos

- La versión desplegada utilizará los seis CSV públicos incluidos en la imagen.
- La aplicación seguirá validando 220.031 IDs únicos y seis ciudades al arrancar.
- Los archivos se tratarán como datos de solo lectura; el servicio no recibe uploads.
- Render proporcionará `PORT` en ejecución y construirá desde una rama publicada.
- No existe actualización automática de la fuente: cualquier cambio requiere commit,
  nueva construcción y validación de la URL.

## Configuración y seguridad

- El servicio se denominará `project8-airbnb-dashboard`.
- Render seleccionará el puerto mediante `PORT`; el valor local 8050 seguirá siendo
  únicamente el predeterminado del contenedor.
- La ruta de salud será `/health`.
- El contenedor mantendrá el usuario sin privilegios definido en `Dockerfile`.
- No se necesitan variables secretas. Cualquier valor futuro sensible deberá
  configurarse en Render y nunca escribirse en Git.

## Coste, límites y mantenimiento

- El plan elegido tiene coste inicial cero y recursos limitados.
- La instancia gratuita puede suspenderse después de 15 minutos sin tráfico; la
  primera visita posterior puede tardar aproximadamente un minuto.
- El sistema de archivos es efímero. No afecta a esta aplicación porque los CSV se
  incluyen en la imagen y no se escriben datos durante la ejecución.
- Render puede reiniciar la instancia y limita horas, ancho de banda y minutos de
  construcción incluidos.
- Cada push posterior a la rama conectada puede producir una nueva construcción. La
  URL debe volver a comprobarse después de cambios en datos, dependencias o arranque.

## Riesgos y limitaciones

- **Memoria**: el plan gratuito ofrece 512 MB. Se conserva un solo trabajador para
  evitar duplicar el DataFrame en memoria.
- **CPU y arranque**: regenerar 220.031 filas con 0,1 CPU puede ser lento. El endpoint
  solo estará disponible después de completar los controles de datos.
- **Demostración**: el servicio debe abrirse antes del ensayo para evitar que el
  arranque en frío interrumpa la presentación.
- **Disponibilidad**: el plan gratuito no es producción y no ofrece disponibilidad
  garantizada; se conserva Docker local como alternativa reproducible.

## Preguntas abiertas

La única acción externa prevista es autorizar a Render para leer el repositorio o
indicar su URL pública. No se autoriza seleccionar un plan de pago.

## Definition of Done

- [ ] `render.yaml` está versionado y coincide con Docker.
- [ ] El servicio público está activo y saludable.
- [ ] Los recorridos principales se validan desde la URL pública.
- [ ] README y la tarjeta #27 documentan evidencia y limitaciones.
- [ ] Tests, SDD y Git quedan validados y la rama publicada.
