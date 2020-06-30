# coding: utf-8

####### NOTA : disponible solo para Windows #######

# archivo a utilizar
archivo = "../imagen.jpeg".path.normalize
 
#-------------------------------------------------------------------------
 
# abrir el explorador de Windows seleccionando el archivo
if not archivo.path.open.explorer(): print ("Sorry no se pudo abrir el archivo")
