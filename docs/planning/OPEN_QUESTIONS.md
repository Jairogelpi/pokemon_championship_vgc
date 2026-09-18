# Preguntas abiertas y supuestos

Resolver con evidencia, no con memoria de otras generaciones. No alterar la fuente original. Estos puntos no reducen la V1: impiden convertir ejemplos en reglas inventadas.

| ID | Pregunta / riesgo | Dueño y bloqueo | Cómo cerrarla |
|---|---|---|---|
| Q-001 | ¿Cuál es el ruleset/temporada Champions objetivo, SP, roster, formas, moves y restricciones Mega exactos? | SPEC-001/003/007/010; reglas reales | Fuente primaria o dataset trazable, fecha y revisión; fixtures de casos permitidos/prohibidos |
| Q-002 | ¿Qué APIs/datos ofrecen realmente los cinco upstreams, con qué licencia y versión? | SPEC-001; integración upstream | Auditar repos y registrar capacidades/licencia/commit; no asumir que un nombre implica soporte |
| Q-003 | Original §10 elimina Choice tras Protect; observar un movimiento aislado no demuestra por sí mismo incompatibilidad del objeto | SPEC-009; inferencia | Definir likelihood/locks/revelaciones con reglas verificadas; conservar candidatos si evidencia no excluye |
| Q-004 | Pipeline §21 es conceptual: KO, entrada, cambios de speed/forma y efectos intercalados requieren orden preciso | SPEC-006; resolver | Tabla de orden de efectos y golden independientes por interacción |
| Q-005 | ¿Ply significa decisión de un lado, par de decisiones simultáneas o turno resuelto? | SPEC-012; profundidad/benchmark | ADR con definición, ejemplo árbol de 2/3 ply y horizonte de turnos; no reducir la intención de anticipación |
| Q-006 | Drizzle o Prisma; versiones Node/Next/TS; gestor de paquetes | SPEC-001/002; scaffold | Comparar SQLite/migraciones/entorno; elegir y fijar versiones con fuentes oficiales |
| Q-007 | Falta equipo real exacto del usuario con SP, moves, nature, ability, item | SPEC-002 y AC-V1-01 | Importación o datos del usuario; no completar desde recuerdos ni usar ejemplo §7 como equipo real |
| Q-008 | Independencia NCP/Smogon y disponibilidad del oráculo de daño | SPEC-003; validated=true | Documentar linaje, cobertura y referencia externa; UNVERIFIED si falta |
| Q-009 | Hardware, dataset, percentil y definición operativa de UI «instantánea» | SPEC-013/015; performance | Protocolo benchmark; conservar umbrales originales sin convertirlos en garantías no medidas |
| Q-010 | EXPECTED/WORST_CASE/MONTE_CARLO: interfaz general y V1 expected+KO; alcance exacto modos opcionales | SPEC-011 | Concretar modos entregados, errores de modo no disponible y roadmap sin borrar requisito original |
| Q-011 | HP rival parcial, reservas ocultas y posterior vacío | SPEC-001/009 | Representar intervalos/unknown y contradicciones; fixtures que no exijan dato oculto |
| Q-012 | Política de undo y schema migrations de eventos | SPEC-005 | ADR, atomicidad, historial efectivo y replay reproducible |

Estado inicial de todos: OPEN. Fecha de apertura: 2026-09-18. Registrar al cerrar fuente, decisión y requisitos afectados. Se pueden continuar tareas independientes mientras la mecánica afectada permanezca bloqueada o explícitamente no verificada.
