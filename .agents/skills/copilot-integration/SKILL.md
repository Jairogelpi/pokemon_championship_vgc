---
name: copilot-integration
description: Integrar API, SQLite, herramientas LLM y UI del Copilot preservando confirmación y degradación.
---

# copilot-integration

Aplicar dentro de este repositorio y del alcance asignado. Las rutas siguientes son relativas a la raíz del repo; localizarla por AGENTS.md. No otorga permisos adicionales ni arranca otros agentes por sí sola.

1. Cargar contrato de la fase; validar límites con esquemas y errores explícitos.
2. Comprobar transacciones, commandId, expectedRevision y no duplicación de efectos.
3. Parser/record_observation solo proponen; la confirmación del usuario pasa por el caso de uso de eventos.
4. No escribir reglas dentro de UI; mostrar unknown/stale/unverified y descartar recomendaciones de revisión vieja.
5. Probar LLM timeout y offline: recomendación matemática disponible; eliminar secretos de traces.

## Referencias a cargar según tarea

- [docs/architecture/API_CONTRACTS.md](../../../docs/architecture/API_CONTRACTS.md)
- [docs/architecture/DATA_FLOW.md](../../../docs/architecture/DATA_FLOW.md)
- [docs/architecture/SYSTEM_CONTEXT.md](../../../docs/architecture/SYSTEM_CONTEXT.md)

## Salida

Handoff con tarea, archivos, decisiones, evidencia ejecutada, límites y siguiente acción. Si falta un dato imprescindible, explicitar qué parte bloquea y continuar únicamente las tareas independientes.
