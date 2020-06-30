# coding: utf-8

# NOTA : En este ejemplo se muestra como pasar N argumentos de una parte del codigo a otro ####

#--------------------------------------------------------------------------------------------------

def salir_aplication(argumentos):

    globals().join(argumentos)

    print (zipfile)
    print (shutil)
    print (sys)
    print (tempfile)
    print (saludo)
    print (despedida())

#--------------------------------------------------------------------------------------------------

def inciando_aplication():

    def despedida():
        return "vale vale, xD"

    import shutil
    import sys
    import tempfile
    import zipfile

    saludo = "hola mundo"
    argumentos = locals() # "globals" or "locals"
    salir_aplication(argumentos)

#--------------------------------------------------------------------------------------------------

# pasando los argumentos a una determinada función
inciando_aplication()



"""

### Pasar solo objetos de tipo -> módulos ###
>> argumentos = locals().packModules()


### Pasar solo objetos de tipo -> función ###
>> argumentos = locals().packFunctions()


### Pasar solo objetos de tipo -> string ###
>> argumentos = locals().packString()


### Pasar solo objetos de tipo -> int ###
>> argumentos = locals().packInt()


### Pasar solo objetos de tipo -> (LONG) ###
>> argumentos = locals().packLong()


### Pasar solo objetos de tipo -> float ###
>> argumentos = locals().packFloat()

"""
