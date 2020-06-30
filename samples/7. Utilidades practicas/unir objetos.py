# coding: utf-8

numeros = 0xCC4336DA  # objetos soportados: int, long, long, list, tuple
print (numeros.join())  # convierte (long) a objeto tipo string (chain::str*)
print (numeros.join(","))

#--------------------------------------------------------------------------

# unir diccionarios

nuevo = {"cometa" : 0x00, "terminator" : 1994}
print ({"dict9": 90, "dict6" : 54}.join(nuevo))
