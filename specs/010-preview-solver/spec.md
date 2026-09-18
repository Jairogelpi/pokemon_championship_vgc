# SPEC-010 — Preview Solver

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S35, REQ-S36, REQ-S49. Dependencias: SPEC-002, SPEC-003, SPEC-004, SPEC-007, SPEC-008, SPEC-009.

## Objetivo y entrega

PreviewSolver: pick-4, lead/back, arquetipos/Megas/amenazas/planes con evidencia.

## Comportamientos que deben conservarse

- REQ-S35 (original §35): Preview enumera 15 pick-4 y seis leads por selección antes de filtros; evalúa matchups y planes.
- REQ-S36 (original §36): Salida distingue selección, lead, back, modos rivales y plan apoyado en evidencia.
- REQ-S49 (original §49): Preview acepta equipo propio persistido y seis rivales y devuelve todos los campos del original.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

No selección legal, restricciones Mega variables, sets desconocidos, slots ordenados si mecánica lo exige.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-010-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then devuelve 4 únicos y lead/back disjuntos legales; filtra por ruleset y explica riesgos sin certeza rival inventada.

AC-010-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-010-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Equipo de seis con 15 combinaciones y 6 pares de lead por cuatro antes de filtros.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.

## Cobertura detallada obligatoria

Antes de READY y de VERIFIED, revisar [DETAILED_COVERAGE](../../docs/quality/DETAILED_COVERAGE.md): §35 (REQ-S35-xx), §36 (REQ-S36-xx), §49 (REQ-S49-xx). Asignar todos los subrequisitos y miembros de sus enumeraciones a aceptación/tests; no basta con los tres criterios iniciales resumidos. La fuente completa sigue siendo referencia para ejemplos y casos límite.

## Evaluación completa del preview

AC-010-04: El evaluador considera matchups, speed, coverage, defensive switching, archetypes, opponent leads, Mega choice y win conditions, con contribuciones o explicación trazables. Validar con escenarios que distingan alternativas, no solo número de combinaciones legales.
