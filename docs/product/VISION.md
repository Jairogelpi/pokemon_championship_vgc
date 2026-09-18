# Visión

Ayudar al jugador humano de Champions Doubles a tomar decisiones antes y durante una batalla, con cálculos reproducibles, estado consistente e incertidumbre explícita. El usuario introduce información, recibe cuatro seleccionados/lead/back y luego acciones dobles con alternativas, riesgos y evidencias; juega manualmente y registra lo ocurrido.

El valor no es un chatbot con una calculadora: el sistema conecta estado, sets compatibles, daño, speed, respuestas rivales y simulación. Debe seguir operativo sin LLM. Una buena explicación no compensa una mecánica incorrecta.

Éxito V1: pasar los 34 criterios de [aceptación](../quality/V1_ACCEPTANCE.md), cubrir reglas soportadas con oráculos fiables y cumplir objetivos de latencia con condiciones de medición declaradas. No prometer ganar partidas ni probabilidades científicas a partir de scores heurísticos.

Usuario primario: jugador individual con equipo exacto y seis especies visibles del rival. Datos ocultos se modelan como hipótesis; no se presume conocer el backline ni estadísticas rivales. Fuente: original §§0–1, 59, 61.
