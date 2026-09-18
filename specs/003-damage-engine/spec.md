# SPEC-003 — Damage Engine

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S13, REQ-S14, REQ-S55. Dependencias: SPEC-001, SPEC-002.

## Objetivo y entrega

DamageEngine con Smogon wrapper, Champions patches, NCPValidator y discrepancies.

## Comportamientos que deben conservarse

- REQ-S13 (original §13): DamageResult contiene rango, porcentajes, rolls, KO 1/2 hits, modificadores y supuestos.
- REQ-S14 (original §14): Casos compatibles se comparan con NCP; coincidencia marca validación, divergencia registra discrepancy visible.
- REQ-S55 (original §55): Dataset golden de daño compara NCP, Smogon adaptado y referencia esperada; tolerancia cero determinista.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Regla no soportada, inputs insuficientes, divergencia de oráculos, spread/crit/status/campo.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-003-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then devuelve rango/rolls/KO/modifiers/assumptions y dual validation solo cuando verificable; tolerancia cero determinista.

AC-003-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-003-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: tests/golden/damage.json con fuente independiente, versiones, condiciones, rolls y KO.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.
