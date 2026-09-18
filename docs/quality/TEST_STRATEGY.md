# Estrategia de pruebas y evaluación

## Capas

- Unit: domain, DamageEngine, SpeedEngine, ActionGenerator, TurnResolver, BeliefEngine; lógica pura y casos negativos.
- Contract: adapters, API, persistence ports, herramientas/proveedores LLM. Inputs/salidas inválidos y capacidades no soportadas.
- Integration: turno completo, eventos+SQLite+replay, search con calculadores reales del ruleset soportado.
- Regression/battle scenarios/golden: resultados mecánicos y secuencias conocidas con fuente independiente.
- UI end-to-end: equipo→preview→batalla→observación confirmada→recomendación→undo→replay; incertidumbre y errores visibles.
- Performance: condiciones reproducibles; separar cálculo determinista de coste LLM/red y cache warm/cold.

## Golden obligatorios (§54)

| Familia | Caso positivo y condiciones que deben fijarse |
|---|---|
| Trick Room | Orden inverso de speed dentro de la misma prioridad; estadísticas intactas; duración/activación según ruleset |
| Psychic Terrain | Fake Out bloqueado contra target elegible/grounded cuando corresponda; no afirmar bloqueo universal |
| Rillaboom switch | Sustitución Psychic→Grassy y reevaluación de bloqueo, conservando otros impedimentos a Fake Out |
| Intimidate | Stage de ataque físico según abilities/inmunidades; daño especial no utiliza ese stage |
| Protect | Daño cero solo cuando protección aplica; probar movimientos/excepciones/spread y cadena |
| Tailwind | Orden cambia por efecto contextual; expiración restaura contexto |
| Mega | Pick-4 y evolución respetan exactamente reglas versionadas, no prohibición inventada |

## Daño dual

`tests/golden/damage.json` se creará con casos auditados, no con números de ejemplo. Cada caso conserva source URL/revision, ruleset, input completo, esperado, engine versions y alcance. Comparar NCP/Smogon patched/referencia independiente; tolerancia 0 determinista. Mismo origen de ambos motores limita confianza; documentarlo. Golden sin procedencia no valida mecánica.

## Beliefs y search

Fixture manual de prior×likelihood→posterior; posterior vacío; HP por intervalo; moves/abilities/items revelados; inferencias compatibles y contradictorias. No excluir Choice solo por el ejemplo no contrastado. Árbol pequeño enumerable valida selección expectiminimax y riesgos; seed fijo prueba reproducibilidad, no calidad estratégica por sí mismo. Pruning y top-K se comparan con búsqueda exhaustiva en problemas pequeños; reportar tradeoff, no óptimo global.

## Persistencia y seguridad del estado

Idempotencia, concurrencia/revision, rollback transaccional, eventos corruptos/versionados, simulación aislada y undo/replay. El estado reconstruido debe coincidir con el esperado y conservar procedencia. Ningún parser/LLM persiste un draft sin confirmación del usuario.

## Evaluación de calidad y rendimiento

Benchmark antes de cerrar SPEC-013: registrar CPU/RAM/runtime, versiones, tamaño de snapshots, profundidad, top-K, set count, seeds, warm-up, muestras y latencias. Conservar objetivos <3s preview, <2s recomendación determinista, <5s con explicación y <100ms daño típico; percentiles y criterio UI pendiente Q-009. No bajar profundidad o quitar incertidumbre en silencio para cumplir latencia.

Recomendaciones se evalúan con escenarios y revisión estratégica separada de la exactitud mecánica. Confidence de arquetipo/recomendación es un score hasta calibración explícita. Una tasa de victoria anecdótica no valida search.

## Evidencia y gates

Usar verification por spec. `PASS` solo con test ejecutado; `NOT RUN`, `FAIL`, `BLOCKED` y `NOT APPLICABLE` se distinguen. Typecheck/lint/build se agregan en SPEC-001. La V1 requiere 34 AC y todos los REQ, no un porcentaje de cobertura de líneas elegido arbitrariamente.
