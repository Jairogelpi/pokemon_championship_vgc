# Convenciones

## Documentación y trazabilidad

Documentación explicativa en español; identificadores, tipos y código en inglés. Raíz: `AGENTS.md`, `memory.md`, `state.md`, `conventions.md`. Documentos temáticos en mayúsculas; directorios y slugs kebab-case. No duplicar versiones por capitalización.

IDs: `REQ-S00`…`REQ-S61` conservan correspondencia con secciones originales; `AC-V1-01`…`AC-V1-34` son aceptación final; `SPEC-001`…`SPEC-016`, tareas `T001`, ADR `ADR-0001`, preguntas `Q-001`. Criterios detallados dentro de cada spec usan `AC-001-01`. Referenciar IDs en tests y cambios. Si se descompone un requisito, usar sufijos y mantener el padre.

Estados spec: DRAFT → READY → IMPLEMENTING → VERIFIED; BLOCKED cuando falta evidencia, SUPERSEDED con enlace. `VERIFIED` requiere evidencia; un documento existente no lo implica. ADR: proposed, accepted, superseded; no reescribir retrospectivamente el motivo histórico.

## Código previsto

TypeScript strict. Zod valida límites HTTP, archivos, herramientas y datos upstream; núcleo usa tipos propios. Dependencias hacia dominio, nunca al revés. Funciones puras para reglas/cálculos/reducer; tiempo y RNG inyectados. Prohibir `any` injustificado y errores silenciados. No usar `Math.random()` ni reloj implícito dentro de motores reproducibles.

IDs canónicos para species/form/move/item; instanceId para un Pokémon en batalla. SP no se convierten a EV por asumir equivalencia. HP propio exacto; HP rival observado en porcentaje/intervalo no se convierte a entero exacto sin evidencia. Todos los números probabilísticos en [0,1]; heurísticas etiquetadas como scores.

Errores tipados y visibles; no devolver datos inventados para completar UI. Claves de cache incluyen contexto semántico y versiones; no cachear solo especie+move.

## Git y validación

Ramas sugeridas `feat/001-domain-data`, `fix/...`, `docs/...`. Commits pequeños con propósito y spec; PR explica problema, comportamiento, pruebas y límites. No forzar merges por tests saltados. Lockfile único, versiones fijadas al seleccionar herramientas; cambios de dependencias se validan con documentación primaria vigente.

Comando disponible hoy: `python3 scripts/validate_docs.py`. SPEC-001 deberá crear y comprobar scripts reales `typecheck`, `lint`, `test`, `test:integration` y `build`; hasta entonces no ejecutar nombres supuestos como si existieran. Tests golden incluyen fuente, ruleset, condiciones y resultado independiente, nunca salida del propio motor como único oráculo.

## Estado y datos

Un coordinador escribe estado/memoria/trazabilidad. Worker no cambia contratos compartidos sin avisar al coordinador. SQLite y credenciales locales se excluyen de Git. Fixtures públicos mínimos, sintéticos o con permiso; no reutilizar datasets sin revisar su licencia.
