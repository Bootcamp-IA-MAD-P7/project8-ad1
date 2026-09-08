# Plan: despliegue público del dashboard Dash

## Especificación relacionada

- `specs/010-public-deployment/spec.md`

## Situación inicial

La aplicación y el contenedor ya fueron reconciliados localmente. El repositorio no
dispone de configuración para una plataforma pública ni de una URL compartible.

## Estrategia

Usar un Blueprint mínimo de Render para que la plataforma construya el `Dockerfile`
desde GitHub. No se duplicará el comando de arranque ni se crearán servicios que la
aplicación no necesita. La URL y la evidencia se documentarán solo después de validar
el despliegue real.

## Cambios previstos

| Archivo o área | Responsabilidad | Requisitos |
|---|---|---|
| `render.yaml` | Servicio, runtime, plan y healthcheck | REQ-001 a REQ-004 |
| `README.md` | URL, actualización, coste y mantenimiento | REQ-008, REQ-009 |
| `specs/010-public-deployment/` | Decisiones, criterios y evidencia | REQ-001 a REQ-009 |
| GitHub issue #27 | Resultado verificable del despliegue | REQ-009 |

## Validación

1. Revisar que el Blueprint no contenga variables secretas.
2. Reconstruir la imagen Docker local sin utilizar caché de aplicación.
3. Medir de forma orientativa el uso de memoria del contenedor.
4. Publicar la rama y crear el servicio gratuito desde el Blueprint.
5. Verificar `/health`, `/`, recursos estáticos, pestañas, filtros y estado vacío.
6. Registrar URL y commit; ejecutar SDD y tests antes del cierre.

## Condiciones de parada

- Solicitar intervención si Render requiere inicio de sesión o autorización de GitHub.
- No continuar si la única opción visible requiere pago.
- Si la memoria gratuita es insuficiente, medir y optimizar antes de proponer gasto.

