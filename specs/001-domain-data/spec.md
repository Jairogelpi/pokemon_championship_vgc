# SPEC-001 — Domain + Champions data

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S01, REQ-S02, REQ-S03, REQ-S04, REQ-S05, REQ-S06, REQ-S16, REQ-S60. Dependencias: ninguna.

## Objetivo y entrega

Contratos TS/Zod de dominio, ruleset/snapshots y adaptadores auditados. Scaffold del monorepo con herramientas reales.

## Comportamientos que deben conservarse

- REQ-S01 (original §1): Las tres capas tienen contratos separados y el LLM no sustituye cálculos o simulador.
- REQ-S02 (original §2): Cada upstream tiene evaluación de licencia, versión, capacidades y un adaptador desacoplado.
- REQ-S03 (original §3): El scaffold representa apps, packages, tests, scripts, data, docs y upstream previstos sin dependencias circulares.
- REQ-S04 (original §4): El stack configurado respeta TS/Node/React/Next/SQLite/Zod/Vitest y proveedor LLM intercambiable.
- REQ-S05 (original §5): BattleState valida ID, formato, turno, fase, lados, campo, historial, beliefs y metadata.
- REQ-S06 (original §6): PokemonState representa identidad, nivel, HP, status, SP, naturaleza, habilidad, objeto, moves, boosts, Mega, volátiles y revelaciones; no Tera.
- REQ-S16 (original §16): Campo representa weather/terrain, TR, Tailwind por lado y otros efectos con duración.
- REQ-S60 (original §60): Las diez exclusiones V2+ permanecen fuera de V1.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Equipo incompleto, species desconocida, reglas no soportadas, input inválido y upstream no disponible.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-001-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then contrato serializa/deserializa sin pérdida y el adaptador normaliza formatos sin imports upstream en domain.

AC-001-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-001-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Fixtures sintéticos de tipos sin afirmar legalidad real; fixture de fuente auditada para adaptación.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.

## Cobertura detallada obligatoria

Antes de READY y de VERIFIED, revisar [DETAILED_COVERAGE](../../docs/quality/DETAILED_COVERAGE.md): §1 (REQ-S01-xx), §2 (REQ-S02-xx), §3 (REQ-S03-xx), §4 (REQ-S04-xx), §5 (REQ-S05-xx), §6 (REQ-S06-xx), §16 (REQ-S16-xx), §60 (REQ-S60-xx). Asignar todos los subrequisitos y miembros de sus enumeraciones a aceptación/tests; no basta con los tres criterios iniciales resumidos. La fuente completa sigue siendo referencia para ejemplos y casos límite.

## Detalle de contratos revisado

AC-001-04: FieldState admite exactamente las variantes originales de weather (NONE/SUN/RAIN/SAND/SNOW) y terrain (NONE/PSYCHIC/GRASSY/ELECTRIC/MISTY), más sus contadores especificados; casos inválidos se rechazan. Los opcionales de PokemonState no permiten inferir información propia requerida.
