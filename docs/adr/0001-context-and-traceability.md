# ADR-0001 — Contexto selectivo y trazabilidad

Estado: accepted (2026-09-18), alcance documental.

## Contexto

La spec es extensa y una sesión no debe cargar ni duplicar todo el contexto.

## Decisión

Original inmutable; requirements/traceability como índices, AGENTS como entrada, memory estable y state operativo. Skills/roles cargan referencias por tarea.

## Alternativas consideradas

Un único documento gigante; memoria como log; duplicar instrucciones en cada agente.

## Consecuencias

Más enlaces que mantener; un validador comprueba integridad, cobertura e inexistencia de enlaces rotos. No prueba semántica funcional.

## Verificación

Hash de fuente, 62 REQ, 34 AC y rutas válidas.
