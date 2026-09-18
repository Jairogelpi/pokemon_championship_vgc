# SPEC-015 — Web UI

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S40, REQ-S41, REQ-S42. Dependencias: SPEC-005, SPEC-010, SPEC-013, SPEC-014.

## Objetivo y entrega

Web Next/React con equipo, preview, battle board, entrada manual/texto, riesgos/evidencia/simular/alternativas.

## Comportamientos que deben conservarse

- REQ-S40 (original §40): UI de batalla muestra turno/campo/HP/reservas/acción/riesgo y permite simulación y alternativas.
- REQ-S41 (original §41): UI preview recibe seis propios/seis rivales y presenta arquetipos/Megas/lead/back/amenazas/win conditions.
- REQ-S42 (original §42): Entrada manual soporta move, target, HP, switch, Mega y Protect de forma rápida.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Ambigüedad de parser, HP incompleto, KO/reemplazo, requests tardías, errores y modo sin LLM.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-015-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then usuario registra move/target/HP/switch/Mega/Protect y confirma; UI distingue unknown/stale/unverified y no duplica reglas.

AC-015-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-015-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Flujo UI completo con estado conocido y fixtures de API versionada.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.
