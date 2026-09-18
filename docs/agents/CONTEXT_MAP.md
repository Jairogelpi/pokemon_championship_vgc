# Mapa de carga de contexto

Carga inicial: `AGENTS.md` + `state.md` + `memory.md` + `conventions.md`. Luego la fila aplicable; no leer todo el repositorio por defecto.

| Trabajo | Contexto adicional mínimo |
|---|---|
| Definir producto/spec | VISION, SCOPE, REQUIREMENTS relevantes, original solo secciones citadas, OPEN_QUESTIONS |
| Datos/reglas | SPEC-001, UPSTREAM, DOMAIN_MODEL, INV-001/004, skill champions-research |
| Daño/speed | SPEC-003/004, modelo, contratos, golden strategy, Q-001/008 |
| Eventos/turnos | SPEC-005/006, DATA_FLOW, invariantes, ADR-0003, Q-004/012 |
| Legalidad/preview | SPEC-007/010, ruleset auditado, restricciones Mega, original §§18–20/35–36 |
| Beliefs/search | SPEC-008/009/011/012, incertidumbre, Q-003/005/010/011 |
| API/DB/LLM/UI | Spec de fase, API_CONTRACTS, SYSTEM_CONTEXT y fallos/invariantes pertinentes |
| Review/cierre | Spec, diff, verificación, aceptación vinculada, traceability; no todo el historial |

## Compactación y continuidad

El coordinador guarda tarea actual, cambios, pruebas, bloqueos y siguiente acción en state. Datos estables nuevos van a memory con fuente; decisiones a ADR; logs a verificación. Reanudar comprobando Git y pruebas, sin confiar solo en un resumen. Una nota de memoria nunca anula la fuente o una decisión posterior.

## Autoridad de conocimiento

Código/tests muestran estado implementado; requisitos muestran intención. Si difieren, existe deuda o defecto, no una autorización implícita para borrar el requisito. Fuentes mecánicas verificadas resuelven ejemplos dudosos mediante documentación explícita.
