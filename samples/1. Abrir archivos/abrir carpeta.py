# coding: utf-8

# directorio a abrir
directorio = __file__.path.dir.path.normalize

#-------------------------------------------------------------------------

# abriendo directorio, con el explorador de archivos predeterminado del sistema
if not directorio.path.open.dir():
    print ("Sorry no se pudo abrir la carpeta")
