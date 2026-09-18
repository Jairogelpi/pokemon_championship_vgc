---
name: copilot-spec
description: Descomponer la spec original del Battle Copilot en aceptación verificable sin perder requisitos.
---

# copilot-spec

Aplicar dentro de este repositorio y del alcance asignado. Las rutas siguientes son relativas a la raíz del repo; localizarla por AGENTS.md. No otorga permisos adicionales ni arranca otros agentes por sí sola.

1. Localizar REQ-Sxx y subcasos de la fuente; no trabajar solo a partir del título del requisito.
2. Separar intención, ejemplos y reglas no verificadas; enlazar OPEN_QUESTIONS si hay conflicto.
3. Definir entradas, salidas, errores, casos Given/When/Then y límites; una carpeta no equivale a READY.
4. Crear diseño/tareas/verificación al activar la fase; mantener fuente inmutable y trazabilidad.

## Referencias a cargar según tarea

- [docs/product/REQUIREMENTS.md](../../../docs/product/REQUIREMENTS.md)
- [docs/planning/OPEN_QUESTIONS.md](../../../docs/planning/OPEN_QUESTIONS.md)
- [templates/SPEC.md](../../../templates/SPEC.md)

## Salida

Handoff con tarea, archivos, decisiones, evidencia ejecutada, límites y siguiente acción. Si falta un dato imprescindible, explicitar qué parte bloquea y continuar únicamente las tareas independientes.
