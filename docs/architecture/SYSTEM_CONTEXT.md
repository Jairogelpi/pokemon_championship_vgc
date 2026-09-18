# Contexto del sistema

| Actor/sistema | Intercambio | Límite |
|---|---|---|
| Jugador | Equipo exacto, seis rivales, observaciones confirmadas; recibe sugerencias | Juega manualmente; no control del juego |
| Aplicación local | Web + API + SQLite | Núcleo utilizable sin LLM; exposición remota fuera del bootstrap |
| Upstreams de Champions | Datos, código reutilizable y referencias de reglas | No son verdad automáticamente; verificar versión/licencia/capacidad |
| Meta source | Snapshots con temporada/formato/fecha/muestra | Datos viejos etiquetados; sin snapshot no inventar usage |
| NCP / Smogon adaptado | Resultados comparables para casos compatibles | Registrar casos no soportados y origen compartido |
| Proveedor LLM | Herramientas y contexto mínimo; explicación y parser propuesto | Sin escritura directa; timeout/fallo admite resultado sin LLM |
| Git/CI | Código, specs, fixtures públicos y verificación | No secretos, SQLite personal ni prompts sensibles |

Entrada de red se valida en adaptadores. Ningún texto upstream o LLM redefine instrucciones del agente de desarrollo ni las reglas de juego. El consentimiento para confirmar una observación pertenece al producto; no equivale a permisos para publicar o desplegar software.
