# ADR-0004 — Reutilización upstream mediante adaptadores

Estado: accepted (2026-09-18), derivado de §2.

## Contexto

Se quiere aprovechar código/datos existentes sin importar acoplamientos o mecánicas incompatibles.

## Decisión

Auditar licencia/capacidad/revisión, fijar versiones y mapear a tipos internos. Smogon no se modifica in-place; patches en wrapper.

## Alternativas consideradas

Copiar todos los datasets; fork completo sin necesidad; dependencia flotante en runtime.

## Consecuencias

Compatibilidad inicial puede estar bloqueada; mantener matriz de soporte. Dos motores derivados del mismo origen no aportan independencia total.

## Verificación

Contrato de adaptador y golden con referencia externa conocida.
