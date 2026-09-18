# SPEC-011 — Simulator

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S28, REQ-S29. Dependencias: SPEC-006, SPEC-007, SPEC-009.

## Objetivo y entrega

Simulator y modelo de acciones rivales con pruning/config top-K, RNG y branches aisladas.

## Comportamientos que deben conservarse

- REQ-S28 (original §28): Simulador explora pares propios/rivales y sets ocultos con pruning trazable.
- REQ-S29 (original §29): Modelo rival genera acciones legales, puntúa plausibilidad y permite top-K configurable (ejemplo K=8).

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Explosión de ramas, masa truncada, acciones inválidas, HP esperado frente a KO discreto, modo no disponible.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-011-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then explora pares y sets sin mutar estado real; registra pruning, supuestos, modos soportados y probabilities.

AC-011-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-011-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Árbol pequeño enumerable a mano, seeds repetibles y hidden sets alternativos.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.

## Cobertura detallada obligatoria

Antes de READY y de VERIFIED, revisar [DETAILED_COVERAGE](../../docs/quality/DETAILED_COVERAGE.md): §28 (REQ-S28-xx), §29 (REQ-S29-xx). Asignar todos los subrequisitos y miembros de sus enumeraciones a aceptación/tests; no basta con los tres criterios iniciales resumidos. La fuente completa sigue siendo referencia para ejemplos y casos límite.

## Ramas rivales y modos RNG (responsabilidad compartida REQ-S22)

AC-011-04: plausibilityScore considera meta usage, damage, KO potential, protect, setup, switch synergy, speed control y board position. Pruning ocurre después de generar acciones legales y conserva configuración top-K.

AC-011-05: Simulator ofrece a Search Engine soporte concreto para EXPECTED, WORST_CASE y MONTE_CARLO. EXPECTED conserva probabilidades KO; WORST_CASE explicita conjunto de resultados adversos evaluado; MONTE_CARLO recibe seed y presupuesto de muestras y reporta incertidumbre. Los detalles se concretan antes de READY. Durante construcción puede haber errores de modo no disponible, pero estos no satisfacen el criterio de cierre de ese modo.
