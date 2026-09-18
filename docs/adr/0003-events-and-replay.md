# ADR-0003 — Eventos, estado y ramas aisladas

Estado: accepted en principio (2026-09-18); detalle pendiente SPEC-005.

## Contexto

Estado editable y observaciones duplicadas impiden depurar y deshacer.

## Decisión

Event log durable; reducer determinista; revision e idempotencia; simulación sobre copias; undo reconstruye y conserva auditoría.

## Alternativas consideradas

Sobrescribir estado; borrar último row; registrar simulación como hecho.

## Consecuencias

Necesita esquema de eventos y migraciones/versionado, estrategia concreta de corrección y control de revisiones. No afirmar replay reproducible sin versiones.

## Verificación

Roundtrip/replay, duplicados, batches atómicos, undo y revisión obsoleta.
