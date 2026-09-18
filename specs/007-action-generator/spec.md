# SPEC-007 — Action Generator

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S18, REQ-S19, REQ-S20. Dependencias: SPEC-001, SPEC-005.

## Objetivo y entrega

Enumeración y validación de pares de acciones, targets, switches y Mega.

## Comportamientos que deben conservarse

- REQ-S18 (original §18): Generador combina acciones de ambos slots: ataques/objetivos, Protect, switches y Mega con ataque.
- REQ-S19 (original §19): Legalidad verifica vivo, moves, targets, switches, colisiones, Mega, Fake Out, locks, Taunt, Encore, Disable y status.
- REQ-S20 (original §20): Preview aplica la restricción Mega del ruleset activo sin asumir prohibición universal de dos piedras.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Dos switches a una reserva, KO, Taunt/Encore/Disable/locks, move sin uso disponible, targets spread/self.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-007-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then todas las acciones generadas son válidas y no se pierden opciones legales en fixtures exhaustivos pequeños.

AC-007-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-007-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Tablas de acciones admitidas y rechazadas bajo ruleset de prueba y real auditado.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.

## Cobertura detallada obligatoria

Antes de READY y de VERIFIED, revisar [DETAILED_COVERAGE](../../docs/quality/DETAILED_COVERAGE.md): §18 (REQ-S18-xx), §19 (REQ-S19-xx), §20 (REQ-S20-xx). Asignar todos los subrequisitos y miembros de sus enumeraciones a aceptación/tests; no basta con los tres criterios iniciales resumidos. La fuente completa sigue siendo referencia para ejemplos y casos límite.
