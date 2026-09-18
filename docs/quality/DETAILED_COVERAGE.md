# Cobertura detallada de la spec inicial

Revisión: 2026-09-18. **177 comprobaciones documentales** agrupadas por las 62 secciones de la fuente. Son subrequisitos derivados, no pruebas ejecutadas ni una medida matemática de completitud semántica.

La [fuente original](../source/V1_SPEC_ORIGINAL.md) permanece íntegra y normativa junto a las decisiones explícitas. Esta lista hace visibles detalles que estaban demasiado resumidos. Los ejemplos, enumeraciones y pseudocódigo originales siguen disponibles allí. [Informe de auditoría](SPEC_COVERAGE_AUDIT.md).

## Regla de cierre

Al activar una fase, asignar los IDs de sus comprobaciones a tareas y casos de aceptación/tests. Antes de VERIFIED, el reviewer debe comprobar **cada comprobación y cada miembro de sus enumeraciones**, registrar evidencia o un bloqueo y contrastar la sección original completa. No basta con marcar que el título REQ-Sxx está cubierto. No completar casillas porque exista documentación.

Las casillas siguientes permanecen sin marcar hasta disponer de evidencia del producto. Un ejemplo dudoso exige resolución documentada, no implementación literal ni eliminación de la capacidad. Los 34 criterios finales se conservan separadamente en [V1_ACCEPTANCE](V1_ACCEPTANCE.md).

## REQ-S00 — Objetivo

Fuente: §0. Propietario principal: [spec](../../specs/016-replay-debug/spec.md).

- [ ] REQ-S00-01: Guardar el equipo exacto del usuario y recibir los seis Pokémon rivales del Team Preview.
- [ ] REQ-S00-02: Consultar automáticamente Pokédex Champions, legalidad, estadísticas, Mega Evoluciones, movimientos, habilidades, objetos, Stat Points y meta actual.
- [ ] REQ-S00-03: Inferir sets rivales y actualizar automáticamente las hipótesis con nueva información revelada.
- [ ] REQ-S00-04: Detectar Trick Room, Tailwind, Rain, Sun, Sand, Psychic Terrain, Grassy Terrain, setup, balance e hyper offense; permitir ampliar arquetipos.
- [ ] REQ-S00-05: Elegir los mejores cuatro de seis y lead/backline; mantener el estado completo de batalla 2v2.
- [ ] REQ-S00-06: Calcular daño y orden de velocidad, generar todas las acciones legales y modelar respuestas plausibles del rival.
- [ ] REQ-S00-07: Simular uno o varios turnos, mantener incertidumbre oculta y evaluar riesgo/recompensa por línea.
- [ ] REQ-S00-08: Recomendar movimientos, objetivos, Protect, switches, Mega, double target, setup, control de velocidad y posicionamiento.
- [ ] REQ-S00-09: Usar LLM para interpretar resultados calculados y explicar; nunca para inventar daño, velocidad, sets o reglas.

## REQ-S01 — Principio fundamental

Fuente: §1. Propietario principal: [spec](../../specs/001-domain-data/spec.md).

- [ ] REQ-S01-01: Mantener la secuencia de responsabilidad DATA → RULE ENGINE → CALCULATORS → SIMULATOR → SEARCH → LLM → USER.
- [ ] REQ-S01-02: Capa determinista: Battle State, reglas Champions, daño, speed, prioridad, acciones legales, efectos y resolución del turno.
- [ ] REQ-S01-03: Capa probabilística: sets, movimientos ocultos, Mega/items posibles, leads/switches probables y arquetipo.
- [ ] REQ-S01-04: Capa de razonamiento: interpretación estratégica, análisis de riesgo y explicación usando exclusivamente datos de las capas anteriores.

## REQ-S02 — Repositorios upstream

Fuente: §2. Propietario principal: [spec](../../specs/001-domain-data/spec.md).

- [ ] REQ-S02-01: pmwl0128/pokemon_champion_agent: evaluar/reutilizar Dex, SP, legality, Mega rules, meta snapshots, team analysis, NCP calculator, speed y conocimiento Champions. No duplicar datasets consumibles.
- [ ] REQ-S02-02: Adapter champions_agent convierte formatos externos a modelos propios; dominio no depende de estructuras upstream.
- [ ] REQ-S02-03: SebNotFound/champions-calc: evaluar/reutilizar adaptaciones Champions, integración @smogon/calc, conversión SP, ideas de damage y lógica 2v2; adapter champions_calc.
- [ ] REQ-S02-04: @smogon/calc: motor matemático solo cuando soporte mecánica; no editar paquete. Wrapper con SmogonCalcAdapter, ChampionsRulesPatch y NCPValidator.
- [ ] REQ-S02-05: huydamm/PokemonVGC-Calculator: evaluar representación de equipo, conditions, set inference, battle state, soporte Champions, damage pipeline e ideas UI/overlay; no importar arquitectura acoplada completa.
- [ ] REQ-S02-06: MSS23/vgc-mcp: evaluar lifecycle, start_battle, record_turn, suggest_move, estado, tools, patrones de test y validación de daño. Registrar límites y licencias antes de reutilizar.

