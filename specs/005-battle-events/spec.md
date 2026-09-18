# SPEC-005 — BattleState + Events

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S08, REQ-S43, REQ-S44, REQ-S45. Dependencias: SPEC-001, SPEC-002.

## Objetivo y entrega

BattleState reconstruible, eventos confirmados, SQLite transaccional, parser propuesto y undo.

## Comportamientos que deben conservarse

- REQ-S08 (original §8): El rival mantiene observaciones separadas de posibles sets/items/abilities/moves/SP/Megas.
- REQ-S43 (original §43): Parser textual genera eventos propuestos y requiere confirmación antes de persistir.
- REQ-S44 (original §44): Eventos de los 13 tipos listados reconstruyen estado y soportan undo sin edición arbitraria.
- REQ-S45 (original §45): SQLite conserva teams, battles, battle_events, meta_snapshots, pokemon_sets, calculations y recommendations.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Doble envío, revisión vieja, batch inválido, texto ambiguo, corrección y replay con versiones ausentes.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-005-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then replay reproduce estado/beliefs; commandId duplicado no duplica daño; parser sin confirmar no escribe.

AC-005-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-005-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Secuencias de eventos con snapshots y hash del estado esperado.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.
