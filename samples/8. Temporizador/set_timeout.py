# coding: utf-8

# NOTA : esta herramienta esta inspirada en la función "setTimeout" de JavaScript

#--------------------------------------------------------------------------------------------------

#### ejecutar función en (0.4s) segundos ####

def funcion_ejemplo(numeroA, numeroB):
    print (numeroA * numeroB)

numeroA = 10
numeroB = 42
instancia = set_timeout(0.4, funcion_ejemplo, numeroA, numeroB)

# instancia.cancel() # cancelar alarma

#--------------------------------------------------------------------------------------------------

#### ejecutar función en (0.8s) segundos, usando un (@decorator) ####

class ClassName(object):

    @Timeout(0.8)
    def funcion(self):
        print ("hola mundo")

clase = ClassName()
clase.funcion()

#--------------------------------------------------------------------------------------------------

#### ejecutar una función cada (0.54s) segundos ####

def ejemplo_final(ronda):
    ronda.conteo += 1
    print ("hola : %s" % ronda.conteo)

    if ronda.conteo == 4:
        return False # sale de la alarma

    return True # repite la alarma

ronda = NameSpace()
ronda.conteo = 0
instancia = set_timeout(0.54, ejemplo_final, ronda)