## REQ-S03 — Monorepo

Fuente: §3. Propietario principal: [spec](../../specs/001-domain-data/spec.md).

- [ ] REQ-S03-01: Apps previstas: apps/web y apps/api.
- [ ] REQ-S03-02: Packages previstos: domain, champions-data, meta-engine, damage-engine, speed-engine, battle-engine, belief-engine, action-generator, simulator, search-engine, preview-solver, copilot, llm, persistence y shared.
- [ ] REQ-S03-03: Tests previstos: unit, integration, regression, battle-scenarios y golden; directorios scripts, data, docs y upstream. Crear contenido real progresivamente, sin dar por implementado un directorio vacío.

## REQ-S04 — Stack

Fuente: §4. Propietario principal: [spec](../../specs/001-domain-data/spec.md).

- [ ] REQ-S04-01: Frontend Next.js/React/TypeScript y backend Node.js/TypeScript; conservar aprovechamiento del ecosistema JS/TS de @smogon/calc.
- [ ] REQ-S04-02: Persistencia SQLite V1; elegir Drizzle o Prisma; Zod en validación y Vitest para pruebas.
- [ ] REQ-S04-03: Abstracción de proveedor LLM con compatibilidad OpenAI, Anthropic, Gemini y endpoint local OpenAI-compatible.

## REQ-S05 — Modelo central

Fuente: §5. Propietario principal: [spec](../../specs/001-domain-data/spec.md).

- [ ] REQ-S05-01: BattleState: battleId, format="champions-doubles", turn, player:SideState, opponent:OpponentSideState, field:FieldState, history:TurnRecord[], beliefs:OpponentBeliefState y metadata:BattleMetadata.
- [ ] REQ-S05-02: Conservar TEAM_PREVIEW, TURN_SELECTION, TURN_RESOLUTION y BATTLE_END; representar reemplazos sin borrar estas fases.
- [ ] REQ-S05-03: BattleState como única verdad operativa; su reconstrucción durable procede de eventos (§44), no de otro estado paralelo editable.

## REQ-S06 — Pokémon State

Fuente: §6. Propietario principal: [spec](../../specs/001-domain-data/spec.md).

- [ ] REQ-S06-01: PokemonState: instanceId, species, form opcional, level, hp.current/hp.max y status.
- [ ] REQ-S06-02: Conservar statPoints, nature, ability, item, moves:MoveState[], boosts:StatBoosts y revealed:RevealedInformation.
- [ ] REQ-S06-03: Conservar mega.capable, mega.stone opcional, mega.evolved y volatile:VolatileState; tera?:never. Los opcionales propios requeridos por el equipo no se rellenan por inferencia.

## REQ-S07 — Equipo del usuario

Fuente: §7. Propietario principal: [spec](../../specs/002-team-store/spec.md).

- [ ] REQ-S07-01: StoredTeam: id, name, pokemon[6] y rules. Información propia exacta/perfecta.
- [ ] REQ-S07-02: Cada miembro: especie, forma, Mega Stone/objeto, habilidad, naturaleza, SP, movimientos y estadísticas finales.
- [ ] REQ-S07-03: Nunca inferir datos propios. El ejemplo Garchomp/Modest/Garchompite Z y sus moves se conserva en la fuente; su legalidad debe verificarse, no usarse como equipo real del usuario.

## REQ-S08 — Rival

Fuente: §8. Propietario principal: [spec](../../specs/005-battle-events/spec.md).

- [ ] REQ-S08-01: Rival observado: species, hp, status, moves[], ability?, item?, mega? y statsEvidence[].
- [ ] REQ-S08-02: Rival inferido: possibleSets[], possibleItems[], possibleAbilities[], possibleMoves[], possibleSP[] y possibleMegas[]; mantener incertidumbre y separación de observed/belief.

## REQ-S09 — Belief Engine

