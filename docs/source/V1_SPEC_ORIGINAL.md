# Pokémon Champions Battle Copilot --- V1 Specification

## 0. Objetivo

Construir un copiloto competitivo para Pokémon Champions Doubles capaz
de:

1.  Guardar el equipo exacto del usuario.
2.  Recibir los 6 Pokémon del rival en Team Preview.
3.  Consultar automáticamente:
    -   Pokédex de Champions.
    -   legalidad.
    -   estadísticas.
    -   Mega Evoluciones.
    -   movimientos.
    -   habilidades.
    -   objetos.
    -   Stat Points.
    -   datos actuales del meta.
4.  Inferir posibles sets del rival.
5.  Detectar arquetipos:
    -   Trick Room
    -   Tailwind
    -   Rain
    -   Sun
    -   Sand
    -   Psychic Terrain
    -   Grassy Terrain
    -   setup
    -   balance
    -   hyper offense
    -   etc.
6.  Elegir los mejores 4 de nuestros 6.
7.  Elegir lead + backline.
8.  Mantener el estado completo de una batalla 2v2.
9.  Calcular daño real.
10. Calcular orden de velocidad real.
11. Generar todas las acciones legales.
12. Modelar acciones plausibles del rival.
13. Simular ramas de uno o varios turnos.
14. Mantener incertidumbre sobre información oculta.
15. Evaluar riesgo/recompensa de cada línea.
16. Usar un LLM para razonar sobre los resultados calculados.
17. Recomendar:
    -   movimientos;
    -   objetivos;
    -   Protect;
    -   switches;
    -   Mega;
    -   double target;
    -   setup;
    -   control de velocidad;
    -   posicionamiento.
18. Explicar por qué.
19. Actualizar automáticamente las hipótesis cuando el rival revele
    información.
20. Nunca permitir que el LLM invente daño, velocidades, sets o reglas.

------------------------------------------------------------------------

## 1. Principio fundamental

El LLM **NO es el simulador**.

``` text
DATA
 ↓
RULE ENGINE
 ↓
CALCULATORS
 ↓
SIMULATOR
 ↓
SEARCH
 ↓
LLM
 ↓
USER
```

Separación estricta:

### Deterministic Layer

-   Battle State
-   Champions rules
-   damage
-   speed
-   priority
-   legal actions
-   effects
-   turn resolution

### Probabilistic Layer

-   opponent sets
-   unrevealed moves
-   possible Mega
-   possible items
-   likely leads
-   likely switches
-   archetype

### Reasoning Layer

-   strategic interpretation
-   risk analysis
-   explanation

El LLM solamente trabaja con información producida por las dos capas
anteriores.

------------------------------------------------------------------------

## 2. Repositorios upstream

### 2.1 pokemon_champion_agent

Upstream: `pmwl0128/pokemon_champion_agent`

Usar para: - Champions Dex - Stat Points - legality - Mega rules - meta
snapshots - team analysis - NCP calculator - speed calculations -
Champions-specific knowledge

NO duplicar estos datasets mientras podamos consumirlos.

Crear:

``` text
src/adapters/champions_agent/
```

Responsabilidad: convertir los formatos del proyecto externo a nuestros
modelos internos.

Nunca permitir que el dominio interno dependa directamente de
estructuras del repo upstream.

### 2.2 champions-calc

Upstream: `SebNotFound/champions-calc`

Reutilizar: - Champions adaptations - `@smogon/calc` integration - SP
conversion - damage calculation ideas - 2v2 calculation logic donde sea
reutilizable

Adapter:

``` text
src/adapters/champions_calc/
```

### 2.3 @smogon/calc

Usar como motor matemático subyacente cuando la mecánica esté soportada.

Nunca modificar directamente el paquete.

Wrapper:

``` text
DamageEngine
    |
    +-- SmogonCalcAdapter
    |
    +-- ChampionsRulesPatch
    |
    +-- NCPValidator
```

### 2.4 PokemonVGC-Calculator

Upstream: `huydamm/PokemonVGC-Calculator`

Reutilizar/adaptar: - team representation - conditions - set inference -
battle-state concepts - Champions support - damage pipeline - UI/overlay
ideas

No copiar arquitectura completa si genera acoplamiento innecesario.

