# Auditoría de cobertura de la spec inicial

Fecha: 2026-09-18. Baseline revisada: `535f5c70b6de1b59cdd8c473830c41ca6c68fbe5` (main antes de esta revisión). Revisión por el mismo agente; no independiente.

## Resultado y límites

La fuente original estaba conservada íntegra; las 62 secciones y 34 criterios V1 estaban enlazados. Eso acreditaba preservación y cobertura por sección, **no un desglose completo de aceptación**. La segunda lectura contrastó fuente, requisitos, specs, alcance, contratos y estrategia de pruebas.

Se detectaron detalles demasiado comprimidos en documentos derivados y una ambigüedad que podía reducir el alcance RNG. No se encontró una sección completa desaparecida. Se corrigen los puntos siguientes; no se certifican mecánicas ni código, que siguen sin implementar.

| Hallazgo | Corrección |
|---|---|
| §0: opciones de recomendación agregadas sin tests concretos | SPEC-013 explicita double target, setup, speed control, posicionamiento y demás acciones |
| §§5–8, 11, 16: campos/enums resumidos | Desglose de todos los campos listados, snapshot y variantes de clima/terreno; aceptación adicional en SPEC-001 |
| §9: familias de evidencia incompletamente enumeradas en SPEC-009 | Lista completa y suite por familia, incluidas inmunidades, boosts y switches |
| §21: referencia general a 15 responsabilidades | Enumeración completa; se mantiene Q-004 para verificar el orden real |
| §22: riesgo de interpretar modos como solo una interfaz o aplazables | EXPECTED/WORST_CASE/MONTE_CARLO conservados como capacidades; ownership SPEC-006/011/012 y aceptación de uso real |
| §§29, 31–32, 35: factores agregados | Factores completos de plausibilidad, score, penalizaciones, valor KO y preview |
| §§40–42, 51: detalles UX poco visibles | Contadores, posición esperada, leads rivales/propios, controles grandes, slider y objetivos temporales explícitos |
| Gate genérico por fase | Cada spec enlaza subrequisitos y exige evidencia por cada uno antes de VERIFIED |

## Cobertura entregada

- Fuente idéntica byte a byte al adjunto; SHA-256 documentado en [PROVENANCE](../source/PROVENANCE.md).
- 62 secciones vinculadas a sus specs, sin eliminar originales ni ejemplos.
- 177 comprobaciones en [DETAILED_COVERAGE](DETAILED_COVERAGE.md). Algunas agrupan campos o miembros de una lista; el gate obliga a revisar cada miembro.
- Los 34 criterios originales siguen íntegros en [V1_ACCEPTANCE](V1_ACCEPTANCE.md).
- Las 16 fases, cinco referencias upstream, once endpoints, diez herramientas LLM, siete familias golden y diez exclusiones V2+ quedan explícitos.

## Ambigüedades que siguen abiertas

Legalidad/datos y ejemplos de especies, inferencia Protect/Choice, orden de efectos, definición ply, oráculos y condiciones de benchmark requieren investigación antes del código. Están en OPEN_QUESTIONS. Preservar un ejemplo no equivale a certificar que su mecánica sea correcta; resolver una duda no autoriza recortar una capacidad.

## Verificación

Ejecutado `python3 scripts/validate_docs.py`: PASS para SHA-256, 62 secciones, 34 criterios originales, 177 comprobaciones detalladas, enlaces, 16 specs y 8 skills. En copias temporales aisladas, el validador rechazó la pérdida de la sección detallada REQ-S22 y la eliminación del enlace de cobertura en SPEC-012. El original no se modificó. El validador comprueba integridad/estructura/enlaces y asignación del desglose; no demuestra por sí mismo completitud semántica ni corrección funcional.
