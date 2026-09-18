# Flujos de datos

## Preparación y preview

1. Ingesta upstream → validación → adaptación → snapshot Dex/reglas con hash.
2. Equipo propio → validación completa y legalidad → SQLite; rechazar/informar campos faltantes.
3. Seis rivales → snapshots meta/dex → hipótesis de arquetipo/Mega/sets.
4. Enumerar pick-4 y leads → filtro ruleset → daño/speed/matchup/planes → recomendación con evidencia.

## Turno real

1. UI manual o texto → parser → propuesta estructurada; usuario confirma.
2. API verifica revisión, identidad y payload; transacción inserta batch de eventos una sola vez.
3. Reducer proyecta nuevo estado; Belief Engine aplica evidencia sobre priors versionados.
4. Generador produce acciones legales; modelo rival prioriza ramas; simulador usa copias del estado.
5. Search evalúa horizonte, incertidumbre y riesgo; copilot selecciona línea y alternativas.
6. Persistir recomendación/trace asociada a revisión; LLM opcional explica solo evidencias permitidas.
7. UI descarta resultados obsoletos si la revisión cambió mientras se calculaba.

## Undo y replay

Undo crea una corrección/auditoría y nueva revisión; no borra silenciosamente evidencia histórica. Reconstruye estado desde eventos efectivos, beliefs y snapshot fijado. Replay reproduce primero con versiones originales; análisis con motor nuevo es un resultado separado. Feedback se almacena como observación local, nunca como frecuencia global actualizada.

## Fallos

Meta inaccesible: último snapshot + META STALE; sin snapshot: UNKNOWN y estrategia sin usage inventado. Cálculos discrepantes: CALCULATION UNVERIFIED y riesgo visible. Regla no soportada: error estructurado, no default de otra generación. LLM timeout: recomendación calculada. Search timeout: devolver solo resultado parcial legal ya verificado con profundidad alcanzada, o error claro si no existe ninguno.
