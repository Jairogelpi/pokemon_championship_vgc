# SPEC-013 — Recommendation Engine

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S34, REQ-S50, REQ-S51, REQ-S52, REQ-S56, REQ-S57. Dependencias: SPEC-010, SPEC-012.

## Objetivo y entrega

Copilot ensambla línea, alternativas, riesgos, supuestos, cálculos, respuestas, trace/cache/fallback.

## Comportamientos que deben conservarse

- REQ-S34 (original §34): Recomendación incluye línea principal, alternativas, confianza, riesgos, supuestos, cálculos y respuestas plausibles.
- REQ-S50 (original §50): Recommend devuelve acciones/objetivos, score/risk/alternatives/explanation/evidence.
- REQ-S51 (original §51): Benchmarks verifican preview<3s, recomendación<2s sin LLM/<5s con LLM y daño típico<100ms bajo condiciones declaradas.
- REQ-S52 (original §52): Cache cubre daño/speed/meta/dex e invalida ante cambios de estado/campo/boosts/ability/item/Mega/spread y versiones.
- REQ-S56 (original §56): Trace registra estado, candidatos, ramas, cálculos, pruning, scores, selección y entrada/salida LLM saneada.
- REQ-S57 (original §57): Fallbacks muestran meta stale, cálculo no verificado, incertidumbre y recomendación sin LLM.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

LLM/meta caído, cálculo divergente, revisión obsoleta, cache context changed y timeout.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-013-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then resultado contiene evidencia asociada al estado y versiones; cumple umbrales medidos o queda explícitamente pendiente.

AC-013-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-013-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Escenarios reproducibles y benchmark con condiciones registradas.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.
