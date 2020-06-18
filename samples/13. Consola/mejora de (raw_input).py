# coding: utf-8

# mejora de "raw_input", el soporte de color de texto solo esta disponible para Windows, en otros sistemas el soporte para color es oviado, para mantener la integridad de la herramienta nativa de Python en sus diferentes versiones.

#--------------------------------------------------------------------------------------------------

ROJO = 12
VERDE = 10

while True:
    resultado = raw_input("\n escribe> ", ROJO, VERDE)
    print (console.color("\n " + resultado, ROJO))
    console.color(False)
    print ("\n vale carnal, DelosEngine esta bien CHIDO")
