# SPEC-009 — Belief Engine

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S09, REQ-S10, REQ-S47. Dependencias: SPEC-005, SPEC-008.

## Objetivo y entrega

Belief Engine con prior/posterior, evidencia de moves/ability/item/Mega/daño/speed y feedback local.

## Comportamientos que deben conservarse

- REQ-S09 (original §9): Priors y evidencia actualizan pesos normalizados; contradicciones se registran y nunca rellenan certezas falsas.
- REQ-S10 (original §10): El ejemplo de Protect se conserva y se contrasta antes de descartar hipótesis Choice; Q-003 evita codificar una inferencia inválida.
- REQ-S47 (original §47): Feedback local evalúa beliefs sin actualizar automáticamente el meta global con una batalla.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Todos los sets rechazados, evidencia parcial, daño intervalado, Protect con Choice y bajo sample size.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-009-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then posteriores normalizados coherentes; observaciones no se sobrescriben y feedback no cambia meta global.

AC-009-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-009-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Hipótesis controladas con probabilidades esperadas calculadas externamente.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.