Fuente: §9. Propietario principal: [spec](../../specs/009-belief-engine/spec.md).

- [ ] REQ-S09-01: Inferencia bayesiana aproximada sin ML entrenado: prior de meta usage, P(set|evidence) proporcional a P(evidence|set)×P(set).
- [ ] REQ-S09-02: Evidencia: movimiento revelado, habilidad, objeto y Mega.
- [ ] REQ-S09-03: Evidencia: daño causado, daño recibido y orden de velocidad.
- [ ] REQ-S09-04: Evidencia: Protect, Fake Out, weather, terrain, inmunidades, stat boosts y switch behaviour.
- [ ] REQ-S09-05: Cada familia de evidencia tiene un caso de actualización o de no-conclusión justificada; no ignorar familias por no aparecer en un resumen.

## REQ-S10 — Ejemplo de inferencia

Fuente: §10. Propietario principal: [spec](../../specs/009-belief-engine/spec.md).

- [ ] REQ-S10-01: Conservar el ejemplo de prior/posterior Staraptor, renormalización tras observación y filtrado posterior por speed.
- [ ] REQ-S10-02: Las cifras de ejemplo y la eliminación Choice tras Protect son ilustrativas pendientes de Q-003; no convertirlas en oráculo mecánico ni eliminar la capacidad de inferir items con evidencia válida.

## REQ-S11 — Meta Engine

Fuente: §11. Propietario principal: [spec](../../specs/008-meta-engine/spec.md).

- [ ] REQ-S11-01: MetaEngine: getPokemonUsage, getMoveUsage, getItemUsage, getAbilityUsage, getPartnerUsage, getLeadUsage, getCommonSets y getArchetypes.
- [ ] REQ-S11-02: MetaSnapshot: format, season, generatedAt, source, sampleSize? y data.
- [ ] REQ-S11-03: Toda recomendación identifica el snapshot utilizado; no reutilizar usage de otro formato/temporada sin señalar incompatibilidad.

## REQ-S12 — Archetype Detector

Fuente: §12. Propietario principal: [spec](../../specs/008-meta-engine/spec.md).

- [ ] REQ-S12-01: Entrada de seis rivales; salida ArchetypeHypothesis[] con type, confidence, enablers[] y abusers[].
- [ ] REQ-S12-02: Soportar varias hipótesis a la vez, como TR y Sand en el ejemplo. Confidence es score interno, no probabilidad científica.

## REQ-S13 — Damage Engine

Fuente: §13. Propietario principal: [spec](../../specs/003-damage-engine/spec.md).

- [ ] REQ-S13-01: calculateDamage(input):DamageResult, no solo etiqueta super effective.
- [ ] REQ-S13-02: DamageResult: minDamage, maxDamage, minPercent, maxPercent y rolls[].
- [ ] REQ-S13-03: Conservar koChance.oneHit, koChance.twoHit, modifiers[] y assumptions[].

## REQ-S14 — Dual validation

Fuente: §14. Propietario principal: [spec](../../specs/003-damage-engine/spec.md).

- [ ] REQ-S14-01: Para casos compatibles, comparar NCP frente a @smogon/calc con Champions patches.
- [ ] REQ-S14-02: Coincidencia verificable: validated=true. Divergencia: validated=false y CalculationDiscrepancy registrada y visible. Falta de soporte/oráculo nunca equivale a coincidencia.

## REQ-S15 — Speed Engine

Fuente: §15. Propietario principal: [spec](../../specs/004-speed-engine/spec.md).

- [ ] REQ-S15-01: Exponer calculateSpeed() y compareSpeed().
- [ ] REQ-S15-02: Soportar naturaleza, SP, boosts, paralysis, Tailwind, Trick Room, Choice Scarf, abilities, weather abilities, prioridad y field modifiers.
- [ ] REQ-S15-03: SpeedOrderResult conserva first, second, tie y reasons[].

## REQ-S16 — Field State

Fuente: §16. Propietario principal: [spec](../../specs/001-domain-data/spec.md).

- [ ] REQ-S16-01: Weather: NONE, SUN, RAIN, SAND y SNOW; terrain: NONE, PSYCHIC, GRASSY, ELECTRIC y MISTY.
- [ ] REQ-S16-02: FieldState conserva trickRoomTurns, playerTailwindTurns, opponentTailwindTurns y otherEffects[].

## REQ-S17 — Turn Engine

Fuente: §17. Propietario principal: [spec](../../specs/006-turn-resolver/spec.md).

