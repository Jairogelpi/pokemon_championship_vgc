# Registro upstream

**Pendiente de auditoría.** Esta lista procede del original §2; no certifica existencia actual, licencia, calidad o compatibilidad. Primera tarea de SPEC-001: leer los repos reales y completar los campos con evidencia. No descargar código/datos para redistribuir sin revisar licencia.

| Fuente solicitada | Uso previsto en el original | Adapter / consumidor | Commit, licencia, soporte comprobado |
|---|---|---|---|
| https://github.com/pmwl0128/pokemon_champion_agent | Dex, SP, legalidad, Mega, meta, NCP, speed, conocimiento Champions | champions-data/champions_agent | PENDING |
| https://github.com/SebNotFound/champions-calc | Adaptaciones Champions, Smogon, SP y 2v2 | damage-engine/champions_calc | PENDING |
| @smogon/calc | Matemática cuando mecánica soportada; wrapper sin modificar paquete | damage-engine/SmogonCalcAdapter | PENDING |
| https://github.com/huydamm/PokemonVGC-Calculator | Representación equipos/condiciones/inferencia/estado/UI como referencia | Adaptadores según capacidad auditada | PENDING |
| https://github.com/MSS23/vgc-mcp | Lifecycle, herramientas, patrones de tests y validación | llm/copilot como referencia | PENDING |

## Evidencia requerida por fuente

URL exacta, fecha, commit/tag y hash, licencia de código y datos por separado, rutas relevantes, método de ingestión, capacidades reales, reglas soportadas, fixtures, mantenimiento, limitaciones y decisión reutilizar/adaptar/referenciar/rechazar. No sustituir «sin licencia» por permiso implícito. Fijar versiones; guardar manifests pequeños, no vendorizar repos completos por defecto.

Los ejemplos de especies/sets de la spec se conservan como ejemplos históricos, nunca como dataset inicial. Una tabla de compatibilidad por ruleset y mecánica debe acompañar al adaptador antes de presentar daño/velocidad como verificados.
