# SPEC-012 — Search Engine

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S30, REQ-S31, REQ-S32, REQ-S33. Dependencias: SPEC-011.

## Objetivo y entrega

Expectiminimax limitado, evaluador contextual y métricas de riesgo.

## Comportamientos que deben conservarse

- REQ-S30 (original §30): Búsqueda expectiminimax limitada soporta profundidad por defecto 2 y opcional 3 con semántica ply definida.
- REQ-S31 (original §31): Evaluador incluye material, posición, speed, presión, defensa, campo, setup, información y penalizaciones de riesgo.
- REQ-S32 (original §32): Valor de preservar un Pokémon depende de amenazas y condiciones de victoria, no solo HP.
- REQ-S33 (original §33): Líneas exponen expectedValue, worst/bestCase, variance, koRisk, doubleKOProbability y posición posterior.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Horizon effects, presupuesto agotado, empate, pruning agresivo y líneas de alto riesgo.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-012-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then depth=2 por defecto, 3 opcional según definición documentada; score no solo HP; reporte de horizonte real y riesgos.

AC-012-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-012-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Árboles de juguete con elección esperada independiente y escenarios con win condition contextual.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.
