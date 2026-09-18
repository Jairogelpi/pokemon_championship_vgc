# ARD — requisitos de arquitectura

Estado: baseline de requisitos; no certificación de implementación. Decisiones concretas en [ADR](../adr/README.md).

| Driver | Restricción arquitectónica | Verificación |
|---|---|---|
| Exactitud mecánica | Núcleo determinista, ruleset versionado y adaptadores contrastados | Golden independiente, tolerancia cero donde determinista |
| Información parcial | Observaciones separadas de hypotheses; no leer estado oculto verdadero en search | Fixtures de incertidumbre y no filtración |
| Reproducibilidad | Eventos, versiones, seed, algoritmo y config conservados | Replay reproduce hash del estado y resultado |
| Interactividad | Preview<3s; recomendación<2s determinista/<5s con LLM; daño típico<100ms | Benchmark fijando hardware, warm/cold, carga y dataset |
| Funcionamiento local | SQLite; cálculo y recomendaciones básicas sin proveedor LLM | Test offline/LLM failure |
| Evolución | Upstream y LLM detrás de interfaces; dominio sin framework | Tests de contrato y revisión del grafo de dependencias |
| Auditoría | Claims con origen, trace y discrepancias visibles | Recomendación rastreable a estado/datos/cálculos |
| Corrección de entrada | Confirmación, revisión de estado e idempotencia | Duplicados, conflicto de revisiones y undo |

## Restricciones heredadas

Monorepo de original §3, stack de §4, endpoints de §48 y fases de §58. ORM abierto Drizzle/Prisma. No cloud obligatorio, visión artificial ni juego automático. Un motor parcial devuelve soporte limitado explícito, no reglas de otra generación por defecto.

## Riesgos principales

Licencia/disponibilidad upstream; reglas Champions incompletas; NCP y Smogon con origen común; explosión combinatoria; sesgo del meta; ambigüedad de HP rival; orden de efectos; latencia LLM variable. Mitigaciones y preguntas en [OPEN_QUESTIONS](../planning/OPEN_QUESTIONS.md).