### 2.5 vgc-mcp

Upstream: `MSS23/vgc-mcp`

Usar como referencia/reutilización para: - battle lifecycle -
`start_battle` - `record_turn` - `suggest_move` - battle state - copilot
tools - test patterns - damage validation

------------------------------------------------------------------------

## 3. Monorepo

``` text
pokemon-champions-copilot/

apps/
    web/
    api/

packages/
    domain/
    champions-data/
    meta-engine/
    damage-engine/
    speed-engine/
    battle-engine/
    belief-engine/
    action-generator/
    simulator/
    search-engine/
    preview-solver/
    copilot/
    llm/
    persistence/
    shared/

tests/
    unit/
    integration/
    regression/
    battle-scenarios/
    golden/

scripts/
data/
docs/
upstream/
```

------------------------------------------------------------------------

## 4. Stack

Frontend: - Next.js - React - TypeScript

Backend: - Node.js - TypeScript

Razón: `@smogon/calc` y gran parte del ecosistema Pokémon competitivo ya
están en JS/TS.

Base de datos V1: - SQLite

ORM: - Drizzle o Prisma

Validation: - Zod

Testing: - Vitest

LLM: - provider abstraction

Compatible con: - OpenAI - Anthropic - Gemini - local OpenAI-compatible
endpoint

------------------------------------------------------------------------

## 5. Modelo central

`BattleState` es la fuente única de verdad.

``` ts
interface BattleState {
    battleId: string

    format: "champions-doubles"

    turn: number

    phase:
        | "TEAM_PREVIEW"
        | "TURN_SELECTION"
        | "TURN_RESOLUTION"
        | "BATTLE_END"

    player: SideState
    opponent: OpponentSideState

    field: FieldState

    history: TurnRecord[]

    beliefs: OpponentBeliefState

    metadata: BattleMetadata
}
```

------------------------------------------------------------------------

## 6. Pokémon State

``` ts
interface PokemonState {
    instanceId: string

    species: string
    form?: string

    level: number

    hp: {
        current: number
        max: number
    }

    status?: Status

    statPoints?: StatPointSpread

    nature?: string

    ability?: string
    item?: string

    moves: MoveState[]

    boosts: StatBoosts

    tera?: never

    mega: {
        capable: boolean
        stone?: string
        evolved: boolean
    }

    volatile: VolatileState

    revealed: RevealedInformation
}
```

------------------------------------------------------------------------

## 7. Equipo del usuario

Nuestro equipo es información perfecta.

``` text
StoredTeam {
    id
    name
    pokemon[6]
    rules
}
```

Cada Pokémon contiene: - especie - forma - Mega Stone - habilidad -
naturaleza - SP - movimientos - estadísticas finales

Ejemplo:

``` text
Garchomp:
    item: Garchompite Z
    nature: Modest

    moves:
      - Light of Ruin
      - Flamethrower
      - Draco Meteor
      - Protect
```

Nunca inferir información de nuestros Pokémon.

------------------------------------------------------------------------

## 8. Rival

El rival se representa mediante incertidumbre.

``` text
OpponentPokemonState {
    species

    observed:
        hp
        status
        moves[]
        ability?
        item?
        mega?
        statsEvidence[]

    belief:
        possibleSets[]
        possibleItems[]
        possibleAbilities[]
        possibleMoves[]
        possibleSP[]
        possibleMegas[]
}
```

------------------------------------------------------------------------

## 9. Belief Engine

Objetivo:

``` text
P(set | observations)
```

No necesitamos ML en V1.

Usaremos inferencia bayesiana aproximada.

Prior: meta usage.

Posterior:

``` text
P(set | evidence)
∝
P(evidence | set) × P(set)
```

Evidence: - movimiento revelado - habilidad - objeto - Mega - daño
causado - daño recibido - orden de velocidad - Protect - Fake Out -
weather - terrain - inmunidades - stat boosts - switch behaviour

------------------------------------------------------------------------

## 10. Ejemplo de inferencia

Inicial:

``` text
Staraptor

Mega Staraptor       0.62
Choice Band          0.14
Choice Scarf         0.10
Other                0.14
```

Observamos `Protect`.

Eliminar: - Choice Band - Choice Scarf