- [ ] REQ-S17-01: Turn Engine recibe BattleState + PlayerActions + OpponentActions y devuelve TurnOutcome.
- [ ] REQ-S17-02: Es determinista con RNG controlado; ejecuta acciones, no decide estrategia.

## REQ-S18 — Action Generator

Fuente: §18. Propietario principal: [spec](../../specs/007-action-generator/spec.md).

- [ ] REQ-S18-01: Por Pokémon activo generar AttackAction, ProtectAction, SwitchAction y MegaAction; combinar ambos slots.
- [ ] REQ-S18-02: Attack conserva actor, move, target y megaBeforeAttack opcional. Normalizar Mega junto a la acción válida sin añadir un tercer movimiento al turno.

## REQ-S19 — Legalidad

Fuente: §19. Propietario principal: [spec](../../specs/007-action-generator/spec.md).

- [ ] REQ-S19-01: Validar actor vivo, movimiento disponible, target válido y switch válido.
- [ ] REQ-S19-02: Rechazar colisión de dos switches al mismo destino y restricciones Mega incumplidas.
- [ ] REQ-S19-03: Comprobar legalidad Fake Out, move locks, Taunt, Encore, Disable y status; ampliar conforme reglas soportadas, sin tratar el «etc.» como permiso para ignorarlas.

## REQ-S20 — Mega constraint

Fuente: §20. Propietario principal: [spec](../../specs/007-action-generator/spec.md).

- [ ] REQ-S20-01: PreviewSolver filtra pick-4 con Megas incompatibles cuando la regla del formato lo prohíba.
- [ ] REQ-S20-02: El ejemplo Raichu Y/Garchomp Z no implica prohibición universal de dos piedras; verificar reglas/entidades antes de usarlo como fixture.

## REQ-S21 — Turn resolution

Fuente: §21. Propietario principal: [spec](../../specs/006-turn-resolver/spec.md).

- [ ] REQ-S21-01: Cubrir collect actions, validate, determine priority y determine speed.
- [ ] REQ-S21-02: Cubrir resolve switches, resolve Mega, resolve actions y calculate damage.
- [ ] REQ-S21-03: Cubrir apply effects, resolve abilities, resolve end-of-turn y decrement field counters.
- [ ] REQ-S21-04: Cubrir process fainted Pokémon, request replacements y generate new BattleState.
- [ ] REQ-S21-05: Mismo input + RNG seed → mismo output. Son las 15 responsabilidades originales; su orden real/intercalado se contrasta en Q-004, sin omitir ninguna.

## REQ-S22 — RNG

Fuente: §22. Propietario principal: [spec](../../specs/006-turn-resolver/spec.md).

- [ ] REQ-S22-01: No basar la evaluación de búsqueda en un único roll.
- [ ] REQ-S22-02: Search Engine debe poder usar EXPECTED, WORST_CASE y MONTE_CARLO; no trasladar modos a V2 ni sustituir implementación por un enum sin autorización de alcance.
- [ ] REQ-S22-03: Camino principal V1: expected damage + KO probabilities. Debug reproducible con seeded RNG. Definir presupuesto y semántica de cada modo sin borrar capacidades.

## REQ-S23 — Protect

Fuente: §23. Propietario principal: [spec](../../specs/006-turn-resolver/spec.md).

- [ ] REQ-S23-01: Protect: protección completa, movimientos que lo atraviesan, interacciones spread y probabilidad de éxito consecutivo.
- [ ] REQ-S23-02: Conservar protectChain:number; verificar con ruleset qué efectos bloquea y qué excepciones aplica.

## REQ-S24 — Fake Out

Fuente: §24. Propietario principal: [spec](../../specs/006-turn-resolver/spec.md).

- [ ] REQ-S24-01: Fake Out: primer turno en campo, prioridad, Psychic Terrain y habilidades relevantes.
- [ ] REQ-S24-02: Fake Out: Ghost immunity cuando corresponda, flinch immunity y Protect; no concluir éxito solo porque desaparece una restricción.

## REQ-S25 — Trick Room

Fuente: §25. Propietario principal: [spec](../../specs/004-speed-engine/spec.md).

- [ ] REQ-S25-01: Trick Room no altera estadísticas: prioridad descendente y speed ascendente; normal: prioridad descendente y speed descendente.
- [ ] REQ-S25-02: La prioridad conserva precedencia sobre la inversión de speed.

## REQ-S26 — Tailwind

Fuente: §26. Propietario principal: [spec](../../specs/004-speed-engine/spec.md).

