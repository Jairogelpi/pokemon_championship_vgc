---
name: copilot-design
description: Diseñar contratos y decisiones del motor Champions manteniendo dominio, proveedores y simulación separados.
---

# copilot-design

Aplicar dentro de este repositorio y del alcance asignado. Las rutas siguientes son relativas a la raíz del repo; localizarla por AGENTS.md. No otorga permisos adicionales ni arranca otros agentes por sí sola.

1. Revisar DOMAIN_MODEL, invariantes y contratos vigentes; no crear tipos duplicados por paquete.
2. Definir inputs/outputs/error/versiones y direcciones de dependencia antes de consumidores paralelos.
3. Separar evento observado de transición simulada y estado persistido de rama hipotética.
4. Crear ADR para decisión estructural con alternativas; mantener propuesto lo no investigado.

## Referencias a cargar según tarea

- [docs/architecture/ARD.md](../../../docs/architecture/ARD.md)
- [docs/architecture/DOMAIN_MODEL.md](../../../docs/architecture/DOMAIN_MODEL.md)
- [docs/architecture/INVARIANTS.md](../../../docs/architecture/INVARIANTS.md)
- [templates/ADR.md](../../../templates/ADR.md)

## Salida

Handoff con tarea, archivos, decisiones, evidencia ejecutada, límites y siguiente acción. Si falta un dato imprescindible, explicitar qué parte bloquea y continuar únicamente las tareas independientes.
