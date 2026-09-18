# SPEC-016 — Replay + debugging

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S00, REQ-S46, REQ-S48, REQ-S53, REQ-S58, REQ-S59, REQ-S61. Dependencias: SPEC-015.

## Objetivo y entrega

Replay/debug con turnos críticos, decisiones, alternativas y errores; cierre completo V1.

## Comportamientos que deben conservarse

- REQ-S00 (original §0): El recorrido equipo→preview→batalla→recomendación cubre las 20 capacidades del objetivo.
- REQ-S46 (original §46): Replay reconstruye batalla y analiza decisiones, alternativas, predicciones, sets y errores.
- REQ-S48 (original §48): Los once endpoints originales tienen entradas, salidas, errores y pruebas de contrato.
- REQ-S53 (original §53): Tests unitarios, integración de turno y golden independientes cubren motores.
- REQ-S58 (original §58): Las 16 fases se conservan con dependencias y criterios de salida explícitos.
- REQ-S59 (original §59): Los 34 criterios finales tienen prueba/evidencia y no se aprueban solo por disponer de UI.
- REQ-S61 (original §61): El flujo end-to-end conserva estado, belief, simulación y búsqueda y justifica decisiones con evidencia.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Versiones antiguas, undo, datos faltantes, recommendation tomada distinta a real y feedback contradictorio.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-016-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then reconstrucción reproducible y análisis separado de recalcular con motor nuevo; 34 AC y requisitos tienen evidencia real.

AC-016-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-016-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Batallas golden completas, recomendación registrada y hechos reales diferenciados.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.