Renormalizar.

Posterior:

``` text
Mega Staraptor       0.87
Other Protect set    0.13
```

Después observamos una velocidad concreta.

Volver a filtrar.

------------------------------------------------------------------------

## 11. Meta Engine

``` ts
interface MetaEngine {
 getPokemonUsage(species)
 getMoveUsage(species)
 getItemUsage(species)
 getAbilityUsage(species)
 getPartnerUsage(species)
 getLeadUsage(species)
 getCommonSets(species)
 getArchetypes(team)
}
```

`MetaSnapshot`:

``` text
{
 format
 season
 generatedAt
 source
 sampleSize?
 data
}
```

Toda recomendación debe indicar qué snapshot está usando.

------------------------------------------------------------------------

## 12. Archetype Detector

Entrada: 6 Pokémon rivales.

Salida: `ArchetypeHypothesis[]`.

Ejemplo:

``` json
[
 {
   "type": "TRICK_ROOM",
   "confidence": 0.87,
   "enablers": ["Oranguru"],
   "abusers": ["Drampa", "Torkoal"]
 },
 {
   "type": "SAND",
   "confidence": 0.63,
   "enablers": ["Tyranitar"],
   "abusers": ["Excadrill"]
 }
]
```

No presentar `confidence` como probabilidad científica. Es un score
interno.

------------------------------------------------------------------------

## 13. Damage Engine

API:

``` text
calculateDamage(input): DamageResult
```

`DamageResult`:

``` text
{
 minDamage
 maxDamage

 minPercent
 maxPercent

 rolls[]

 koChance:
   oneHit
   twoHit

 modifiers[]

 assumptions[]
}
```

Nunca devolver solamente `"super effective"`.

Necesitamos números.

------------------------------------------------------------------------

## 14. Dual validation

Para casos compatibles:

``` text
NCP
 vs
@smogon/calc + Champions patches
```

Si coinciden:

``` text
validated=true
```

Si divergen:

``` text
validated=false
```

Registrar `CalculationDiscrepancy` y no ocultarlo.

------------------------------------------------------------------------

## 15. Speed Engine

Funciones:

``` text
calculateSpeed()
compareSpeed()
```

Debe soportar: - naturaleza - SP - boosts - paralysis - Tailwind - Trick
Room - Choice Scarf - abilities - weather abilities - priority - field
modifiers

Resultado:

``` text
SpeedOrderResult {
 first
 second
 tie
 reasons[]
}
```

------------------------------------------------------------------------

## 16. Field State

``` ts
interface FieldState {
 weather:
    NONE
    SUN
    RAIN
    SAND
    SNOW

 terrain:
    NONE
    PSYCHIC
    GRASSY
    ELECTRIC
    MISTY

 trickRoomTurns: number

 playerTailwindTurns: number
 opponentTailwindTurns: number

 otherEffects[]
}
```

------------------------------------------------------------------------

## 17. Turn Engine

Turn Engine es determinista.

Input:

``` text
BattleState
+
PlayerActions
+
OpponentActions
```

Output:

``` text
TurnOutcome
```

No decide qué hacer.

Solo ejecuta.

------------------------------------------------------------------------

## 18. Action Generator

Para cada Pokémon activo generar: - `AttackAction` - `ProtectAction` -
`SwitchAction` - `MegaAction`

Attack:

``` text
{
 actor
 move
 target
 megaBeforeAttack?
}
```

Combinamos ambos slots.

------------------------------------------------------------------------

## 19. Legalidad

Debe comprobar: - Pokémon vivo - movimiento disponible - target válido -
switch válido - no dos Pokémon cambiando al mismo slot - restricciones
Mega - Fake Out legality - move locks - Taunt - Encore - Disable -
status - etc.

------------------------------------------------------------------------

## 20. Mega constraint

Especialmente importante en Champions.

Team Preview: si dos Pokémon llevan Mega Stone:

``` text
Raichu Y
Garchomp Z
```

ambos **NO pueden formar parte del pick-4** cuando la regla del formato
lo prohíba.

`PreviewSolver` debe filtrar automáticamente combinaciones ilegales.

------------------------------------------------------------------------

## 21. Turn resolution

Pipeline:

