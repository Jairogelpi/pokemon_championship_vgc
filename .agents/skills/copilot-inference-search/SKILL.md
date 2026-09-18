---
name: copilot-inference-search
description: Implementar beliefs, simulación y búsqueda con incertidumbre explícita y sin acceso a información oculta.
---

# copilot-inference-search

Aplicar dentro de este repositorio y del alcance asignado. Las rutas siguientes son relativas a la raíz del repo; localizarla por AGENTS.md. No otorga permisos adicionales ni arranca otros agentes por sí sola.

1. Conservar observaciones separadas; calcular posterior con evidencia trazable y normalización.
2. Probar conjunto vacío, OTHER, observaciones contradictorias y el caso Protect/Choice antes de descartar sets.
3. Generar acciones legales antes de puntuar/prunar; registrar ramas descartadas, masa retenida cuando exista y presupuesto.
4. Definir ply antes de search; modelar KO discreto además de daño esperado, sin promediar estados imposibles.
5. Entregar riesgo, supuestos y horizonte alcanzado; confidence heurística no es probabilidad calibrada.

## Referencias a cargar según tarea

- [docs/architecture/DOMAIN_MODEL.md](../../../docs/architecture/DOMAIN_MODEL.md)
- [docs/planning/OPEN_QUESTIONS.md](../../../docs/planning/OPEN_QUESTIONS.md)
- [docs/quality/TEST_STRATEGY.md](../../../docs/quality/TEST_STRATEGY.md)

## Salida

Handoff con tarea, archivos, decisiones, evidencia ejecutada, límites y siguiente acción. Si falta un dato imprescindible, explicitar qué parte bloquea y continuar únicamente las tareas independientes.
