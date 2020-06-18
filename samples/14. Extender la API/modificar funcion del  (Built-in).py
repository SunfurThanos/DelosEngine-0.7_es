# coding: utf-8

#### modificar una funcion ya existente del "Built-in" ####

# nueva funcion a utilizar
def nueva_funcion():
    print (delos.sys.version_info[0] == 3)

# detectar si el "Built-in" ya existe
if hasattr(__builtins__, "isPython3"):
    # modificando "Built-in"
    builtin_instance.isPython3 = nueva_funcion

# ejecutando "Built-in" modificado
isPython3()
