# SPEC-014 — LLM tool layer

Estado: DRAFT. Implementación: PENDING. Fuente: REQ-S37, REQ-S38, REQ-S39. Dependencias: SPEC-013.

## Objetivo y entrega

Herramientas LLM con provider abstraction OpenAI/Anthropic/Gemini/local y claims con provenance.

## Comportamientos que deben conservarse

- REQ-S37 (original §37): Herramientas LLM cubren los diez nombres del original y no dan acceso directo de escritura al estado.
- REQ-S38 (original §38): Contrato LLM obliga a herramientas, KNOWN/INFERRED/UNKNOWN y evidencia; no inventa datos o reglas.
- REQ-S39 (original §39): Cada claim tiene provenance; afirmaciones sin respaldo no aparecen como hechos.

Consultar el [original](../../docs/source/V1_SPEC_ORIGINAL.md) para todos los subcasos y la [matriz](../../docs/quality/TRACEABILITY.md) para cierre. Esta lista no sustituye esos detalles.

## Contratos y casos límite

Tool inválida, texto sin evidencia, inyección, timeout, modelo no disponible, intento de escritura directa.

Consultar [modelo](../../docs/architecture/DOMAIN_MODEL.md), [API](../../docs/architecture/API_CONTRACTS.md) e [invariantes](../../docs/architecture/INVARIANTS.md). Concretar schemas y puertos propios antes de READY; no tratar pseudocódigo como contrato compilable.

## Aceptación inicial

AC-014-01: Given entradas válidas bajo versiones fijadas, When se ejecuta el caso de uso, Then funciona sin LLM; record_observation no confirma; get/calc/search devuelven evidencia y claims no sustentados se rechazan.

AC-014-02: Given un caso inválido de los enumerados arriba, When se procesa, Then se obtiene error/unknown explícito sin mutar información real ni inventar valores.

AC-014-03: Given iguales entradas y versiones (y seed cuando aplique), When se repite/reconstruye, Then el resultado de dominio es reproducible; IO y tiempos no contaminan la lógica.

## Plan TDD y evidencia

Fixtures: Provider falso determinista más pruebas de contrato de adaptadores cuando credenciales estén disponibles.

Antes de implementar, descomponer los comportamientos en tests unitarios/contrato/integración/golden pertinentes. Ejecutar RED→GREEN→refactor y registrar comandos/resultados. Evidencia de producto hoy: **NOT RUN**.

## Activación y siguiente paso

Resolver preguntas relevantes de [OPEN_QUESTIONS](../../docs/planning/OPEN_QUESTIONS.md); crear proposal/design/tasks/verification al comenzar la fase. No introducir capacidades V2+ para satisfacer una fase V1.
