---
name: copilot-verify
description: Verificar aceptación, trazabilidad y evidencia del Battle Copilot sin confundir documentación con producto implementado.
---

# copilot-verify

Aplicar dentro de este repositorio y del alcance asignado. Las rutas siguientes son relativas a la raíz del repo; localizarla por AGENTS.md. No otorga permisos adicionales ni arranca otros agentes por sí sola.

1. Leer spec/diff/fixtures y reproducir criterios críticos con comandos disponibles.
2. Comprobar procedencia de golden y que el esperado no proviene únicamente del motor bajo prueba.
3. Inspeccionar efectos reales: eventos escritos, undo/replay, cambios de estado y soporte de mecánicas; un ok no es suficiente.
4. Reportar casos reproducibles con severidad y límites; no marcar PASS con pruebas omitidas.
5. Actualizar verificación asignada; coordinador actualiza aceptación/state. Declarar si la revisión no fue independiente.

## Referencias a cargar según tarea

- [docs/quality/TEST_STRATEGY.md](../../../docs/quality/TEST_STRATEGY.md)
- [docs/quality/V1_ACCEPTANCE.md](../../../docs/quality/V1_ACCEPTANCE.md)
- [docs/quality/TRACEABILITY.md](../../../docs/quality/TRACEABILITY.md)
- [templates/VERIFICATION.md](../../../templates/VERIFICATION.md)

## Salida

Handoff con tarea, archivos, decisiones, evidencia ejecutada, límites y siguiente acción. Si falta un dato imprescindible, explicitar qué parte bloquea y continuar únicamente las tareas independientes.
