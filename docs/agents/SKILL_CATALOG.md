# Catálogo de skills del repositorio

Ubicación convencional `.agents/skills/<name>/SKILL.md`. Cada skill contiene nombre y descripción para descubrirla y referencias progresivas. El coordinador puede cargarla explícitamente en cualquier runtime; la autodetección depende de la herramienta. No se presupone integración automática ni configuración de proveedor instalada.

| Skill | Cuándo cargarla |
|---|---|
| [copilot-orchestrate](../../.agents/skills/copilot-orchestrate/SKILL.md) | Coordinar tareas SDD y handoffs del Battle Copilot, con dependencias, contexto y límites de escritura. |
| [copilot-spec](../../.agents/skills/copilot-spec/SKILL.md) | Descomponer la spec original del Battle Copilot en aceptación verificable sin perder requisitos. |
| [champions-research](../../.agents/skills/champions-research/SKILL.md) | Auditar reglas, datasets y repos upstream de Champions antes de usarlos como evidencia o dependencia. |
| [copilot-design](../../.agents/skills/copilot-design/SKILL.md) | Diseñar contratos y decisiones del motor Champions manteniendo dominio, proveedores y simulación separados. |
| [copilot-engine-tdd](../../.agents/skills/copilot-engine-tdd/SKILL.md) | Implementar daño, speed, legalidad y resolución determinista de Champions con pruebas y reglas verificadas. |
| [copilot-inference-search](../../.agents/skills/copilot-inference-search/SKILL.md) | Implementar beliefs, simulación y búsqueda con incertidumbre explícita y sin acceso a información oculta. |
| [copilot-integration](../../.agents/skills/copilot-integration/SKILL.md) | Integrar API, SQLite, herramientas LLM y UI del Copilot preservando confirmación y degradación. |
| [copilot-verify](../../.agents/skills/copilot-verify/SKILL.md) | Verificar aceptación, trazabilidad y evidencia del Battle Copilot sin confundir documentación con producto implementado. |

Un agente puede usar más de una skill cuando la tarea cruza límites; mantener un responsable y un alcance de edición. No cargar todas por defecto. La configuración nativa de subagentes de Claude/Codex se podrá añadir cuando se elija runtime y se verifique su formato vigente; los perfiles y handoffs ya son portables.
