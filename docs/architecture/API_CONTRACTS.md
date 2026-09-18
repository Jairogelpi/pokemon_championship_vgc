# Contratos API y herramientas

Estado: contrato de diseño v0.1, **no endpoints implementados**. Conserva las once rutas del original §§48–50; nuevas operaciones de undo/parser/replay se indican como ampliaciones necesarias. SPEC-001 fija tipos base; cada fase propietaria añade esquemas Zod y tests. Antes de implementar un endpoint, concretar sus campos anidados y casos inválidos; esta tabla no reemplaza esos esquemas.

## Envelope y reglas comunes

Respuesta de éxito: `{data, meta:{requestId, schemaVersion, rulesetVersion?, dexSnapshotId?, metaSnapshotId?, battleRevision?, warnings[]}}`.
Error: `{error:{code,message,details?,retryable},meta:{requestId,schemaVersion}}`.
HTTP 400 payload inválido, 404 recurso ausente, 409 revisión/idempotencia en conflicto, 422 equipo/acción ilegal o mecánica no soportada, 503 dependencia obligatoria no disponible. Nunca retornar HTTP 200 con una operación inexistente o sin efecto.

IDs opacos; especies canónicas o nombres resueltos sin ambigüedad. Timestamps ISO UTC. Mutaciones llevan `commandId`; batch de eventos lleva `expectedRevision` y confirmación explícita. Repetición idéntica de commandId devuelve resultado original; payload diferente con mismo ID devuelve conflicto. Lecturas/cálculos no modifican estado real.

| Ruta original | Entrada | data de salida | Dueño / fallos específicos |
|---|---|---|---|
| POST /preview/analyze | ourTeamId, opponent[6]; config opcional | archetypes, megaCandidates, recommendedSelection[4], lead[2], back[2], threats, plan, evidence | SPEC-010; duplicados/ilegalidad según ruleset, snapshot incompatible |
| POST /battles | commandId, ourTeamId, opponent[6], selection[4], lead[2], rulesetRef | battleId, revision, BattleState | SPEC-005; selección/lead ilegal |
| GET /battles/:id | id; revision opcional | BattleState, revision y snapshot refs | SPEC-005; revisión desconocida |
| POST /battles/:id/events | commandId, expectedRevision, confirmed, events[] | acceptedEventIds, revision, BattleState | SPEC-005; batch atómico, no aplicar parcialmente |
| POST /battles/:id/recommend | revision, searchConfig?, explanationProvider? | actions, score, risk, alternatives, explanation?, evidence, Recommendation, traceId | SPEC-013; revisión obsoleta, sin acciones; explanation opcional por fallo LLM |
| POST /battles/:id/simulate | revision, playerActions, opponentActions, hiddenSetHypotheses, rngMode, seed | outcomes, probabilities, assumptions, traceId | SPEC-011; acciones incompatibles, modo no soportado; no escribir eventos reales |
| POST /damage | attacker, defender, move, field, boosts, spreadContext, rulesetRef | DamageResult, validated/status, discrepancyId? | SPEC-003; supuestos insuficientes, incompatibilidad de motores |
| POST /speed | combatants, field, priorities, rulesetRef | SpeedOrderResult y valores calculados | SPEC-004; empate no resuelto artificialmente |
| GET /meta/:pokemon | canonical species; snapshotId o season/formato | usage/moves/items/abilities/partners/leads/sets, snapshot | SPEC-008; stale/ausente explícito |
| GET /teams | filtros/paginación opcionales | teams[] | SPEC-002; no rellenar equipo ficticio |
| POST /teams | commandId, name, pokemon[6], rulesetRef | StoredTeam, validation evidence | SPEC-002; requerido incompleto/ilegal |

Los campos `Recommendation` amplían la respuesta sin perder `actions/score/risk/alternatives/explanation/evidence` del original. Una única representación canónica de acción se mapea a ambas vistas; evitar listas divergentes.

## Operaciones derivadas a concretar en sus specs

| Operación propuesta | Contrato mínimo |
|---|---|
| POST /battles/:id/observations/parse | Texto + revision → draftId + eventos propuestos + ambigüedades; cero mutaciones de batalla |
| POST /battles/:id/undo | commandId + expectedRevision + targetEvent/batch → nueva revisión y estado reconstruido; preservar auditoría |
| GET /battles/:id/replay | Eventos efectivos, estados y refs de versiones; no recalcular con versiones nuevas de forma invisible |
| POST /battles/:id/feedback | Hechos confirmados + origen → observaciones locales; no modificar meta global |
| GET /recommendations/:id/trace | Trace saneada; excluir secretos de proveedores |

## Herramientas del LLM (original §37)

| Herramienta | Acceso / salida |
|---|---|
| get_battle_state | Lectura por battleId/revision |
| get_our_team | Equipo exacto almacenado |
| get_opponent_beliefs | Hipótesis + pesos + evidencia |
| get_meta | Snapshot y estado freshness |
| calculate_damage | DamageResult y verification |
| compare_speed | Orden, empate y razones |
| get_legal_actions | Acciones compatibles con estado/reglas |
| simulate_line | Outcomes hipotéticos aislados |
| search_best_lines | Líneas calculadas, riesgos y profundidad |
| record_observation | Solo propone draft; confirmación del usuario pasa por API de eventos |

Schemas de herramientas prohíben ejecución arbitraria y acceso directo SQLite. El frontend confirma los eventos, no un flag inventado por el LLM. Claims aceptan OBSERVED, DEX, META, CALCULATOR, SIMULATION, INFERENCE; SPEED_CALCULATOR se normaliza a CALCULATOR con subtype=speed.

## Casos de contrato obligatorios

Batch inválido no escribe nada; reintento no duplica efectos; revisión vieja no sobrescribe; parser sin confirmar no modifica; simulación no contamina; recomendación tiene revision; error LLM conserva acciones calculadas; species desconocida no se corrige por conjetura; endpoint pendiente devuelve no disponible explícito.
