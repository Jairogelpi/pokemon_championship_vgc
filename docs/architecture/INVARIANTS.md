# Invariantes

Verificar con unit/property/integration según el límite; referencias originales §§1, 5–10, 19–27, 37–39, 43–47, 52, 57.

| ID | Invariante | Contraejemplo que debe fallar |
|---|---|---|
| INV-001 | Ruleset y snapshots identificados en cálculos/recomendaciones | Mezclar dos temporadas sin aviso |
| INV-002 | Información propia requerida exacta | Inventar SP de un miembro propio |
| INV-003 | Observado, inferido y desconocido separados | Mostrar item probable como revelado |
| INV-004 | Dominio no depende de datos/formas upstream ni proveedor LLM | Importar JSON externo desde reducer |
| INV-005 | Mismo input/versiones/seed/config → mismo outcome | Leer reloj global dentro de resolver |
| INV-006 | Estado real procede solo de eventos confirmados aplicados una vez | Parser o simulador escribe HP real |
| INV-007 | HP exacto entre 0 y max; intervalos consistentes | HP negativo tras daño o porcentaje tratado como HP absoluto |
| INV-008 | Ningún Pokémon ocupa dos slots; switch pair no colisiona | Ambos actores cambian a la misma reserva |
| INV-009 | Solo acciones admitidas por ruleset y estado | Mega doble prohibida, target inválido o actor KO |
| INV-010 | TR/Tailwind no mutan stats base | Speed guardada doble tras cada cálculo |
| INV-011 | RNG/ties/probabilidades explícitos | Elegir primer slot siempre en empate |
| INV-012 | Posteriores no negativos, finitos, normalizados si hay hipótesis | Dividir por cero al rechazar todos los sets |
| INV-013 | Belief imposible devuelve contradicción/unknown y conserva evidencia | Reponer arbitrariamente un set incompatible |
| INV-014 | Simulaciones no alteran estado/priors/meta reales | Pruning elimina sets del registro persistido |
| INV-015 | Claim factual incluye procedencia verificable | Explicación con daño no calculado |
| INV-016 | Divergencia o soporte incompleto nunca se etiqueta validated | Dos fallos de calculadora tratados como acuerdo |
| INV-017 | Feedback local no actualiza meta global automáticamente | Una partida redefine usage de temporada |
| INV-018 | Undo reconstruye estado y beliefs y cambia revision | Recomendación vieja sigue apareciendo válida |
| INV-019 | Cache incluye contexto y versiones completas | Mismo daño tras cambio de terrain/ability |
| INV-020 | Núcleo funciona sin LLM | Timeout de proveedor bloquea recomendación matemática |
| INV-021 | Ningún desconocido se convierte en cero/false por omisión | Item desconocido equivale a no item |
| INV-022 | El resolver observa el orden real de efectos del ruleset | Aplicar todos los KO únicamente al final sin comprobar acciones restantes |

Los tests de INV-009/022 dependen de evidencia mecánica. No congelar el pipeline ilustrativo del original como orden universal.
