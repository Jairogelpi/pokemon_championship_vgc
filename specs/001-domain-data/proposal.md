# Propuesta SPEC-001

Problema: la spec necesita tipos y fuentes estables antes de implementar cálculos, estado y búsqueda. El repo actual solo documenta el producto.

Entregar scaffold TS reproducible y contratos de dominio/datos con adapter auditado y fixtures de procedencia. El esquema puede validar forma estructural sin afirmar legalidad real hasta cerrar Q-001/Q-002. Separar ambos tipos de validación en nombres/resultados.

No implementar aún daño, UI, búsqueda ni copiar datasets completos. Preservar monorepo previsto; crear paquetes cuando tengan contrato/código real, no decenas de carpetas vacías presentadas como módulos terminados.

Salida: decisiones de herramientas fijadas, scripts ejecutables, contratos validados y límites upstream conocidos. Si no hay fuentes accesibles, cerrar solo scaffold/contratos sintéticos y dejar integración real BLOCKED; no declarar SPEC-001 completa.
