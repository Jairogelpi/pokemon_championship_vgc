# Modelo de dominio

Base: original §§5–8, 11, 16, 33–34, 44–47, 56. Los tipos originales son pseudocódigo incompleto; SPEC-001 los convierte en contratos validados.

| Agregado / valor | Campos y restricciones |
|---|---|
| RulesetRef | format, season/regulation, version, sourceRefs; compatibilidad explícita |
| StoredTeam | id, name, seis miembros exactos, rulesetRef; errores por información requerida ausente |
| PokemonState | instanceId, species/form, level, HP, status, SP, nature, ability, item, moves, boosts, mega, volatile, revealed; Tera excluida |
| SideState | roster seleccionado, dos slots activos o vacantes tras KO, bench, restricciones por lado |
| OpponentSideState | seis especies del preview, activos/reservas conocidos y no revelados; sin inventar pick-4 oculto |
| BattleState | battleId, formato, turno, phase original, lados, field, history, beliefs, metadata |
| FieldState | weather/terrain con duración, TR, Tailwind por lado, otherEffects; efectos permanentes distinguidos de contador |
| ObservedValue | valor exacto/intervalo/desconocido, unidad, evento origen; HP rival porcentual puede ser intervalo |
| OpponentBeliefState | conjuntos candidatos con pesos, evidencia y origen; residual OTHER/UNKNOWN cuando corresponde |
| BattleEvent | id, battleId, sequence, schemaVersion, tipo, payload, origen, confirmación; aplicado una sola vez |
| ActionPair | dos acciones compatibles o slots ausentes legales; actor instanceId, move/target o reserva, megaBeforeAttack |
| DamageResult | min/max, %, rolls, KO 1/2 hits, modifiers, assumptions, verification status, references |
| SpeedOrderResult | first/second/tie y reasons; contexto prioridad/field/ruleset |
| Recommendation | línea, alternativas, confianza, riesgos, supuestos, cálculos, respuestas probables, referencias |
| StrategicClaim | texto, KNOWN/INFERRED/UNKNOWN, provenance y referenceId verificable |
| RecommendationTrace | estado/versiones, candidatos, ramas, pruning, cálculos, scores, selección, input/output LLM saneados |

## Estados transitorios

Mantener las fases originales TEAM_PREVIEW, TURN_SELECTION, TURN_RESOLUTION, BATTLE_END. Los reemplazos obligatorios se representarán con un subestado/solicitud explícito o extensión documentada en SPEC-006; no permitir que una fase de selección implique siempre dos activos vivos.

## Acciones y eventos

Mega no consume una tercera acción: es una transformación asociada a una acción válida según ruleset. La forma `MegaAction` del original se normaliza sin perder la intención. Targets modelan Pokémon, lado, campo o self según move; no forzar todos a single-target.

Tipos mínimos de evento: MOVE_USED, DAMAGE, HEAL, SWITCH, FAINT, MEGA, ABILITY_REVEALED, ITEM_REVEALED, STATUS, WEATHER, TERRAIN, TRICK_ROOM, TAILWIND. Inicio, avance de turno y correcciones/undo necesitan eventos de control adicionales documentados en SPEC-005. Protect y boosts deben quedar representados mediante payloads tipados o tipos adicionales, no texto libre.

## Persistencia y revisiones

Cada estado tiene revision monotónica; comandos apuntan a expectedRevision. Recomendación referencia revisión y hashes de reglas/datos/meta/motores. Branches simuladas nunca se guardan como observaciones. Un evento contiene evidencia, no certezas inferidas. Beliefs se recalculan con algoritmo y priors fijados para replay reproducible.