- [ ] REQ-S26-01: Tailwind se pasa contextualmente a SpeedEngine como tailwind=true o equivalente tipado.
- [ ] REQ-S26-02: No guardar permanentemente speed modificada en Pokémon.

## REQ-S27 — Switch Engine

Fuente: §27. Propietario principal: [spec](../../specs/006-turn-resolver/spec.md).

- [ ] REQ-S27-01: Switch: hazards si el contexto Champions los admite e Intimidate.
- [ ] REQ-S27-02: Switch: terrain setters, weather setters y entry abilities.
- [ ] REQ-S27-03: Switch: reset de elegibilidad Fake Out y limpieza de volátiles.

## REQ-S28 — Simulator

Fuente: §28. Propietario principal: [spec](../../specs/011-simulator/spec.md).

- [ ] REQ-S28-01: Simulador explora OurActionPair × OpponentActionPair × RelevantHiddenSets.
- [ ] REQ-S28-02: Evitar producto cartesiano completo en escenarios grandes mediante pruning trazable; conservar ramas hipotéticas aisladas.

## REQ-S29 — Opponent Action Model

Fuente: §29. Propietario principal: [spec](../../specs/011-simulator/spec.md).

- [ ] REQ-S29-01: Generar inicialmente todas las acciones rivales legales y después asignar plausibilityScore.
- [ ] REQ-S29-02: Factores explícitos: meta usage, damage, KO potential y protect.
- [ ] REQ-S29-03: Factores explícitos: setup, switch synergy, speed control y board position.
- [ ] REQ-S29-04: Descartar ramas irrelevantes; top-K configurable, K=8 es ejemplo, no restricción fija universal.

## REQ-S30 — Search Engine

Fuente: §30. Propietario principal: [spec](../../specs/012-search-engine/spec.md).

- [ ] REQ-S30-01: Expectiminimax limitado V1; 2 ply por defecto, 3 ply opcional, sin búsqueda de partida completa.
- [ ] REQ-S30-02: Definir unidad ply en Q-005 antes de implementar/medir; un resultado parcial de menor horizonte no acredita AC-V1-26.

## REQ-S31 — Evaluación del estado

Fuente: §31. Propietario principal: [spec](../../specs/012-search-engine/spec.md).

- [ ] REQ-S31-01: No evaluar únicamente HP: conservar material, boardPosition, speedControl, offensivePressure, defensivePosition, fieldControl, setup e information.
- [ ] REQ-S31-02: Conservar penalizaciones koRisk, trappedRisk y opponentPressure; cada componente identificable y comprobable por separado.

## REQ-S32 — Material score

Fuente: §32. Propietario principal: [spec](../../specs/012-search-engine/spec.md).

- [ ] REQ-S32-01: KO implica penalización grande, con escala documentada respecto a otros componentes.
- [ ] REQ-S32-02: Preservar Pokémon críticos tiene valor contextual según amenazas/win conditions; Strategy Layer puede aportar ese valor. El ejemplo Rillaboom ante Basculegion no es peso universal fijo.

## REQ-S33 — Risk metrics

Fuente: §33. Propietario principal: [spec](../../specs/012-search-engine/spec.md).

- [ ] REQ-S33-01: Cada línea expone expectedValue, worstCase, bestCase y variance.
- [ ] REQ-S33-02: Cada línea expone koRisk, doubleKOProbability y positionAfterTurn.

## REQ-S34 — Recommendation Engine

Fuente: §34. Propietario principal: [spec](../../specs/013-recommendation-engine/spec.md).

- [ ] REQ-S34-01: No devolver solo bestAction; Recommendation conserva primaryLine y alternatives[].
- [ ] REQ-S34-02: Conservar confidence, keyRisks[], assumptions[], calculations[] y opponentLikelyResponses[].

## REQ-S35 — Preview Solver

Fuente: §35. Propietario principal: [spec](../../specs/010-preview-solver/spec.md).

- [ ] REQ-S35-01: Entrada OurTeam[6] y OpponentTeam[6]; enumerar C(6,4)=15 selecciones antes de filtros Mega/legalidad.
- [ ] REQ-S35-02: Para cada pick-4 enumerar C(4,2)=6 pares de lead; tratar orden de slots adicionalmente si ruleset lo necesita.
- [ ] REQ-S35-03: Evaluar matchups, speed, coverage y defensive switching.
- [ ] REQ-S35-04: Evaluar archetypes, opponent leads, Mega choice y win conditions.

## REQ-S36 — Preview output

Fuente: §36. Propietario principal: [spec](../../specs/010-preview-solver/spec.md).

