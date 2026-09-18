# Pokémon Champions Battle Copilot

Copiloto competitivo local para Champions Doubles: preview, estado de batalla, inferencia del rival, cálculos, simulación y recomendaciones justificadas.

**Estado: base documental; aplicación todavía no implementada.** Este repositorio no contiene un motor de batalla operativo. La V1 completa conserva el alcance de la especificación aportada por Jairo.

## Empezar con un agente

Lee [AGENTS.md](AGENTS.md), [state.md](state.md) y el [mapa de contexto](docs/agents/CONTEXT_MAP.md). La siguiente unidad de trabajo es [SPEC-001: dominio y datos](specs/001-domain-data/spec.md). Usa su propuesta, diseño, tareas y verificaciones. No saltes directamente a la interfaz.

## Documentación

- [Spec original íntegra](docs/source/V1_SPEC_ORIGINAL.md) y [procedencia](docs/source/PROVENANCE.md).
- [Visión](docs/product/VISION.md), [alcance](docs/product/SCOPE.md), [requisitos](docs/product/REQUIREMENTS.md), [glosario](docs/product/GLOSSARY.md).
- [ARD](docs/architecture/ARD.md), [arquitectura](docs/architecture/ARCHITECTURE.md), [contratos](docs/architecture/API_CONTRACTS.md), [invariantes](docs/architecture/INVARIANTS.md), [decisiones ADR](docs/adr/README.md).
- [Memoria](memory.md), [convenciones](conventions.md), [roadmap](docs/planning/ROADMAP.md), [preguntas abiertas](docs/planning/OPEN_QUESTIONS.md).
- [SDD y TDD](docs/workflows/SDD_TDD.md), [subagentes](docs/agents/ORCHESTRATION.md), [skills](docs/agents/SKILL_CATALOG.md), [trazabilidad](docs/quality/TRACEABILITY.md), [aceptación V1](docs/quality/V1_ACCEPTANCE.md).

## Validar esta base documental

```sh
python3 scripts/validate_docs.py
```

Valida conservación de la fuente, cobertura documental de sus 62 secciones y 34 criterios de cierre, enlaces locales y metadatos de skills. No ejecuta tests del producto ni prueba corrección de mecánicas.

Vitest, TypeScript, Next.js y los comandos del monorepo se configurarán en SPEC-001. No se documentan como disponibles hasta que funcionen.
