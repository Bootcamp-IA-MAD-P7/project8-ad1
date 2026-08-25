# Reglas de trabajo del proyecto

Este repositorio se desarrolla con **Spec Driven Development (SDD)** y con un
objetivo educativo. La fuente de verdad de cada incremento está en `specs/`.

## Antes de implementar

1. Localizar y leer la especificación aplicable.
2. Revisar el estado real del repositorio y de los datos.
3. Identificar alcance, criterios de aceptación, preguntas abiertas y riesgos.
4. Explicar los conceptos nuevos y proponer el incremento verificable más pequeño.
5. No implementar requisitos ambiguos ni ampliar silenciosamente el alcance.

Si todavía no existe una especificación, crearla y acordar sus decisiones
materiales antes de implementar la funcionalidad.

## Forma de trabajo

- Seguir el ciclo: explicar, analizar, decidir, implementar, validar e interpretar.
- Avanzar mediante cambios pequeños, legibles y reproducibles.
- Tratar una decisión material cada vez. Una decisión es material cuando cambia
  requisitos, datos, arquitectura, dependencias, seguridad o criterios de aceptación.
- Las decisiones pequeñas y reversibles pueden documentarse y ejecutarse sin
  interrumpir innecesariamente el flujo.
- No iniciar una fase posterior (por ejemplo, modelado) al completar una anterior
  (por ejemplo, EDA) sin una petición o especificación que la incluya.
- Mantener coherencia entre `README.md`, `specs/`, código y tests.

## Trabajo con datos

- Cada gráfico debe responder una pregunta y terminar con una interpretación.
- No transformar datos antes de comprender el problema que resuelve la transformación.
- Diferenciar limpieza, preprocessing y feature engineering.
- Antes de modelar, definir un baseline, la estrategia de partición y las métricas.
- Ajustar sobre entrenamiento toda transformación que aprenda parámetros y revisar
  explícitamente posibles fugas de información (*data leakage*).
- Presentar métricas, tablas, gráficos y errores con significado y consecuencias,
  no como resultados aislados.

## Calidad y seguridad

- Preferir soluciones sencillas, nombres descriptivos y funciones pequeñas.
- Añadir dependencias solo cuando estén justificadas y documentadas.
- Los tests deben proteger comportamiento relevante, no inflar cobertura.
- No eliminar ni sobrescribir datasets, notebooks, configuraciones o trabajo ajeno.
- No hacer `push`, reescribir historial ni ejecutar operaciones destructivas sin
  autorización explícita.

## Definition of Done

Un incremento está terminado cuando cumple sus criterios de aceptación, pasa sus
validaciones, documenta decisiones y limitaciones relevantes, interpreta los
resultados y deja claro el siguiente paso. La comprensión de la persona
desarrolladora es un criterio de revisión humana, no una comprobación automatizable.

