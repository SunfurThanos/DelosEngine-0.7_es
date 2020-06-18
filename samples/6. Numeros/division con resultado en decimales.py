# coding: utf-8

# operación matemática normal
print (999999 / 62)

#--------------------------------------------------------------------------------------------------

# activando decimales en la operación matemática
resultado = Math("999999 / 62")
print (resultado)

# controlando la precisión de decimales en la operación matemática
resultado = Math("999999 / 62", prec=10)
print (resultado)

#--------------------------------------------------------------------------------------------------

# desactivando decimales en la operación matemática
resultado = Math("999999 / 62", float=False)
print (resultado)

#--------------------------------------------------------------------------------------------------

# soporte de "formatstrings"
numero_concurrente = 262
numero_final = 4526
resultado = Math("{numero_concurrente} * 100 / {numero_final}".Format, prec=3)
print ("Progreso de descarga: {resultado} %".Format)

#--------------------------------------------------------------------------------------------------


"""

# NOTA : En versiones anteriores a Python 3, el soporte de decimales para operaciones matemáticas no esta activado de forma automática, ademas en las versiones de Python 3 o superior no puedes controlar de forma sencilla la precisión de los puntos flotantes, esta nueva herramienta "Math" da por solucionado el problema manteniendo la integridad de todas versiones de Python

# prec : Se recomienda poner un valor no mayor a 10 para que sea compatible con todas las versiones de Python, ahora si solo quieres que funcione para Python 3 o superior, puedes colocar valores mas altos.

NOTA : esta herramienta esta inspirada en la funcion "Math" de Javascript xD

"""
