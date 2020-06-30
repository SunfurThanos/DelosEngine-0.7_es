# coding: utf-8

Get_ObjectsTypes() # iniciando detectado automático de objetos (static object *ALL)

# permite de una manera mas sencilla y productiva detectar que tipo de objeto es una variable

#-------------------------------------------------------------------------------------------------

def funcion_prueba(self):
    pass

class ClassName1994(object):
    def __init__(self, arg=False):
        super(ClassName1994, self).__init__()
        self.arg = arg

print (funcion_prueba.type)

print (ClassName1994.type)

print (delos.os.type)

print (delos.os.path.type)

print ("hola mundo".type)

print ((1994).type)

print ((False).type)

#-------------------------------------------------------------------------

"""

NOTA : la función "Get_ObjectsTypes()" es necesaria llamarla para establecer que ¡todos los objetos! tengan el método type activado.

**** ¿porque esa función no se activa de forma automática como las demás? ****

la activación automática puede traer problemas graves en un IDE específicamente en complementos de auto completado como (Anaconda, JEDI) entre otros, por ello esta opción se debe activar de forma manual en el "MAIN" de tu aplicación, una vez activada no es necesario volverlo a hacer en ningún otro modulo de tu aplicación.

"""
