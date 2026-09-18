# SPEC-008 — Meta Engine

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S11, REQ-S12. Dependencias: SPEC-001.

## Objetivo y entrega

Meta snapshots versionados y arquetipos con usage/sets/partners/leads y scores.

## Comportamientos que deben conservarse

- REQ-S11 (original §11): MetaEngine expone usage, moves, items, abilities, partners, leads, sets y arquetipos con snapshot identificado.
- REQ-S12 (original §12): Arquetipos devuelven enablers, abusers y confidence etiquetada como score interno.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Snapshot incompatible, stale, sin datos, source failure y varios arquetipos simultáneos.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-008-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then recomendación identifica snapshot; confidence no se etiqueta probabilidad científica; fallo usa stale o unknown.

AC-008-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-008-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Snapshot pequeño con procedencia y equipos para modos TR/Tailwind/Rain/Sun/Sand/terrain/setup/balance/offense.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.

## Cobertura detallada obligatoria

Antes de READY y de VERIFIED, revisar [DETAILED_COVERAGE](../../docs/quality/DETAILED_COVERAGE.md): §11 (REQ-S11-xx), §12 (REQ-S12-xx). Asignar todos los subrequisitos y miembros de sus enumeraciones a aceptación/tests; no basta con los tres criterios iniciales resumidos. La fuente completa sigue siendo referencia para ejemplos y casos límite.
