---
name: copilot-engine-tdd
description: Implementar daño, speed, legalidad y resolución determinista de Champions con pruebas y reglas verificadas.
---

# copilot-engine-tdd

Aplicar dentro de este repositorio y del alcance asignado. Las rutas siguientes son relativas a la raíz del repo; localizarla por AGENTS.md. No otorga permisos adicionales ni arranca otros agentes por sí sola.

1. Partir de aceptación y fuente mecánica; si no existe oráculo, devolver no verificado sin fabricar golden.
2. Ejecutar RED por comportamiento, GREEN mínimo y refactor. Registrar comandos reales y resultados.
3. Inyectar ruleset y RNG; probar prioridades, ties, switches, efectos/KO y aislamiento según módulo.
4. Comparar dual validation solo en casos compatibles; discrepancias conservadas, tolerancia cero determinista. No editar upstream in-place.

## Referencias a cargar según tarea

- [docs/quality/TEST_STRATEGY.md](../../../docs/quality/TEST_STRATEGY.md)
- [docs/architecture/INVARIANTS.md](../../../docs/architecture/INVARIANTS.md)
- [docs/workflows/SDD_TDD.md](../../../docs/workflows/SDD_TDD.md)

## Salida

Handoff con tarea, archivos, decisiones, evidencia ejecutada, límites y siguiente acción. Si falta un dato imprescindible, explicitar qué parte bloquea y continuar únicamente las tareas independientes.
