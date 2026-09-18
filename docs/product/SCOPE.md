# Alcance

## V1 obligatoria

Las 16 fases de [ROADMAP](../planning/ROADMAP.md) constituyen una V1 única: dominio/datos, equipo propio, daño, speed, eventos/estado, turnos, acciones, meta, beliefs, preview, simulador, búsqueda, recomendaciones, herramientas LLM, web, replay/debug.

Incluye entrada manual y texto confirmado; preview de seis rivales, pick-4 legal, lead/back; combate 2v2 completo dentro del ruleset soportado; incertidumbre, undo, SQLite, snapshots, trazas, degradación ante fallos y validación dual donde sea compatible. Búsqueda limitada de ≥2 ply y modo V1 de daño esperado con probabilidades KO. El alcance conserva los tres modos EXPECTED, WORST_CASE y MONTE_CARLO exigidos para Search Engine en §22; el camino principal V1 usa daño esperado y probabilidades KO. SPEC-011 y SPEC-012 deben concretar e implementar el soporte, no solo declarar un enum. Q-010 define semántica y presupuesto; no autoriza posponer modos ni trasladarlos a V2 sin una decisión explícita de alcance.

## V2+ excluida

Computer vision, OCR, control automático del juego, ML entrenado, self-play masivo, RL, MCTS profundo, reconocimiento desde vídeo, cloud obligatorio y aplicación móvil nativa. Fuente: original §60.

## Límites de este cambio

Este bootstrap crea documentación y reglas de ejecución; no implementa aún el producto. La UI no será sustituto del motor y una fase intermedia no se denominará V1 terminada.

## Cambios de alcance

Registrar propuesta, requisitos afectados, impacto y decisión del usuario cuando cambie el producto solicitado. Correcciones de ejemplos mecánicos con evidencia no eliminan capacidades; se documentan con ADR o registro de investigación. Una fuente ausente produce un bloqueo o estado no verificado, nunca una cifra inventada.
