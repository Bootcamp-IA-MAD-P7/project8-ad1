---
id: 000
title: Infraestructura inicial de Spec Driven Development
status: done
owner: equipo del proyecto
created: 2026-08-25
updated: 2026-08-25
---

# Especificación: infraestructura inicial de SDD

## Problema y contexto

El repositorio contiene las consignas generales, pero no dispone de una forma
versionada y verificable de convertirlas en incrementos con alcance, criterios de
aceptación, tareas y decisiones explícitas.

## Objetivos

- Establecer una convención SDD sencilla para todo el repositorio.
- Hacer trazables requisitos, criterios de aceptación y tareas.
- Proporcionar plantillas reutilizables y una validación automática sin dependencias.
- Incorporar las reglas pedagógicas del proyecto al contexto operativo de Codex.

## Fuera de alcance

- Analizar o modificar el dataset.
- Elegir herramientas de EDA, dashboard, gestión Kanban o despliegue.
- Definir todas las especificaciones de las fases futuras.
- Automatizar la calidad semántica o la comprensión humana de los documentos.

## Requisitos

- **REQ-001**: el repositorio debe documentar la estructura y el ciclo de vida SDD.
- **REQ-002**: cada incremento debe poder describir requisitos, plan y tareas trazables.
- **REQ-003**: las decisiones materiales deben disponer de un formato versionable.
- **REQ-004**: una comprobación local sin dependencias externas debe detectar errores
  estructurales básicos en las especificaciones.
- **REQ-005**: las reglas de trabajo deben preservar el carácter educativo y gradual.
- **REQ-006**: los artefactos locales y secretos habituales no deben entrar
  accidentalmente en el control de versiones.
- **REQ-007**: las consignas originales deben conservarse separadas de la portada y
  de las especificaciones aprobadas, con enlaces claros entre los tres niveles.

## Criterios de aceptación

- **AC-001** (cubre REQ-001): existe `specs/README.md` con estructura, estados y flujo.
- **AC-002** (cubre REQ-002): existen plantillas para `spec.md`, `plan.md` y `tasks.md`.
- **AC-003** (cubre REQ-003): existe una plantilla para registrar decisiones materiales.
- **AC-004** (cubre REQ-004): el validador acepta esta especificación y sus tests pasan.
- **AC-005** (cubre REQ-005): `AGENTS.md` convierte los principios pedagógicos en reglas
  operativas aplicables al repositorio.
- **AC-006** (cubre REQ-001): el README principal explica cómo iniciar y validar un cambio.
- **AC-007** (cubre REQ-006): `.gitignore` excluye cachés, entornos virtuales y `.env`
  sin excluir genéricamente los datasets del proyecto.
- **AC-008** (cubre REQ-007): `docs/project-brief.md` conserva el briefing, objetivos,
  entregables, tecnologías, datos, niveles y evaluación originales; `README.md` actúa
  como portada y enlaza tanto las consignas como las especificaciones.
- **AC-009** (cubre REQ-004, REQ-007): el validador informa de un error cuando falta
  `docs/project-brief.md`.

## Datos y supuestos

- SDD no impone un estándar universal; esta convención es propia del repositorio.
- Python estará disponible cuando comience el análisis, pero el validador usa solo
  la biblioteca estándar.
- Las especificaciones y decisiones se revisan mediante Git.
- Las consignas son contexto de entrada: solo una spec aprobada convierte una parte
  de ellas en alcance comprometido.

## Riesgos y limitaciones

- Demasiada documentación puede frenar el aprendizaje; por eso solo hay tres
  documentos obligatorios y las decisiones separadas son condicionales.
- Un validador estructural no puede determinar si un requisito es bueno o si una
  conclusión analítica está respaldada por los datos.

## Preguntas abiertas

No hay preguntas que bloqueen este incremento. La primera especificación analítica
deberá decidir qué dataset o ciudad entra en alcance.

## Definition of Done

- [x] Todos los criterios de aceptación están verificados.
- [x] Resultados y limitaciones están interpretados y documentados.
- [x] README, reglas, plantillas, tests y especificación son coherentes.