- [ ] REQ-S36-01: Salida incluye SELECT, LEAD, BACK, OPPONENT MODES y KEY PLAN, o equivalentes estructurados que la UI muestre.
- [ ] REQ-S36-02: Modos rivales pueden incluir varios arquetipos/amenazas y confianza; plan indica qué impedir, preservar y evitar. Los Pokémon/valores del ejemplo no se convierten en respuesta fija.

## REQ-S37 — LLM Tool Layer

Fuente: §37. Propietario principal: [spec](../../specs/014-llm-tools/spec.md).

- [ ] REQ-S37-01: Herramientas: get_battle_state, get_our_team, get_opponent_beliefs, get_meta y calculate_damage.
- [ ] REQ-S37-02: Herramientas: compare_speed, get_legal_actions, simulate_line, search_best_lines y record_observation.
- [ ] REQ-S37-03: LLM sin modificación directa de BattleState; record_observation propone para confirmación conforme §§43–44.

## REQ-S38 — LLM System Contract

Fuente: §38. Propietario principal: [spec](../../specs/014-llm-tools/spec.md).

- [ ] REQ-S38-01: Contrato LLM: nunca inventar damage, speed, moves, items, abilities, mechanics ni usage statistics.
- [ ] REQ-S38-02: Usar herramientas, separar KNOWN/INFERRED/UNKNOWN y apoyar recomendación en evidencia calculada u observada.

## REQ-S39 — Anti-hallucination

Fuente: §39. Propietario principal: [spec](../../specs/014-llm-tools/spec.md).

- [ ] REQ-S39-01: StrategicClaim contiene claim y provenance; sin origen no se muestra como hecho.
- [ ] REQ-S39-02: Orígenes: OBSERVED, DEX, META, CALCULATOR, SIMULATION e INFERENCE. SPEED_CALCULATOR del ejemplo se representa como CALCULATOR/subtype speed sin perder trazabilidad.

## REQ-S40 — Battle Copilot UI

Fuente: §40. Propietario principal: [spec](../../specs/015-web-ui/spec.md).

- [ ] REQ-S40-01: Battle board muestra turno y contadores de efectos como TR y terreno.
- [ ] REQ-S40-02: Muestra ambos campos activos, HP, reservas propias y reservas rivales desconocidas explícitas.
- [ ] REQ-S40-03: Muestra acciones/targets recomendados, riesgo principal y posición esperada posterior; permite SIMULATE y ALTERNATIVES.

## REQ-S41 — Team Preview UI

Fuente: §41. Propietario principal: [spec](../../specs/015-web-ui/spec.md).

- [ ] REQ-S41-01: UI preview muestra seis propios y seis rivales y acción ANALYZE PREVIEW.
- [ ] REQ-S41-02: Resultado: archetype, probable Mega(s), likely leads rivales, recommended 4, recommended lead, backline, threats y win conditions; no confundir leads rivales con nuestro lead.

## REQ-S42 — Battle input V1

Fuente: §42. Propietario principal: [spec](../../specs/015-web-ui/spec.md).

- [ ] REQ-S42-01: Entrada manual rápida V1, botones grandes; no depender de computer vision.
- [ ] REQ-S42-02: Controles Opponent used/move, Target/pokemon, HP after con slider/input, Switch, Mega y Protect.
- [ ] REQ-S42-03: Objetivo UX: registrar un turno en segundos; medir interacción y definir criterio operativo sin perder el objetivo original.

## REQ-S43 — Quick Input

Fuente: §43. Propietario principal: [spec](../../specs/005-battle-events/spec.md).

- [ ] REQ-S43-01: ObservationParser convierte comando textual abreviado a eventos estructurados; LLM puede ayudar.
- [ ] REQ-S43-02: Usuario confirma antes de alterar estado. Conservar caso con Mega, abreviatura de move, objetivo, cambio HP y Parting Shot/switch como escenario de parsing; resolver ambigüedades.

## REQ-S44 — Event sourcing

Fuente: §44. Propietario principal: [spec](../../specs/005-battle-events/spec.md).

- [ ] REQ-S44-01: Persistir BattleEvent[] y reconstruir BattleState; no permitir edición arbitraria.
- [ ] REQ-S44-02: Tipos: MOVE_USED, DAMAGE, HEAL, SWITCH, FAINT, MEGA y ABILITY_REVEALED.
- [ ] REQ-S44-03: Tipos: ITEM_REVEALED, STATUS, WEATHER, TERRAIN, TRICK_ROOM y TAILWIND.
- [ ] REQ-S44-04: UNDO debe corregir entradas erróneas; mantener auditoría/reconstrucción coherente en diseño de SPEC-005.