1.  collect actions
2.  validate
3.  determine priority
4.  determine speed
5.  resolve switches
6.  resolve Mega
7.  resolve actions
8.  calculate damage
9.  apply effects
10. resolve abilities
11. resolve end-of-turn
12. decrement field counters
13. process fainted Pokémon
14. request replacements
15. generate new `BattleState`

Debe ser reproducible.

``` text
Mismo input + RNG seed
=
mismo output.
```

------------------------------------------------------------------------

## 22. RNG

No simular un único roll.

Search Engine debe poder utilizar: - EXPECTED - WORST_CASE - MONTE_CARLO

V1: - expected damage + KO probabilities.

Debug: - seeded RNG.

------------------------------------------------------------------------

## 23. Protect

El simulador debe conocer: - protección completa - movimientos que
atraviesen Protect - spread interactions - consecutive Protect
probability

Estado:

``` text
protectChain: number
```

------------------------------------------------------------------------

## 24. Fake Out

Validar: - primer turno en campo - prioridad - Psychic Terrain -
habilidades relevantes - Ghost immunity cuando corresponda - flinch
immunity - Protect

------------------------------------------------------------------------

## 25. Trick Room

NO cambiar estadísticas.

Modificar comparator de velocidad.

Normal:

``` text
priority DESC
speed DESC
```

TR:

``` text
priority DESC
speed ASC
```

Priority sigue teniendo precedencia.

------------------------------------------------------------------------

## 26. Tailwind

`SpeedEngine` recibe:

``` text
tailwind=true
```

No meter valores modificados permanentemente en Pokémon.

------------------------------------------------------------------------

## 27. Switch Engine

Al cambiar, procesar: - hazards si Champions los admite en ese
contexto - Intimidate - terrain setters - weather setters - entry
abilities - Fake Out eligibility reset - volatile cleanup

------------------------------------------------------------------------

## 28. Simulator

Simulator explora:

``` text
OurActionPair
×
OpponentActionPair
×
RelevantHiddenSets
```

No podemos hacer producto cartesiano completo.

Necesitamos pruning.

------------------------------------------------------------------------

## 29. Opponent Action Model

Generar inicialmente todas las acciones legales.

Después asignar:

``` text
plausibilityScore
```

Factores: - meta usage - damage - KO potential - protect - setup -
switch synergy - speed control - board position

Descartar ramas irrelevantes.

Ejemplo:

``` text
Top K opponent actions = 8
```

Configurable.

------------------------------------------------------------------------

## 30. Search Engine

V1: - Expectiminimax limitado.

Depth: - 2 ply por defecto. - Opcional: 3 ply.

No buscar partida completa.

------------------------------------------------------------------------

## 31. Evaluación del estado

NO usar únicamente HP.

``` text
score =
  material
+ boardPosition
+ speedControl
+ offensivePressure
+ defensivePosition
+ fieldControl
+ setup
+ information
- koRisk
- trappedRisk
- opponentPressure
```

------------------------------------------------------------------------

## 32. Material score

KO: gran penalización.

Pero preservar Pokémon críticos debe tener valor contextual.

Ejemplo: si rival conserva Basculegion, `Rillaboom alive` tiene mayor
strategic value.

Esto lo puede aportar Strategy Layer.

------------------------------------------------------------------------

## 33. Risk metrics

Para cada línea: - expectedValue - worstCase - bestCase - variance -
koRisk - doubleKOProbability - positionAfterTurn

------------------------------------------------------------------------

## 34. Recommendation Engine

No devolver simplemente `bestAction`.

Devolver:

``` text
Recommendation {
 primaryLine
 alternatives[]
 confidence
 keyRisks[]
 assumptions[]
 calculations[]
 opponentLikelyResponses[]
}
```

------------------------------------------------------------------------

## 35. Preview Solver

Entrada:

``` text
OurTeam[6]
OpponentTeam[6]
```

Proceso:

Generar combinaciones legales:

``` text
C(6,4) = 15
```

menos incompatibilidades Mega.

Para cada pick-4:

generar leads:

``` text
C(4,2) = 6
```

Evaluar: - matchups - speed - coverage - defensive switching -
archetypes - opponent leads - Mega choice - win conditions

------------------------------------------------------------------------

