# SPEC-006 — Turn Resolver

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S17, REQ-S21, REQ-S22, REQ-S23, REQ-S24, REQ-S27, REQ-S54. Dependencias: SPEC-003, SPEC-004, SPEC-005.

## Objetivo y entrega

TurnResolver determinista con acciones dadas y pipeline mecánico contrastado.

## Comportamientos que deben conservarse

- REQ-S17 (original §17): Resolver recibe estado y acciones de ambos lados y devuelve outcome sin elegir estrategia.
- REQ-S21 (original §21): Resolver cubre las 15 responsabilidades del pipeline; seed e input iguales producen resultado idéntico.
- REQ-S22 (original §22): RNG inyectado; V1 evalúa daño esperado y probabilidades KO. Conservar soporte de EXPECTED, WORST_CASE y MONTE_CARLO en simulación/búsqueda (SPEC-011/012), sin posponer modos ni fallback silencioso.
- REQ-S23 (original §23): Protect cubre protección, excepciones, spread y cadena consecutiva con probabilidad según ruleset.
- REQ-S24 (original §24): Fake Out comprueba entrada, prioridad, terreno, abilities, inmunidades y Protect con condiciones explícitas.
- REQ-S27 (original §27): Switch procesa hazards si legales, entry abilities, clima/terreno, elegibilidad Fake Out y limpieza de volátiles.
- REQ-S54 (original §54): Golden incluye TR, Psychic Terrain, cambio a Grassy, Intimidate, Protect, Tailwind y Mega con precondiciones.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

KO intermedio, reemplazos, Protect chains, prioridad bloqueada, entrada/cambio de terrain/weather y fin de turno.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-006-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then mismo estado/acciones/seed/versiones produce mismos eventos/outcome; orden de efectos y duraciones correcto.

AC-006-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-006-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Siete familias golden del original §54 con precondiciones y fuente.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.

## Cobertura detallada obligatoria

Antes de READY y de VERIFIED, revisar [DETAILED_COVERAGE](../../docs/quality/DETAILED_COVERAGE.md): §17 (REQ-S17-xx), §21 (REQ-S21-xx), §22 (REQ-S22-xx), §23 (REQ-S23-xx), §24 (REQ-S24-xx), §27 (REQ-S27-xx), §54 (REQ-S54-xx). Asignar todos los subrequisitos y miembros de sus enumeraciones a aceptación/tests; no basta con los tres criterios iniciales resumidos. La fuente completa sigue siendo referencia para ejemplos y casos límite.
