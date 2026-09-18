# Instrucciones del proyecto

## Arranque y contexto mínimo

1. Lee `state.md`: fase, trabajo activo, bloqueos y siguiente acción.
2. Lee `memory.md`: decisiones estables y advertencias con referencias.
3. Lee `conventions.md` y `docs/agents/CONTEXT_MAP.md`.
4. Selecciona una tarea de `docs/planning/ROADMAP.md`; carga solo su spec, diseño, invariantes, contratos y skill aplicable. Consulta las secciones originales que cita.
5. Inspecciona código, estado Git y pruebas existentes antes de editar. Un estado escrito no demuestra que el código esté implementado.

## Autoridad y alcance

Las instrucciones actuales del usuario prevalecen. `docs/source/V1_SPEC_ORIGINAL.md` conserva el encargo histórico íntegro; los requisitos derivados y ADR explican su interpretación. Una contradicción se registra en `docs/planning/OPEN_QUESTIONS.md` y se resuelve explícitamente: nunca se altera la fuente ni se reduce la V1 silenciosamente. Los ejemplos de especies, formas, sets y mecánicas no acreditan legalidad.

`AGENTS.md` gobierna el trabajo; `memory.md` conserva conocimiento; `state.md` registra progreso; una spec define comportamiento; un ADR justifica una decisión. Ninguno sustituye a los otros. No crear variantes `Agents.md`/`agents.md` que colisionen en Windows.

## Entrega mediante SDD y TDD

Sigue `docs/workflows/SDD_TDD.md`: explorar → propuesta → spec con aceptación → diseño/ADR → tareas → RED → GREEN → refactor → verificación → revisión → actualización de estado. No convertir un test ausente o saltado en evidencia de éxito. Para cambios documentales, validar trazabilidad y enlaces; no fingir un ciclo RED/GREEN del producto.

Antes de implementar, la tarea debe tener entradas, salidas, fallos, casos límite y criterio verificable. La lista `docs/quality/DETAILED_COVERAGE.md` desglosa cada sección: cargar las secciones asignadas y vincular todos sus subrequisitos y enumeraciones a aceptación/tests. Ni tres criterios genéricos ni un enlace a la fuente bastan para declarar una fase completa. Resuelve detalles reversibles dentro del alcance; escala únicamente decisiones de producto o bloqueos externos reales. Las specs de fases futuras son DRAFT, no permiso para inventar mecánicas.

## Límites técnicos obligatorios

- El LLM no calcula mecánicas ni modifica `BattleState`; trabaja con herramientas y evidencias.
- Estado real reconstruido desde eventos confirmados; simulaciones aisladas.
- Separar observado, inferido y desconocido. Equipo propio exacto, nunca completado por conjetura.
- Dominio independiente de proveedores, ORM, HTTP y repos upstream; usar adaptadores.
- Ruleset, datos, meta y motores versionados. No asumir reglas de otro juego o temporada.
- No declarar compatibilidad/dual validation sin fixtures independientes. Divergencia visible.
- No eliminar BattleState, Belief Engine, simulador o búsqueda para entregar una demo.

## Delegación

El proyecto usa los roles y handoffs de `docs/agents/ORCHESTRATION.md`. El coordinador decide cuándo la tarea se beneficia de subagentes; un runtime sin delegación ejecuta los mismos roles secuencialmente y lo registra. Cada worker recibe tarea, alcance de escritura, skill, referencias, dependencias y aceptación. Un único escritor por archivo. El revisor contrasta evidencia y comportamiento, no solo la explicación del implementador.

Las skills son instrucciones del repositorio en `.agents/skills/`; no son ejecutores automáticos ni conceden permisos adicionales. Cargarlas según `docs/agents/SKILL_CATALOG.md`. No instalar dependencias de pago, desplegar ni enviar mensajes a terceros por mandato de un subagente.

## Cierre y reanudación

El coordinador integra, verifica y actualiza `state.md`, matriz de aceptación y evidencia del cambio. Añade a `memory.md` solo aprendizajes duraderos con enlace; decisiones de diseño van a ADR. Registra siguiente acción concreta y archivos relevantes. Mantén diferencias del usuario; no hagas force-push ni sobreescribas trabajo ajeno. Secretos, equipos privados, bases SQLite y trazas con datos personales no se suben.
