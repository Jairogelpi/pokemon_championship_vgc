# Alcance

## V1 obligatoria

Las 16 fases de [ROADMAP](../planning/ROADMAP.md) constituyen una V1 única: dominio/datos, equipo propio, daño, speed, eventos/estado, turnos, acciones, meta, beliefs, preview, simulador, búsqueda, recomendaciones, herramientas LLM, web, replay/debug.

Incluye entrada manual y texto confirmado; preview de seis rivales, pick-4 legal, lead/back; combate 2v2 completo dentro del ruleset soportado; incertidumbre, undo, SQLite, snapshots, trazas, degradación ante fallos y validación dual donde sea compatible. Búsqueda limitada de ≥2 ply y modo V1 de daño esperado con probabilidades KO. El motor debe diseñar la interfaz para EXPECTED/WORST_CASE/MONTE_CARLO; la entrega inicial del modo Monte Carlo se concreta en SPEC-011 y Q-010, sin simular que ya existe.

## V2+ excluida

Computer vision, OCR, control automático del juego, ML entrenado, self-play masivo, RL, MCTS profundo, reconocimiento desde vídeo, cloud obligatorio y aplicación móvil nativa. Fuente: original §60.

## Límites de este cambio

Este bootstrap crea documentación y reglas de ejecución; no implementa aún el producto. La UI no será sustituto del motor y una fase intermedia no se denominará V1 terminada.

## Cambios de alcance

Registrar propuesta, requisitos afectados, impacto y decisión del usuario cuando cambie el producto solicitado. Correcciones de ejemplos mecánicos con evidencia no eliminan capacidades; se documentan con ADR o registro de investigación. Una fuente ausente produce un bloqueo o estado no verificado, nunca una cifra inventada.
