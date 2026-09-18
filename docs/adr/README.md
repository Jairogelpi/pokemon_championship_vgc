# Registro de decisiones de arquitectura

ARD contiene los requisitos; ADR documenta cómo y por qué se resuelven. Cada ADR incluye estado, contexto, decisión, alternativas, consecuencias y verificación. Numeración estable; una revocación crea otro ADR y enlaza al anterior.

| ADR | Tema | Estado |
|---|---|---|
| [0001](0001-context-and-traceability.md) | Contexto selectivo, fuente inmutable y trazabilidad | accepted para bootstrap |
| [0002](0002-deterministic-core.md) | Núcleo determinista y LLM restringido | accepted, derivado de spec |
| [0003](0003-events-and-replay.md) | Event log, proyección y simulación aislada | accepted en principio; detalle SPEC-005 |
| [0004](0004-upstream-adapters.md) | Reutilización con adaptadores y versiones | accepted, auditoría upstream pendiente |

ORM, gestor de paquetes, versiones, semántica ply y política completa de undo requieren ADR posteriores cuando se investiguen; no se presentan como decisiones ya tomadas.
