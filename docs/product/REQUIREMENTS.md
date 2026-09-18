# Requisitos V1

Estado: BASELINE documental derivada; implementación PENDING. Cada `REQ-Sxx` corresponde exactamente a una sección original. Son requisitos compuestos: sus listas y subcasos íntegros siguen en la fuente. La aceptación resumida aquí no elimina esos subcasos. Las specs los descomponen antes de implementar.

Las discrepancias entre intención y ejemplos se registran en [preguntas abiertas](../planning/OPEN_QUESTIONS.md). La [trazabilidad](../quality/TRACEABILITY.md) asigna cada sección a una fase y evidencia pendiente. El [desglose detallado](../quality/DETAILED_COVERAGE.md) explicita los subrequisitos que cada fase debe asignar a aceptación/tests; forma parte del gate de cierre.

## REQ-S00 — Objetivo

Fuente: [original §0](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-016.

Aceptación: El recorrido equipo→preview→batalla→recomendación cubre las 20 capacidades del objetivo.

## REQ-S01 — Principio fundamental

Fuente: [original §1](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-001.

Aceptación: Las tres capas tienen contratos separados y el LLM no sustituye cálculos o simulador.

## REQ-S02 — Repositorios upstream

Fuente: [original §2](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-001.

Aceptación: Cada upstream tiene evaluación de licencia, versión, capacidades y un adaptador desacoplado.

## REQ-S03 — Monorepo

Fuente: [original §3](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-001.

Aceptación: El scaffold representa apps, packages, tests, scripts, data, docs y upstream previstos sin dependencias circulares.

## REQ-S04 — Stack

Fuente: [original §4](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-001.

Aceptación: El stack configurado respeta TS/Node/React/Next/SQLite/Zod/Vitest y proveedor LLM intercambiable.

## REQ-S05 — Modelo central

Fuente: [original §5](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-001.

Aceptación: BattleState valida ID, formato, turno, fase, lados, campo, historial, beliefs y metadata.

## REQ-S06 — Pokémon State

Fuente: [original §6](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-001.

Aceptación: PokemonState representa identidad, nivel, HP, status, SP, naturaleza, habilidad, objeto, moves, boosts, Mega, volátiles y revelaciones; no Tera.

## REQ-S07 — Equipo del usuario

Fuente: [original §7](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-002.

Aceptación: Se almacena equipo exacto de seis con forma, objeto, habilidad, naturaleza, SP, moves y stats sin inferir faltantes.

## REQ-S08 — Rival

Fuente: [original §8](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-005.

Aceptación: El rival mantiene observaciones separadas de posibles sets/items/abilities/moves/SP/Megas.

## REQ-S09 — Belief Engine

Fuente: [original §9](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-009.

Aceptación: Priors y evidencia actualizan pesos normalizados; contradicciones se registran y nunca rellenan certezas falsas.

## REQ-S10 — Ejemplo de inferencia

Fuente: [original §10](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-009.

Aceptación: El ejemplo de Protect se conserva y se contrasta antes de descartar hipótesis Choice; Q-003 evita codificar una inferencia inválida.

## REQ-S11 — Meta Engine

Fuente: [original §11](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-008.

Aceptación: MetaEngine expone usage, moves, items, abilities, partners, leads, sets y arquetipos con snapshot identificado.

## REQ-S12 — Archetype Detector

Fuente: [original §12](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-008.

Aceptación: Arquetipos devuelven enablers, abusers y confidence etiquetada como score interno.

## REQ-S13 — Damage Engine

Fuente: [original §13](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-003.

Aceptación: DamageResult contiene rango, porcentajes, rolls, KO 1/2 hits, modificadores y supuestos.

## REQ-S14 — Dual validation

Fuente: [original §14](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-003.

Aceptación: Casos compatibles se comparan con NCP; coincidencia marca validación, divergencia registra discrepancy visible.

## REQ-S15 — Speed Engine

Fuente: [original §15](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-004.

Aceptación: Speed contempla naturaleza, SP, boosts, paralysis, Tailwind, TR, Scarf, abilities, weather, prioridad y campo; devuelve ties y razones.

## REQ-S16 — Field State

Fuente: [original §16](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-001.

Aceptación: Campo representa weather/terrain, TR, Tailwind por lado y otros efectos con duración.

## REQ-S17 — Turn Engine

Fuente: [original §17](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-006.

Aceptación: Resolver recibe estado y acciones de ambos lados y devuelve outcome sin elegir estrategia.

## REQ-S18 — Action Generator

Fuente: [original §18](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-007.

Aceptación: Generador combina acciones de ambos slots: ataques/objetivos, Protect, switches y Mega con ataque.

## REQ-S19 — Legalidad

Fuente: [original §19](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-007.

Aceptación: Legalidad verifica vivo, moves, targets, switches, colisiones, Mega, Fake Out, locks, Taunt, Encore, Disable y status.

## REQ-S20 — Mega constraint

Fuente: [original §20](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-007.

Aceptación: Preview aplica la restricción Mega del ruleset activo sin asumir prohibición universal de dos piedras.

## REQ-S21 — Turn resolution

Fuente: [original §21](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-006.

Aceptación: Resolver cubre las 15 responsabilidades del pipeline; seed e input iguales producen resultado idéntico.

## REQ-S22 — RNG

Fuente: [original §22](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-006.

Aceptación: RNG inyectado; V1 evalúa daño esperado y probabilidades KO. Conservar soporte de EXPECTED, WORST_CASE y MONTE_CARLO en simulación/búsqueda (SPEC-011/012), sin posponer modos ni fallback silencioso.

## REQ-S23 — Protect

Fuente: [original §23](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-006.

Aceptación: Protect cubre protección, excepciones, spread y cadena consecutiva con probabilidad según ruleset.

## REQ-S24 — Fake Out

Fuente: [original §24](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-006.

Aceptación: Fake Out comprueba entrada, prioridad, terreno, abilities, inmunidades y Protect con condiciones explícitas.

## REQ-S25 — Trick Room

Fuente: [original §25](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-004.

Aceptación: TR modifica comparator dentro de prioridad, no stats; ties siguen representados.

## REQ-S26 — Tailwind

Fuente: [original §26](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-004.

Aceptación: Tailwind afecta cálculo contextual, nunca stats base persistentes.

## REQ-S27 — Switch Engine

Fuente: [original §27](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-006.

Aceptación: Switch procesa hazards si legales, entry abilities, clima/terreno, elegibilidad Fake Out y limpieza de volátiles.

## REQ-S28 — Simulator

Fuente: [original §28](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-011.

Aceptación: Simulador explora pares propios/rivales y sets ocultos con pruning trazable.

## REQ-S29 — Opponent Action Model

Fuente: [original §29](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-011.

Aceptación: Modelo rival genera acciones legales, puntúa plausibilidad y permite top-K configurable (ejemplo K=8).

## REQ-S30 — Search Engine

Fuente: [original §30](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-012.

Aceptación: Búsqueda expectiminimax limitada soporta profundidad por defecto 2 y opcional 3 con semántica ply definida.

## REQ-S31 — Evaluación del estado

Fuente: [original §31](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-012.

Aceptación: Evaluador incluye material, posición, speed, presión, defensa, campo, setup, información y penalizaciones de riesgo.

## REQ-S32 — Material score

Fuente: [original §32](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-012.

Aceptación: Valor de preservar un Pokémon depende de amenazas y condiciones de victoria, no solo HP.

## REQ-S33 — Risk metrics

Fuente: [original §33](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-012.

Aceptación: Líneas exponen expectedValue, worst/bestCase, variance, koRisk, doubleKOProbability y posición posterior.

## REQ-S34 — Recommendation Engine

Fuente: [original §34](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-013.

Aceptación: Recomendación incluye línea principal, alternativas, confianza, riesgos, supuestos, cálculos y respuestas plausibles.

## REQ-S35 — Preview Solver

Fuente: [original §35](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-010.

Aceptación: Preview enumera 15 pick-4 y seis leads por selección antes de filtros; evalúa matchups y planes.

## REQ-S36 — Preview output

Fuente: [original §36](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-010.

Aceptación: Salida distingue selección, lead, back, modos rivales y plan apoyado en evidencia.

## REQ-S37 — LLM Tool Layer

Fuente: [original §37](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-014.

Aceptación: Herramientas LLM cubren los diez nombres del original y no dan acceso directo de escritura al estado.

## REQ-S38 — LLM System Contract

Fuente: [original §38](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-014.

Aceptación: Contrato LLM obliga a herramientas, KNOWN/INFERRED/UNKNOWN y evidencia; no inventa datos o reglas.

## REQ-S39 — Anti-hallucination

Fuente: [original §39](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-014.

Aceptación: Cada claim tiene provenance; afirmaciones sin respaldo no aparecen como hechos.

## REQ-S40 — Battle Copilot UI

Fuente: [original §40](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-015.

Aceptación: UI de batalla muestra turno/campo/HP/reservas/acción/riesgo y permite simulación y alternativas.

## REQ-S41 — Team Preview UI

Fuente: [original §41](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-015.

Aceptación: UI preview recibe seis propios/seis rivales y presenta arquetipos/Megas/lead/back/amenazas/win conditions.

## REQ-S42 — Battle input V1

Fuente: [original §42](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-015.

Aceptación: Entrada manual soporta move, target, HP, switch, Mega y Protect de forma rápida.

## REQ-S43 — Quick Input

Fuente: [original §43](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-005.

Aceptación: Parser textual genera eventos propuestos y requiere confirmación antes de persistir.

## REQ-S44 — Event sourcing

Fuente: [original §44](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-005.

Aceptación: Eventos de los 13 tipos listados reconstruyen estado y soportan undo sin edición arbitraria.

## REQ-S45 — Persistence

Fuente: [original §45](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-005.

Aceptación: SQLite conserva teams, battles, battle_events, meta_snapshots, pokemon_sets, calculations y recommendations.

## REQ-S46 — Replay

Fuente: [original §46](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-016.

Aceptación: Replay reconstruye batalla y analiza decisiones, alternativas, predicciones, sets y errores.

## REQ-S47 — Feedback loop

Fuente: [original §47](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-009.

Aceptación: Feedback local evalúa beliefs sin actualizar automáticamente el meta global con una batalla.

## REQ-S48 — API

Fuente: [original §48](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-016.

Aceptación: Los once endpoints originales tienen entradas, salidas, errores y pruebas de contrato.

## REQ-S49 — `/preview/analyze`

Fuente: [original §49](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-010.

Aceptación: Preview acepta equipo propio persistido y seis rivales y devuelve todos los campos del original.

## REQ-S50 — `/recommend`

Fuente: [original §50](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-013.

Aceptación: Recommend devuelve acciones/objetivos, score/risk/alternatives/explanation/evidence.

## REQ-S51 — Performance target

Fuente: [original §51](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-013.

Aceptación: Benchmarks verifican preview<3s, recomendación<2s sin LLM/<5s con LLM y daño típico<100ms bajo condiciones declaradas.

## REQ-S52 — Cache

Fuente: [original §52](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-013.

Aceptación: Cache cubre daño/speed/meta/dex e invalida ante cambios de estado/campo/boosts/ability/item/Mega/spread y versiones.

## REQ-S53 — Testing strategy

Fuente: [original §53](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-016.

Aceptación: Tests unitarios, integración de turno y golden independientes cubren motores.

## REQ-S54 — Golden tests críticos

Fuente: [original §54](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-006.

Aceptación: Golden incluye TR, Psychic Terrain, cambio a Grassy, Intimidate, Protect, Tailwind y Mega con precondiciones.

## REQ-S55 — Damage validation suite

Fuente: [original §55](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-003.

Aceptación: Dataset golden de daño compara NCP, Smogon adaptado y referencia esperada; tolerancia cero determinista.

## REQ-S56 — Observability

Fuente: [original §56](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-013.

Aceptación: Trace registra estado, candidatos, ramas, cálculos, pruning, scores, selección y entrada/salida LLM saneada.

## REQ-S57 — Failure modes

Fuente: [original §57](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-013.

Aceptación: Fallbacks muestran meta stale, cálculo no verificado, incertidumbre y recomendación sin LLM.

## REQ-S58 — Orden de implementación

Fuente: [original §58](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-016.

Aceptación: Las 16 fases se conservan con dependencias y criterios de salida explícitos.

## REQ-S59 — V1 Definition of Done

Fuente: [original §59](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-016.

Aceptación: Los 34 criterios finales tienen prueba/evidencia y no se aprueban solo por disponer de UI.

## REQ-S60 — NO entra en V1

Fuente: [original §60](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-001.

Aceptación: Las diez exclusiones V2+ permanecen fuera de V1.

## REQ-S61 — Resultado final V1

Fuente: [original §61](../source/V1_SPEC_ORIGINAL.md). Responsable: SPEC-016.

Aceptación: El flujo end-to-end conserva estado, belief, simulación y búsqueda y justifica decisiones con evidencia.
