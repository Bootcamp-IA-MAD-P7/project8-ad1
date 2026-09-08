# Guion de presentación y demo final

## Objetivo y duración

Presentar en **8 minutos** un diagnóstico reproducible de la oferta de Airbnb en
seis ciudades. El mensaje central es que el proyecto ayuda a decidir **qué
segmentos investigar** y **qué registros revisar**, sin afirmar reservas,
ocupación o rentabilidad.

### Mensaje de apertura

> Este proyecto le sirve a Airbnb como herramienta de diagnóstico y priorización,
> pero todavía no para tomar decisiones comerciales importantes. Permite priorizar
> 30 segmentos, crear una cola operativa de revisión, detectar la asociación entre
> estancias mínimas largas y menor actividad aproximada, y explorar la evidencia en
> un dashboard reproducible. La decisión que facilita es: **¿qué segmentos y anuncios
> debe revisar primero el equipo de operaciones?**

## Guion sugerido

1. **Portada — 30 s.** Explicar el alcance: 220.031 anuncios de seis ciudades.
2. **Decisiones — 45 s.** Separar oportunidad de oferta y revisión de calidad.
3. **Datos — 40 s.** Explicar la unificación en un DataFrame conservando la ciudad.
4. **Método — 45 s.** Resumir inventario, calidad, EDA, estadística y producto.
5. **Composición — 50 s.** Mostrar el peso de vivienda completa y las diferencias.
6. **Segmentos — 60 s.** Explicar índice de precio, actividad y regla candidata.
7. **Estancia mínima — 60 s.** Explicar Mann-Whitney, Holm, efecto y no causalidad.
8. **Calidad — 45 s.** Mostrar las tres reglas y la revisión manual recomendada.
9. **Demo — 90 s.** Recorrer filtros, tabla, calidad y estado sin datos.
10. **Conclusión — 40 s.** Diferenciar decisiones actuales de futuras ampliaciones.

## Ruta de demo

1. Abrir <https://project8-airbnb-dashboard.onrender.com/> antes de presentar para
   despertar el servicio gratuito de Render.
2. En **Oportunidades de oferta**, filtrar por ciudad y explicar que el precio se
   compara dentro de cada ciudad y tipo mediante un índice, no entre monedas.
3. Seleccionar un segmento y señalar volumen, índice de precio y actividad aproximada.
4. Abrir **Calidad de datos**, elegir una regla y mostrar los registros afectados.
5. Probar una combinación sin datos para demostrar que el dashboard controla el
   estado vacío.
6. Si se pregunta por el despliegue, abrir
   <https://project8-airbnb-dashboard.onrender.com/health> y explicar que Dash se
   sirve con Gunicorn dentro de Docker y se despliega en Render.

## Respuestas breves a preguntas previsibles

- **¿Actividad significa reservas?** No. `reviews_per_month` es una aproximación y
  solo sirve para comparar patrones dentro de este conjunto.
- **¿Los segmentos son oportunidades rentables?** No. Son candidatos para
  investigación porque combinan escala, precio relativo y actividad aproximada.
- **¿Por qué no se comparan precios entre ciudades?** Las monedas no están
  documentadas y no se aplicó conversión.
- **¿Un valor extremo es necesariamente un error?** No. Se marca para revisión y
  no se elimina automáticamente.
- **¿El contraste demuestra causalidad?** No. Detecta una diferencia de distribución
  asociada a la estancia mínima, con tamaño de efecto explícito.

## Plan de contingencia

- Mantener abierta la presentación, que contiene capturas del dashboard.
- Si Render tarda en despertar, explicar la captura y continuar sin bloquear la demo.
- Conservar Power BI Desktop como evidencia alternativa local.
- No editar datos ni código durante la presentación.

## Checklist de ensayo

- [ ] El archivo `presentation/airbnb_offer_analysis_final.pptx` abre correctamente.
- [ ] La exposición completa dura entre 7 y 9 minutos.
- [ ] El dashboard público carga y los filtros responden.
- [ ] La página de calidad muestra registros al seleccionar una regla.
- [ ] La combinación sin datos presenta un mensaje comprensible.
- [ ] Se explican índice de precio, proxy de actividad y límites sin ambigüedad.
- [ ] Se nombra el alcance de las mejoras #24, #25 y #26 sin presentarlas como hechas.
- [ ] Validación SDD y tests ejecutados antes de la entrega.
- [ ] `git status` limpio en el commit final.

**Fecha del ensayo:** pendiente

**Duración:** pendiente

**Incidencias y ajustes:** pendiente
