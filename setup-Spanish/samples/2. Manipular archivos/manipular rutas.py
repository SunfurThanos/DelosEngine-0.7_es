# coding: utf-8

archivo = "manipular rutas.py".path.normalize

#----------------------------------------------------------------------------------------------

print (archivo.path.change_ext("java")) # cambiar extensión del archivo

#----------------------------------------------------------------------------------------------

print (archivo.path.drive) # extraer del archivo el directorio RAIZ (driver) del sistema

print (archivo.path.dir) # extraer el directorio del archivo

print (archivo.path.file) # extraer el (basename) del archivo

print (archivo.path.name) # extraer el nombre del archivo
 
print (archivo.path.ext) # extraer la extensión del archivo

print (archivo.path.size.value) # extraer el peso del archivo en bytes

print (archivo.path.size.info) # extraer información del peso del archivo (BYTE, KB, MB, ...)

#----------------------------------------------------------------------------------------------

print (archivo.path.relative) # convertir ruta del archivo a relativa

print (archivo.path.normalize) # convertir ruta del archivo a absoluta

print (archivo.path.isNormalize) # detecta si la ruta es absoluta

print (archivo.path.isRelative) # detecta si la ruta es relativa

#----------------------------------------------------------------------------------------------

print (archivo.path.isdir) # detectando si el archivo es un directorio

print (archivo.path.isfile) # detectando si es un archivo

print (archivo.path.isExist) # detecta si existe la ruta

#----------------------------------------------------------------------------------------------

print (archivo.path.isnull) # detecta si el archivo esta vació

print (archivo.path.istext) # detecta si el archivo es de tipo texto

print (archivo.path.isbinary) # detecta si el archivo es de tipo binario
