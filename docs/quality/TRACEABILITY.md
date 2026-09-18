# Trazabilidad de origen a implementación

Cobertura documental, no validación funcional. `PENDING` significa que falta evidencia de producto. Al implementar, añadir rutas reales de tests y registro de ejecución con commit; no borrar la relación con la fuente.

| Requisito | Sección original | Spec responsable | Evidencia de producto |
|---|---|---|---|
| REQ-S00 | §0 Objetivo | [SPEC-016](../../specs/016-replay-debug/spec.md) | PENDING |
| REQ-S01 | §1 Principio fundamental | [SPEC-001](../../specs/001-domain-data/spec.md) | PENDING |
| REQ-S02 | §2 Repositorios upstream | [SPEC-001](../../specs/001-domain-data/spec.md) | PENDING |
| REQ-S03 | §3 Monorepo | [SPEC-001](../../specs/001-domain-data/spec.md) | PENDING |
| REQ-S04 | §4 Stack | [SPEC-001](../../specs/001-domain-data/spec.md) | PENDING |
| REQ-S05 | §5 Modelo central | [SPEC-001](../../specs/001-domain-data/spec.md) | PENDING |
| REQ-S06 | §6 Pokémon State | [SPEC-001](../../specs/001-domain-data/spec.md) | PENDING |
| REQ-S07 | §7 Equipo del usuario | [SPEC-002](../../specs/002-team-store/spec.md) | PENDING |
| REQ-S08 | §8 Rival | [SPEC-005](../../specs/005-battle-events/spec.md) | PENDING |
| REQ-S09 | §9 Belief Engine | [SPEC-009](../../specs/009-belief-engine/spec.md) | PENDING |
| REQ-S10 | §10 Ejemplo de inferencia | [SPEC-009](../../specs/009-belief-engine/spec.md) | PENDING |
| REQ-S11 | §11 Meta Engine | [SPEC-008](../../specs/008-meta-engine/spec.md) | PENDING |
| REQ-S12 | §12 Archetype Detector | [SPEC-008](../../specs/008-meta-engine/spec.md) | PENDING |
| REQ-S13 | §13 Damage Engine | [SPEC-003](../../specs/003-damage-engine/spec.md) | PENDING |
| REQ-S14 | §14 Dual validation | [SPEC-003](../../specs/003-damage-engine/spec.md) | PENDING |
| REQ-S15 | §15 Speed Engine | [SPEC-004](../../specs/004-speed-engine/spec.md) | PENDING |
| REQ-S16 | §16 Field State | [SPEC-001](../../specs/001-domain-data/spec.md) | PENDING |
| REQ-S17 | §17 Turn Engine | [SPEC-006](../../specs/006-turn-resolver/spec.md) | PENDING |
| REQ-S18 | §18 Action Generator | [SPEC-007](../../specs/007-action-generator/spec.md) | PENDING |
| REQ-S19 | §19 Legalidad | [SPEC-007](../../specs/007-action-generator/spec.md) | PENDING |
| REQ-S20 | §20 Mega constraint | [SPEC-007](../../specs/007-action-generator/spec.md) | PENDING |
| REQ-S21 | §21 Turn resolution | [SPEC-006](../../specs/006-turn-resolver/spec.md) | PENDING |
| REQ-S22 | §22 RNG | [SPEC-006](../../specs/006-turn-resolver/spec.md) | PENDING |
| REQ-S23 | §23 Protect | [SPEC-006](../../specs/006-turn-resolver/spec.md) | PENDING |
| REQ-S24 | §24 Fake Out | [SPEC-006](../../specs/006-turn-resolver/spec.md) | PENDING |
| REQ-S25 | §25 Trick Room | [SPEC-004](../../specs/004-speed-engine/spec.md) | PENDING |
| REQ-S26 | §26 Tailwind | [SPEC-004](../../specs/004-speed-engine/spec.md) | PENDING |
| REQ-S27 | §27 Switch Engine | [SPEC-006](../../specs/006-turn-resolver/spec.md) | PENDING |
| REQ-S28 | §28 Simulator | [SPEC-011](../../specs/011-simulator/spec.md) | PENDING |
| REQ-S29 | §29 Opponent Action Model | [SPEC-011](../../specs/011-simulator/spec.md) | PENDING |
| REQ-S30 | §30 Search Engine | [SPEC-012](../../specs/012-search-engine/spec.md) | PENDING |
| REQ-S31 | §31 Evaluación del estado | [SPEC-012](../../specs/012-search-engine/spec.md) | PENDING |
| REQ-S32 | §32 Material score | [SPEC-012](../../specs/012-search-engine/spec.md) | PENDING |
| REQ-S33 | §33 Risk metrics | [SPEC-012](../../specs/012-search-engine/spec.md) | PENDING |
| REQ-S34 | §34 Recommendation Engine | [SPEC-013](../../specs/013-recommendation-engine/spec.md) | PENDING |
| REQ-S35 | §35 Preview Solver | [SPEC-010](../../specs/010-preview-solver/spec.md) | PENDING |
| REQ-S36 | §36 Preview output | [SPEC-010](../../specs/010-preview-solver/spec.md) | PENDING |
| REQ-S37 | §37 LLM Tool Layer | [SPEC-014](../../specs/014-llm-tools/spec.md) | PENDING |
| REQ-S38 | §38 LLM System Contract | [SPEC-014](../../specs/014-llm-tools/spec.md) | PENDING |
| REQ-S39 | §39 Anti-hallucination | [SPEC-014](../../specs/014-llm-tools/spec.md) | PENDING |
| REQ-S40 | §40 Battle Copilot UI | [SPEC-015](../../specs/015-web-ui/spec.md) | PENDING |
| REQ-S41 | §41 Team Preview UI | [SPEC-015](../../specs/015-web-ui/spec.md) | PENDING |
| REQ-S42 | §42 Battle input V1 | [SPEC-015](../../specs/015-web-ui/spec.md) | PENDING |
| REQ-S43 | §43 Quick Input | [SPEC-005](../../specs/005-battle-events/spec.md) | PENDING |
| REQ-S44 | §44 Event sourcing | [SPEC-005](../../specs/005-battle-events/spec.md) | PENDING |
| REQ-S45 | §45 Persistence | [SPEC-005](../../specs/005-battle-events/spec.md) | PENDING |
| REQ-S46 | §46 Replay | [SPEC-016](../../specs/016-replay-debug/spec.md) | PENDING |
| REQ-S47 | §47 Feedback loop | [SPEC-009](../../specs/009-belief-engine/spec.md) | PENDING |
| REQ-S48 | §48 API | [SPEC-016](../../specs/016-replay-debug/spec.md) | PENDING |
| REQ-S49 | §49 `/preview/analyze` | [SPEC-010](../../specs/010-preview-solver/spec.md) | PENDING |
| REQ-S50 | §50 `/recommend` | [SPEC-013](../../specs/013-recommendation-engine/spec.md) | PENDING |
| REQ-S51 | §51 Performance target | [SPEC-013](../../specs/013-recommendation-engine/spec.md) | PENDING |
| REQ-S52 | §52 Cache | [SPEC-013](../../specs/013-recommendation-engine/spec.md) | PENDING |
| REQ-S53 | §53 Testing strategy | [SPEC-016](../../specs/016-replay-debug/spec.md) | PENDING |
| REQ-S54 | §54 Golden tests críticos | [SPEC-006](../../specs/006-turn-resolver/spec.md) | PENDING |
| REQ-S55 | §55 Damage validation suite | [SPEC-003](../../specs/003-damage-engine/spec.md) | PENDING |
| REQ-S56 | §56 Observability | [SPEC-013](../../specs/013-recommendation-engine/spec.md) | PENDING |
| REQ-S57 | §57 Failure modes | [SPEC-013](../../specs/013-recommendation-engine/spec.md) | PENDING |
| REQ-S58 | §58 Orden de implementación | [SPEC-016](../../specs/016-replay-debug/spec.md) | PENDING |
| REQ-S59 | §59 V1 Definition of Done | [SPEC-016](../../specs/016-replay-debug/spec.md) | PENDING |
| REQ-S60 | §60 NO entra en V1 | [SPEC-001](../../specs/001-domain-data/spec.md) | PENDING |
| REQ-S61 | §61 Resultado final V1 | [SPEC-016](../../specs/016-replay-debug/spec.md) | PENDING |
