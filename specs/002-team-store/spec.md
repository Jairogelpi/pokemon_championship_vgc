# SPEC-002 — Nuestro Team Store

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S07. Dependencias: SPEC-001.

## Objetivo y entrega

StoredTeam completo persistido/importado, listado y validación contra ruleset.

## Comportamientos que deben conservarse

- REQ-S07 (original §7): Se almacena equipo exacto de seis con forma, objeto, habilidad, naturaleza, SP, moves y stats sin inferir faltantes.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Menos/más de seis, datos faltantes, duplicados según reglas, SP/moves ilegales, fallo transaccional.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-002-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then guardar y recargar conserva cada campo y estadísticas; entrada inválida no crea equipo parcial.

AC-002-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-002-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Equipo sintético válido por ruleset de prueba y equipo real aportado cuando esté disponible.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.

## Cobertura detallada obligatoria

Antes de READY y de VERIFIED, revisar [DETAILED_COVERAGE](../../docs/quality/DETAILED_COVERAGE.md): §7 (REQ-S07-xx). Asignar todos los subrequisitos y miembros de sus enumeraciones a aceptación/tests; no basta con los tres criterios iniciales resumidos. La fuente completa sigue siendo referencia para ejemplos y casos límite.
