# coding: utf-8

### Posicionar ejecución en el directorio del script. ###

setWorkingDir()

if __file__.path.isfile: print ("si existe")

#--------------------------------------------------------------------------------------------------

### Posicionamiento personalizado.  ###

setWorkingDir("../")

for file in "./".path.listdir():
    print (file)
