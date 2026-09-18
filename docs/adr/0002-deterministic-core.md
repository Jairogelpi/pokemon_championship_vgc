# ADR-0002 — Núcleo determinista y LLM restringido

Estado: accepted (2026-09-18), heredado de §§1, 37–39, 57.

## Contexto

Las recomendaciones deben justificarse con números y reglas.

## Decisión

Separar capa determinista, beliefs probabilísticos y explicación. Herramientas LLM tipadas; record_observation propone, no confirma.

## Alternativas consideradas

LLM simulando por texto; acoplar proveedor a resolver.

## Consecuencias

Más trabajo en motores y tests, pero fallo LLM admite resultado útil. Cualquier inferencia del LLM se marca y no se trata como evidencia observada.

## Verificación

Tests de aislamiento, timeout, claims sin origen y parser sin confirmación.
