# Diseño SPEC-001

Estado: propuesta técnica, pendiente de auditoría y selección de versiones.

## Límites

`packages/domain/src/` contiene tipos/esquemas y puertos. Si Zod se usa en dominio, mantenerlo como validación pura sin IO; el dominio no importa JSON upstream, HTTP ni ORM. `packages/champions-data/src/adapters/champions_agent/` normaliza datos verificados. Manifest identifica revision/licencia/hash/ruleset y capacidades soportadas.

Contratos mínimos: RulesetRef, EntityId/InstanceId, StatPointSpread, ExactHP/ObservedHP, StoredTeam, PokemonState, SideState, OpponentSideState, FieldState, BattleState, BattleEvent, Action/ActionPair, MetaSnapshotRef y EvidenceRef. Definir desconocido explícito; no `undefined` que alternativamente signifique no item o item no revelado.

Puertos: DexRepository (lookup por ID), RulesetProvider (restricciones/soporte), TeamLegalityValidator y ActionLegalityValidator (resultado con reasons/unsupported). No implementar mecánicas no verificadas en un schema genérico. Dejar cálculos detrás de puertos propios de fases posteriores.

## Versiones y fixtures

Fijar versiones después de consultar documentación oficial y compatibilidad. ADR para gestor/ORM. Manifest de fixtures contiene input source/ruleset/hash y esperado independiente. Datos sintéticos usan `test-ruleset`, nunca se publican como Champions legal.

## Pruebas

Roundtrip de datos exactos y parciales; validación cardinalidad/HP/IDs; desconocido vs ausente; adapter mapping sin pérdida; rechazo/unsupported de regla desconocida. Verificar que las importaciones del domain no apuntan a adaptadores/apps/persistencia.
