# coding: utf-8

carpeta = r"C:\Users\Sunfur studio\Pictures"

if not carpeta.path.isdir:
	exit( "Sorry. la carpeta '{carpeta.path.normalize}' no existe".toF )

#-------------------------------------------------------------------------

for carpeta, archivo in carpeta.path.walkFile:
	if archivo.path.ext == "png":
		print (archivo.path.file)
