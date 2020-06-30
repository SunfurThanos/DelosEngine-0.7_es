# coding: utf-8

# creando archivo para nuestro ejemplo
archivo = "archivo de remplazo.txt"
archivo.path.save("hola mundo\nfin de archivo xD").close()

#--------------------------------------------------------------------------------------------------

print ([archivo.path.read()])

#--------------------------------------------------------------------------------------------------

# remplazando texto
SAVE = archivo.path.save(mode="+")

SAVE.cursor(5) # saltar en la posicion 5 de memoria
SAVE.save(b"mundi") # sobre-escribir 5 bytes

# visualizando los cambios realizados
print (SAVE.read(5, 5).close())

#--------------------------------------------------------------------------------------------------

print ([archivo.path.read()])