## REQ-S45 — Persistence

Fuente: §45. Propietario principal: [spec](../../specs/005-battle-events/spec.md).

- [ ] REQ-S45-01: SQLite conserva teams, battles, battle_events y meta_snapshots.
- [ ] REQ-S45-02: SQLite conserva pokemon_sets, calculations y recommendations; no limitar persistencia a equipos/batallas.

## REQ-S46 — Replay

Fuente: §46. Propietario principal: [spec](../../specs/016-replay-debug/spec.md).

- [ ] REQ-S46-01: Guardar cada batalla y ofrecer REPLAY ANALYSIS.
- [ ] REQ-S46-02: Identificar turnos críticos, recomendaciones tomadas y alternativa superior.
- [ ] REQ-S46-03: Identificar predicciones incorrectas, sets revelados y errores del modelo; distinguir recomendación propuesta de acción realmente tomada.

## REQ-S47 — Feedback loop

Fuente: §47. Propietario principal: [spec](../../specs/009-belief-engine/spec.md).

- [ ] REQ-S47-01: Feedback postcombate confirma hechos sobre Mega/moves/otros datos rivales para evaluar Belief Engine.
- [ ] REQ-S47-02: Guardar como local observations; no actualizar automáticamente estadísticas globales del meta con una sola partida.

## REQ-S48 — API

Fuente: §48. Propietario principal: [spec](../../specs/016-replay-debug/spec.md).

- [ ] REQ-S48-01: POST /preview/analyze; POST /battles; GET /battles/:id.
- [ ] REQ-S48-02: POST /battles/:id/events; POST /battles/:id/recommend; POST /battles/:id/simulate.
- [ ] REQ-S48-03: POST /damage; POST /speed; GET /meta/:pokemon; GET /teams; POST /teams.
- [ ] REQ-S48-04: Los once endpoints conservan función observable; contratos y errores en API_CONTRACTS, no respuestas ok sin efecto.

## REQ-S49 — `/preview/analyze`

Fuente: §49. Propietario principal: [spec](../../specs/010-preview-solver/spec.md).

- [ ] REQ-S49-01: Request preview: ourTeamId y opponent con seis Pokémon.
- [ ] REQ-S49-02: Response preview: archetypes, megaCandidates, recommendedSelection, lead, back, threats y plan.

## REQ-S50 — `/recommend`

Fuente: §50. Propietario principal: [spec](../../specs/013-recommendation-engine/spec.md).

- [ ] REQ-S50-01: Response recommend: actions[] con pokemon/actor, action y target cuando proceda.
- [ ] REQ-S50-02: Conservar score, risk, alternatives, explanation y evidence; explicación LLM puede faltar en fallo sin perder recomendación matemática (§57).

## REQ-S51 — Performance target

Fuente: §51. Propietario principal: [spec](../../specs/013-recommendation-engine/spec.md).

- [ ] REQ-S51-01: Team Preview <3 segundos.
- [ ] REQ-S51-02: Recomendación de turno <2 segundos determinista y <5 segundos con explicación LLM.
- [ ] REQ-S51-03: Cálculo de daño típico <100 ms; UI update instantánea. Q-009 concreta medición, no autoriza relajar objetivos.

## REQ-S52 — Cache

Fuente: §52. Propietario principal: [spec](../../specs/013-recommendation-engine/spec.md).

- [ ] REQ-S52-01: Cache de damage calculations, speed calculations, meta queries y dex queries.
- [ ] REQ-S52-02: Damage cache key incluye attacker state, defender state, move y field.
- [ ] REQ-S52-03: También incluye boosts, ability, item, Mega y spread context; referencias de versión añadidas para no mezclar reglas.

## REQ-S53 — Testing strategy

Fuente: §53. Propietario principal: [spec](../../specs/016-replay-debug/spec.md).

- [ ] REQ-S53-01: Unit tests: DamageEngine, SpeedEngine, ActionGenerator, TurnResolver y BeliefEngine.
- [ ] REQ-S53-02: Integration tests: full turn simulation. Golden battles: escenarios conocidos con resultado esperado.

## REQ-S54 — Golden tests críticos

Fuente: §54. Propietario principal: [spec](../../specs/006-turn-resolver/spec.md).

