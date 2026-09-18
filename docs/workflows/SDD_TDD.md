# Flujo SDD + TDD

## 1. Explorar

Leer tarea y secciones originales, inspeccionar repositorio y fuentes necesarias. Identificar contratos existentes, incógnitas, soporte upstream, licencias y riesgos. Resultado: evidencias y límites, no código especulativo.

## 2. Proponer y especificar

Crear `specs/NNN-slug/` con `proposal.md`, `spec.md`, `design.md`, `tasks.md`, `verification.md` cuando la fase esté próxima. Las fases lejanas empiezan con spec DRAFT. Definir problema, alcance/no alcance, requisitos fuente, entradas/salidas, errores, incertidumbre y casos Given/When/Then. Registrar ADR si cambia una decisión estructural.

READY requiere: aceptación comprobable, dependencias disponibles o separadas, contrato preciso y ninguna regla inventada. Revisar las secciones correspondientes de `docs/quality/DETAILED_COVERAGE.md`; asignar todos sus subrequisitos y miembros de listas a tareas/tests. Para VERIFIED, aportar evidencia por subrequisito; los criterios resumidos de la spec no bastan. No pedir aprobación para detalles rutinarios ya autorizados; cambios de alcance y decisiones de producto no resueltas se consultan. Estado READY es una revisión técnica, no aprobación externa ficticia.

## 3. Diseñar y dividir

Definir interfaces y límites de escritura; tareas pequeñas con archivos, dependencias, tests y salida. Coordinador asigna roles/skills y exige el contrato compartido antes de paralelizar consumidores. Un worker no amplía su alcance unilateralmente.

## 4. TDD por comportamiento

- RED: escribir un test a partir de aceptación/oráculo; ejecutar y registrar fallo por comportamiento ausente. Un fallo de import/dependencia no demuestra la lógica requerida.
- GREEN: mínimo cambio que satisface comportamiento sin hardcodear fixtures ni inventar datos.
- REFACTOR: limpiar conservando tests; volver a ejecutar pruebas afectadas.
- Casos límite: errores, incertidumbre, determinismo, aislamiento y reglas negativas cuando el cambio los afecte.

No exigir commits separados para RED si no conviene, pero conservar comando, resultado y caso del ciclo en `verification.md`. No inventar logs retroactivos. Tests de contrato no sustituyen tests de efectos reales; `ok` sin persistir/calcular es un fallo.

## 5. Integrar y verificar

Revisar cambios, tests unit/integration/golden pertinentes, typecheck/build según paquete y regresiones afectadas. LLM y red se simulan en tests reproducibles, pero un mock no acredita compatibilidad upstream. Un golden no deriva su esperado del motor bajo prueba. Revisor comprueba el diff y reproduce los criterios críticos con información suficiente.

## 6. Cerrar

Actualizar verificación, trazabilidad, aceptación, estado y decisiones. Marcar VERIFIED solo si pasa aceptación y están descritos límites reales. Una fase puede estar parcial o bloqueada. El estado final V1 exige todos los 34 AC y los requisitos completos; no se infiere de que las 16 carpetas existan.

## Evidencia mínima de un handoff

Task/spec/REQ, base commit, archivos, comportamiento cambiado, comandos ejecutados, resultados, fixture y procedencia, limitaciones, preguntas y próximo paso. No pegar miles de líneas de logs en state; enlazar la evidencia pertinente.