## 36. Preview output

Ejemplo:

``` text
SELECT

Garchomp Z
Incineroar
Rillaboom
Gholdengo

LEAD

Gholdengo + Incineroar

BACK

Garchomp + Rillaboom

OPPONENT MODES

Trick Room       HIGH
Mega Drampa      MEDIUM
Sand             MEDIUM

KEY PLAN

Prevent free Trick Room.
Preserve Rillaboom for Primarina.
Do not expose Garchomp to Fairy damage.
```

------------------------------------------------------------------------

## 37. LLM Tool Layer

El LLM recibe herramientas:

``` text
get_battle_state()
get_our_team()
get_opponent_beliefs()
get_meta()
calculate_damage()
compare_speed()
get_legal_actions()
simulate_line()
search_best_lines()
record_observation()
```

NO puede modificar directamente `BattleState`.

------------------------------------------------------------------------

## 38. LLM System Contract

Prompt base:

``` text
You are the strategic reasoning layer of a
Pokémon Champions Doubles battle engine.

Never invent:
- damage
- speed
- moves
- items
- abilities
- mechanics
- usage statistics.

Use tools.

Separate:
KNOWN
INFERRED
UNKNOWN.

A recommendation must be supported by
calculated or observed evidence.
```

------------------------------------------------------------------------

## 39. Anti-hallucination

Cada `StrategicClaim`:

``` text
{
 claim
 provenance
}
```

Provenance: - OBSERVED - DEX - META - CALCULATOR - SIMULATION -
INFERENCE

Ejemplo:

``` text
"Staraptor outspeeds Garchomp"

source:
SPEED_CALCULATOR
```

No provenance: no mostrar como hecho.

------------------------------------------------------------------------

## 40. Battle Copilot UI

Pantalla principal:

``` text
┌────────────────────────────────────────────┐
│ TURN 3          TR: 2       GRASS: 3      │
├───────────────────┬────────────────────────┤
│ OUR FIELD         │ OPPONENT FIELD         │
│ Garchomp 81%      │ Staraptor 53%          │
│ Incineroar 64%    │ Incineroar 91%         │
├───────────────────┼────────────────────────┤
│ OUR BACK          │ OPPONENT BACK          │
│ Rillaboom 100%    │ ???                    │
│ Gholdengo 72%     │ ???                    │
├───────────────────┴────────────────────────┤
│ RECOMMENDED                               │
│                                           │
│ Garchomp → Protect                        │
│ Incineroar → Parting Shot → Staraptor     │
│                                           │
│ Main risk: Close Combat                   │
│ Expected position: +1.8                   │
│                                           │
│ [SIMULATE] [ALTERNATIVES]                 │
└────────────────────────────────────────────┘
```

------------------------------------------------------------------------

## 41. Team Preview UI

6 Pokémon propios.

6 Pokémon rivales.

Botón:

``` text
ANALYZE PREVIEW
```

Resultado: - archetype - probable Mega(s) - likely leads - recommended
4 - recommended lead - backline - threats - win conditions

------------------------------------------------------------------------

## 42. Battle input V1

No intentar computer vision todavía.

Input manual rápido.

Botones grandes:

``` text
Opponent used:
[move]

Target:
[pokemon]

HP after:
[slider/input]

Switch:
[pokemon]

Mega:
[pokemon]

Protect:
[button]
```

Esto permite registrar un turno en segundos.

------------------------------------------------------------------------

## 43. Quick Input

Comando textual adicional:

``` text
"staraptor mega, cc garchomp, 81>23,
inci parting gholdengo"
```

Parser:

``` text
ObservationParser
```

Convierte texto a eventos estructurados.

LLM puede ayudar a parsear.

Pero usuario confirma antes de alterar estado.

------------------------------------------------------------------------

## 44. Event sourcing

`BattleState` NO se edita arbitrariamente.

Guardar:

``` text
BattleEvent[]
```

Ejemplos: - MOVE_USED - DAMAGE - HEAL - SWITCH - FAINT - MEGA -
ABILITY_REVEALED - ITEM_REVEALED - STATUS - WEATHER - TERRAIN -
TRICK_ROOM - TAILWIND

`BattleState` se reconstruye desde eventos.

Beneficio: **UNDO**.

