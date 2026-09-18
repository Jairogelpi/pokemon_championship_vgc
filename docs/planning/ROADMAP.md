# Roadmap de implementación

Conserva las 16 fases del original §58. Estado inicial de todas: PENDING. La numeración indica secuencia solicitada; las dependencias indican qué puede adelantarse sin inventar contratos. SPEC-001 se desglosa; las demás se expanden a proposal/design/tasks/verification al activarse.

| Fase | Entrega | Dependencias | Estado |
|---|---|---|---|
| [SPEC-001](../../specs/001-domain-data/spec.md) | Domain + Champions data | Ninguna | PENDING |
| [SPEC-002](../../specs/002-team-store/spec.md) | Nuestro Team Store | 001 | PENDING |
| [SPEC-003](../../specs/003-damage-engine/spec.md) | Damage Engine | 001, 002 | PENDING |
| [SPEC-004](../../specs/004-speed-engine/spec.md) | Speed Engine | 001 | PENDING |
| [SPEC-005](../../specs/005-battle-events/spec.md) | BattleState + Events | 001, 002 | PENDING |
| [SPEC-006](../../specs/006-turn-resolver/spec.md) | Turn Resolver | 003, 004, 005 | PENDING |
| [SPEC-007](../../specs/007-action-generator/spec.md) | Action Generator | 001, 005 | PENDING |
| [SPEC-008](../../specs/008-meta-engine/spec.md) | Meta Engine | 001 | PENDING |
| [SPEC-009](../../specs/009-belief-engine/spec.md) | Belief Engine | 005, 008 | PENDING |
| [SPEC-010](../../specs/010-preview-solver/spec.md) | Preview Solver | 002, 003, 004, 007, 008, 009 | PENDING |
| [SPEC-011](../../specs/011-simulator/spec.md) | Simulator | 006, 007, 009 | PENDING |
| [SPEC-012](../../specs/012-search-engine/spec.md) | Search Engine | 011 | PENDING |
| [SPEC-013](../../specs/013-recommendation-engine/spec.md) | Recommendation Engine | 010, 012 | PENDING |
| [SPEC-014](../../specs/014-llm-tools/spec.md) | LLM tool layer | 013 | PENDING |
| [SPEC-015](../../specs/015-web-ui/spec.md) | Web UI | 005, 010, 013, 014 | PENDING |
| [SPEC-016](../../specs/016-replay-debug/spec.md) | Replay + debugging | 015 | PENDING |

## Orden y paralelismo

SPEC-006 usa un puerto de legalidad para validar acciones proporcionadas. SPEC-007 completa enumeración exhaustiva; no hay que hacer que resolver dependa del generador. El contrato del puerto se fija en SPEC-001. La rama de meta/datos puede adelantarse sin bloquear daño/speed; el cierre de cada fase sigue sus dependencias reales.

## Definition of Ready

Fuente/requisitos vinculados, aceptación con casos límite, contratos concretos, fuentes mecánicas disponibles para el alcance y tareas acotadas. Si solo una parte está lista, dividir tarea; no declarar listo todo el motor.

## Definition of Done por fase

Código integrado, tests adecuados ejecutados, evidencia reproducible, límites explícitos, revisión y trazabilidad/state actualizados. Para fases con reglas: fixtures y procedencia verificadas. Para V1: además todos los criterios de V1_ACCEPTANCE y los requisitos transversales.