- [ ] REQ-S54-01: Golden TR: inversión de speed en turno correspondiente; golden Psychic Terrain/Fake Out con condiciones de elegibilidad.
- [ ] REQ-S54-02: Golden Rillaboom switch Psychic→Grassy: desaparece ese impedimento a Fake Out, manteniendo cualquier otra restricción.
- [ ] REQ-S54-03: Golden Intimidate: baja ataque físico donde corresponda; daño especial no se calcula con ese stage.
- [ ] REQ-S54-04: Golden Protect: daño cero cuando aplica; golden Tailwind: cambia orden; golden Mega: selección legal. Verificar precondiciones, sin eliminar ninguna de las siete familias.

## REQ-S55 — Damage validation suite

Fuente: §55. Propietario principal: [spec](../../specs/003-damage-engine/spec.md).

- [ ] REQ-S55-01: Crear tests/golden/damage.json con casos conocidos y referencias.
- [ ] REQ-S55-02: Comparar NCP, Smogon patched y expected reference; tolerancia 0 para reglas deterministas.

## REQ-S56 — Observability

Fuente: §56. Propietario principal: [spec](../../specs/013-recommendation-engine/spec.md).

- [ ] REQ-S56-01: Cada recomendación genera RecommendationTrace con battleState, candidateActions y opponentBranches.
- [ ] REQ-S56-02: Conservar calculations, prunedBranches, scores y selectedLine.
- [ ] REQ-S56-03: Conservar llmInput y llmOutput (saneados; ausencia explícita si no se llama LLM), para diagnosticar por qué falló.

## REQ-S57 — Failure modes

Fuente: §57. Propietario principal: [spec](../../specs/013-recommendation-engine/spec.md).

- [ ] REQ-S57-01: Meta no disponible: último snapshot y META STALE.
- [ ] REQ-S57-02: Damage Engine diverge: CALCULATION UNVERIFIED; set rival desconocido: ampliar uncertainty.
- [ ] REQ-S57-03: LLM falla: mostrar recomendación matemática sin explicación LLM; programa funcional sin LLM.

## REQ-S58 — Orden de implementación

Fuente: §58. Propietario principal: [spec](../../specs/016-replay-debug/spec.md).

- [ ] REQ-S58-01: Conservar fases 1–4: Domain+Champions data, Team Store, Damage Engine, Speed Engine.
- [ ] REQ-S58-02: Conservar fases 5–8: BattleState+Events, Turn Resolver, Action Generator, Meta Engine.
- [ ] REQ-S58-03: Conservar fases 9–12: Belief Engine, Preview Solver, Simulator, Search Engine.
- [ ] REQ-S58-04: Conservar fases 13–16: Recommendation Engine, LLM tool layer, Web UI, Replay+debugging. Dependencias permiten paralelismo seguro, sin borrar entregables.

## REQ-S59 — V1 Definition of Done

Fuente: §59. Propietario principal: [spec](../../specs/016-replay-debug/spec.md).

- [ ] REQ-S59-01: Aplicar los 34 criterios AC-V1-01…AC-V1-34 de V1_ACCEPTANCE con texto original y evidencia real.
- [ ] REQ-S59-02: La V1 no termina por tener una interfaz; no confundir cobertura documental con funcionamiento.

## REQ-S60 — NO entra en V1

Fuente: §60. Propietario principal: [spec](../../specs/001-domain-data/spec.md).

- [ ] REQ-S60-01: Excluir V1: Computer Vision automática, OCR, control automático del juego y reconocimiento desde vídeo.
- [ ] REQ-S60-02: Excluir V1: ML entrenado, self-play masivo, RL y MCTS profundo.
- [ ] REQ-S60-03: Excluir V1: cloud obligatorio y mobile app nativa. Conservar los diez puntos V2+.

## REQ-S61 — Resultado final V1

Fuente: §61. Propietario principal: [spec](../../specs/016-replay-debug/spec.md).

- [ ] REQ-S61-01: End-to-end preview: seis enemigos → meta/dex → arquetipos → Megas → pick-4 → legalidad → leads → daño/speed/matchups → selección.
- [ ] REQ-S61-02: End-to-end combate: observaciones → estado → beliefs → acciones → cálculos → ramas rivales → simulación 2v2 → búsqueda → riesgo → análisis LLM opcional → recomendación → nueva observación.
- [ ] REQ-S61-03: Justificar recomendaciones con estado, sets compatibles, meta, speed, daño y simulación; no sustituirlo por opinión conversacional.
- [ ] REQ-S61-04: No recortar BattleState, Belief Engine, simulador ni búsqueda para convertir la V1 en una demo.
