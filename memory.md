# Memoria del proyecto

Conocimiento estable; progreso en [state.md](state.md), decisiones en [ADR](docs/adr/README.md).

| Hecho / decisión | Procedencia | Estado |
|---|---|---|
| Objetivo: copiloto real Champions Doubles; LLM separado del motor | Spec original §§0–1, 61 | Requisito |
| No recortar estado, inferencia, simulación o búsqueda de la V1 | Spec original §61 | Requisito |
| Next.js/React/TypeScript; Node/TypeScript; SQLite; Zod; Vitest | Spec original §4 | Base solicitada; versiones pendientes |
| Reutilizar upstream por adaptadores, sin acoplar dominio | Spec original §2 | Compatibilidad y licencia pendientes |
| No hay equipo real exacto importado | Spec original §7 contiene solo ejemplo | Pendiente del usuario/dataset |
| Ejemplos de Protect/Choice, Mega y orden de efectos requieren contraste | OPEN_QUESTIONS Q-001–Q-004 | No son reglas verificadas |
| Fuente original conservada byte a byte | docs/source/PROVENANCE.md | SHA-256 `eaf30087a4b49ae6330c735c05d116d8b18e72404ef55377cc6b9e7125852e91` |
| Documentación repartida por responsabilidad y carga selectiva | ADR-0001 | Adoptado para este bootstrap |

## Actualizar esta memoria

Añade fecha, hecho comprobado, referencia y consecuencia. Sustituye hechos obsoletos enlazando la decisión que los revoca. No almacenes logs, tareas terminadas, secretos ni hipótesis como hechos. Las observaciones de batallas pertenecen a la persistencia del producto, no a este archivo.
