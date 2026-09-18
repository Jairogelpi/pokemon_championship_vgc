# Tareas SPEC-001

Todas PENDING. Coordinador asigna rutas exclusivas antes de delegar.

| ID | Trabajo / rol / skill | Dependencia | Archivos previstos | Salida verificable |
|---|---|---|---|---|
| T001 | Auditar upstream y ruleset; researcher / champions-research | Ninguna | docs/research/UPSTREAM.md y evidencia nueva | URL, fecha, commit, licencias, capacidades y límites; Q-001/002 resueltas o bloqueo concreto |
| T002 | Concretar contratos y aceptación; architect / copilot-design | Modelo inicial; reglas que necesite T001 | design.md, spec.md, contratos asignados | Datos exactos/unknown, puertos y errores definidos; preguntas sin evidencia separadas |
| T003 | Seleccionar versiones y scaffold; engineer / copilot-integration | T002 para límites | manifests, lockfile, configs, apps/packages realmente usados | install reproducible, scripts reales, ADR de herramientas, build/typecheck/tests de base |
| T004 | Escribir y ejecutar RED de dominio; engineer / copilot-engine-tdd | T002/T003 | tests unitarios de domain | Fallos funcionales para cardinalidad, HP, serialización e incertidumbre |
| T005 | GREEN y refactor de dominio | T004 | packages/domain | Tests anteriores pasan sin dependencia de upstream o IO |
| T006 | Adapter Champions con TDD | T001/T005 | packages/champions-data y fixtures asignados | Normalización contrastada, manifest y errores de soporte; sin dataset inventado |
| T007 | Verificación de integración y revisión; reviewer / copilot-verify | T005/T006 | verification.md | Evidencia reproducible, licencias y límites; hallazgos resueltos |
| T008 | Integrar y actualizar estado; coordinator / copilot-orchestrate | T007 | state/memory/traceability/roadmap | Próxima fase y requisitos parciales/completos declarados con exactitud |

T003 puede avanzar sin datos reales, pero T006 y el cierre de fase no. No usar el scaffold como prueba de que los cálculos Champions funcionan.