Fundamental cuando el usuario introduce algo mal.

------------------------------------------------------------------------

## 45. Persistence

SQLite: - teams - battles - battle_events - meta_snapshots -
pokemon_sets - calculations - recommendations

------------------------------------------------------------------------

## 46. Replay

Cada batalla queda guardada.

Posteriormente:

``` text
REPLAY ANALYSIS
```

Identifica: - turnos críticos - recomendaciones tomadas - alternativa
superior - predicciones incorrectas - sets revelados - errores del
modelo

------------------------------------------------------------------------

## 47. Feedback loop

Después del combate:

``` text
Did opponent have:
[x] Mega Staraptor
[x] Protect
[x] Close Combat
...
```

Esto permite evaluar el Belief Engine.

NO actualizar automáticamente estadísticas globales del meta con una
sola partida.

Guardar como local observations.

------------------------------------------------------------------------

## 48. API

``` text
POST /preview/analyze

POST /battles

GET /battles/:id

POST /battles/:id/events

POST /battles/:id/recommend

POST /battles/:id/simulate

POST /damage

POST /speed

GET /meta/:pokemon

GET /teams

POST /teams
```

------------------------------------------------------------------------

## 49. `/preview/analyze`

Request:

``` json
{
  "ourTeamId": "team-id",
  "opponent": [
    "Tyranitar",
    "Steelix",
    "Primarina",
    "Oranguru",
    "Drampa",
    "Archaludon"
  ]
}
```

Response:

``` text
{
 archetypes,
 megaCandidates,
 recommendedSelection,
 lead,
 back,
 threats,
 plan
}
```

------------------------------------------------------------------------

## 50. `/recommend`

Response:

``` text
{
 actions: [
   {
     pokemon: "Garchomp",
     action: "PROTECT"
   },
   {
     pokemon: "Incineroar",
     action: "PARTING_SHOT",
     target: "Staraptor"
   }
 ],

 score,
 risk,
 alternatives,
 explanation,
 evidence
}
```

------------------------------------------------------------------------

## 51. Performance target

Team Preview: - `< 3 seconds`

Turn recommendation: - `< 2 seconds deterministic` -
`< 5 seconds with LLM explanation`

Damage calculation: - `< 100 ms typical`

UI update: - instant.

------------------------------------------------------------------------

## 52. Cache

Cachear: - damage calculations - speed calculations - meta queries - dex
queries

Damage cache key debe incluir: - attacker state - defender state -
move - field - boosts - ability - item - Mega - spread context

------------------------------------------------------------------------

## 53. Testing strategy

Tres niveles.

### UNIT

-   DamageEngine
-   SpeedEngine
-   ActionGenerator
-   TurnResolver
-   BeliefEngine

### INTEGRATION

-   full turn simulation.

### GOLDEN BATTLES

-   escenarios conocidos con resultado esperado.

------------------------------------------------------------------------

## 54. Golden tests críticos

### TRICK ROOM

``` text
Farigiraf uses Trick Room.
Verify reversed speed next turn.
```

### PSYCHIC TERRAIN

``` text
Indeedee terrain.
Fake Out blocked.
```

### RILLABOOM SWITCH

``` text
Rillaboom enters.
Psychic → Grassy.
Fake Out enabled afterward.
```

### INTIMIDATE

``` text
Incineroar enters.
Physical Attack reduced.
Special Garchomp unaffected.
```

### PROTECT

``` text
damage = 0.
```

### TAILWIND

``` text
speed ordering changes.
```

### MEGA

``` text
only legal Mega selected.
```

------------------------------------------------------------------------

## 55. Damage validation suite

Crear dataset:

``` text
tests/golden/damage.json
```

Casos conocidos.

Comparar: - NCP - Smogon patched - expected reference

Tolerancia: - `0` para reglas deterministas.

------------------------------------------------------------------------

## 56. Observability

Cada recomendación genera trace:

``` text
RecommendationTrace {
 battleState
 candidateActions
 opponentBranches
 calculations
 prunedBranches
 scores
 selectedLine
 llmInput
 llmOutput
}
```

Necesario para saber **por qué** falló.

------------------------------------------------------------------------

## 57. Failure modes

