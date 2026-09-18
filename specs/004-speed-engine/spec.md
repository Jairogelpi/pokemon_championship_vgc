# SPEC-004 — Speed Engine

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S15, REQ-S25, REQ-S26. Dependencias: SPEC-001.

## Objetivo y entrega

SpeedEngine contextual con prioridad, comparador TR, Tailwind, empates y razones.

## Comportamientos que deben conservarse

- REQ-S15 (original §15): Speed contempla naturaleza, SP, boosts, paralysis, Tailwind, TR, Scarf, abilities, weather, prioridad y campo; devuelve ties y razones.
- REQ-S25 (original §25): TR modifica comparator dentro de prioridad, no stats; ties siguen representados.
- REQ-S26 (original §26): Tailwind afecta cálculo contextual, nunca stats base persistentes.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Empates, modificación temporal, paralysis/Scarf/abilities/weather y distinta prioridad.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-004-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then tR invierte speed dentro de prioridad; Tailwind no altera stats guardadas; tie explícito.

AC-004-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-004-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Casos de speed documentados con SP/nature/stages/campo y referencia.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.
