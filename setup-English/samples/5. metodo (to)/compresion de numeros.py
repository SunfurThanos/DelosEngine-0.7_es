# coding: utf-8

##### HIGH compress number ¡util para ciencias de datos, NLP y IA! #####

"""

1. permite comprimir cadenas numericas (int, float, long, string-numbers) a unos pocos bytes

2. el resultado de compresion es ¡constante! sin importar los numeros que compongan cada variante de la cadena numerica, por ende si la cadena tiene solo 4 bytes seran reducidos a los 2 bytes en todas las variantes

"""

#--------------------------------------------------------------------------------------------------

cadena = "1234"
comprimido = cadena.toCompress()
print (comprimido,)

decode = comprimido.toDecompress()
print (decode,)

#--------------------------------------------------------------------------------------------------

# NOTA : siempre dara la misma longitud ¡para todas las N variantes!

cadena = "27128183213212913931"
comprimido = cadena.toCompress()
print (comprimido.len,)

cadena = "0.388489459453435534"
comprimido = cadena.toCompress()
print (comprimido.len,)

#--------------------------------------------------------------------------------------------------

cadena = "123"
comprimido = cadena.toCompress()
print (comprimido.len,)

cadena = "12"
comprimido = cadena.toCompress()
print (comprimido.len,)

#--------------------------------------------------------------------------------------------------

cadena = "-3484324343"
comprimido = cadena.toCompress()
print (comprimido.len,)
