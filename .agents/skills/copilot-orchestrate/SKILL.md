---
name: copilot-orchestrate
description: Coordinar tareas SDD y handoffs del Battle Copilot, con dependencias, contexto y límites de escritura.
---

# copilot-orchestrate

Aplicar dentro de este repositorio y del alcance asignado. Las rutas siguientes son relativas a la raíz del repo; localizarla por AGENTS.md. No otorga permisos adicionales ni arranca otros agentes por sí sola.

1. Leer state y roadmap; elegir siguiente tarea desbloqueada, no una fase arbitraria.
2. Cargar spec y skill del rol; entregar asignación según templates/HANDOFF.md con rutas de escritura exclusivas.
3. Delegar solo si el runtime dispone de capacidad y la tarea lo justifica; si no, ejecutar roles secuencialmente.
4. Integrar por dependencia; comprobar evidencia antes de marcar progreso. Mantener state/memory/traceability como escritor único.

## Referencias a cargar según tarea

- [docs/agents/ORCHESTRATION.md](../../../docs/agents/ORCHESTRATION.md)
- [docs/agents/CONTEXT_MAP.md](../../../docs/agents/CONTEXT_MAP.md)
- [docs/workflows/SDD_TDD.md](../../../docs/workflows/SDD_TDD.md)

## Salida

Handoff con tarea, archivos, decisiones, evidencia ejecutada, límites y siguiente acción. Si falta un dato imprescindible, explicitar qué parte bloquea y continuar únicamente las tareas independientes.
