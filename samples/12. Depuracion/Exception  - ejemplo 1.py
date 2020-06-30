# coding: utf-8

mensaje1 = """File "$file$", line $line$
     Tipo de error "$type$": $error$
     Codigo involucrado: $code$
     Linea del error: $line$
     Linea de depuracion: $debug$"""

mensaje2 = """File "$file$", line $line$
     Error desconocido: $error$
     Codigo involucrado: $code$
     Linea del error: $line$
     Linea de depuracion: $debug$"""

try:
  (x, 0.4).joins
  # (0.00062, 0.4).joins
except Exception:
    if debug.ExceptionType == AttributeError: # detecta el tipo de error
        debug.error(mensaje1, False) # imprimir error sin salir del código
    else:
        debug.error(mensaje2) # imprime error y salir del código

print ("fin de codigo :)")


"""

Esto permite capturar una "Exception" de una manera productiva y altamente personalizable :)

"""
