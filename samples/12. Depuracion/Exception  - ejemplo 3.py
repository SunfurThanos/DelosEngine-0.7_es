# coding: utf-8

delos.ignoreError = True # los mensajes del error no se mostraran en pantalla

mensaje = """File "$file$", line $line$
     Tipo de error "$type$": ($error$)
     Codigo involucrado: $code$
     Linea del error: $line$
     Linea de depuracion: $debug$

"""

try:
  # (x, 0.4).joins
  (0.00062, 0.4).joins
except Exception:
    mensaje = debug.error(mensaje, False)
    "registros de errores.txt".path.save(mensaje).close()


"""

Esto permite capturar los mensajes de error, para entre otras cosas poder guardarlos en un archivo externo y tener un registro de los errores de nuestras aplicaciones.

"""