Si meta no disponible: - usar último snapshot. - mostrar `META STALE`.

Si Damage Engine diverge: - mostrar `CALCULATION UNVERIFIED`.

Si rival tiene set desconocido: - ampliar uncertainty.

Si LLM falla: - mostrar recomendación matemática sin explicación LLM.

El programa debe funcionar sin LLM.

------------------------------------------------------------------------

## 58. Orden de implementación

### PHASE 1

Domain + Champions data.

### PHASE 2

Nuestro Team Store.

### PHASE 3

Damage Engine.

### PHASE 4

Speed Engine.

### PHASE 5

BattleState + Events.

### PHASE 6

Turn Resolver.

### PHASE 7

Action Generator.

### PHASE 8

Meta Engine.

### PHASE 9

Belief Engine.

### PHASE 10

Preview Solver.

### PHASE 11

Simulator.

### PHASE 12

Search Engine.

### PHASE 13

Recommendation Engine.

### PHASE 14

LLM tool layer.

### PHASE 15

Web UI.

### PHASE 16

Replay + debugging.

------------------------------------------------------------------------

## 59. V1 Definition of Done

La V1 NO está terminada porque exista una interfaz.

Debe superar:

1.  Importar nuestro equipo real.
2.  Introducir 6 rivales.
3.  Detectar arquetipo.
4.  Detectar Megas posibles.
5.  Respetar restricción Mega.
6.  Seleccionar 4.
7.  Recomendar lead/back.
8.  Iniciar batalla.
9.  Registrar switches.
10. Registrar movimientos.
11. Registrar HP.
12. Registrar Mega.
13. Manejar Protect.
14. Manejar Fake Out.
15. Manejar Intimidate.
16. Manejar terrain.
17. Manejar weather.
18. Manejar Trick Room.
19. Manejar Tailwind.
20. Calcular daño.
21. Calcular Speed.
22. Inferir sets.
23. Actualizar inferencias.
24. Generar acciones legales.
25. Simular rival.
26. Buscar ≥2 ply.
27. Recomendar acción doble.
28. Mostrar alternativa.
29. Mostrar riesgos.
30. Mostrar cálculos.
31. Guardar batalla.
32. Undo.
33. Replay.
34. Funcionar si LLM cae.

------------------------------------------------------------------------

## 60. NO entra en V1

-   Computer Vision automática.
-   OCR del combate.
-   Control automático del juego.
-   Machine learning entrenado.
-   Self-play masivo.
-   RL.
-   MCTS profundo.
-   Reconocimiento automático desde vídeo.
-   Cloud obligatorio.
-   Mobile app nativa.

Son V2+.

------------------------------------------------------------------------

## 61. Resultado final V1

``` text
TEAM PREVIEW
     ↓
6 enemigos
     ↓
META + DEX
     ↓
ARCHETYPE DETECTION
     ↓
POSSIBLE MEGAS
     ↓
15 PICK-4
     ↓
LEGALITY FILTER
     ↓
LEAD SEARCH
     ↓
DAMAGE/SPEED/MATCHUPS
     ↓
RECOMMENDED 4
     ↓
BATTLE START
     ↓
OBSERVATIONS
     ↓
BATTLE STATE
     ↓
BELIEF UPDATE
     ↓
ACTION GENERATION
     ↓
DAMAGE + SPEED
     ↓
OPPONENT BRANCHES
     ↓
2v2 SIMULATION
     ↓
SEARCH
     ↓
RISK EVALUATION
     ↓
LLM STRATEGIC ANALYSIS
     ↓
RECOMMENDATION
     ↓
USER PLAYS TURN
     ↓
NEW OBSERVATIONS
     └──────────────→ repeat
```

La diferencia esencial respecto a una recomendación puramente
conversacional es que el sistema ya no diría simplemente «creo que
Garchomp es mejor». Tendría que demostrarlo con el estado, los sets
compatibles con lo observado, el meta, speed tiers, cálculos de daño y
simulación de las principales respuestas del rival.

Esta es la V1 objetivo. No se recortan `BattleState`, `Belief Engine`,
simulador o búsqueda para convertirla en una demo superficial, porque
precisamente esas piezas son las que convierten una calculadora con un
chatbot encima en un **copiloto de batalla real**.
