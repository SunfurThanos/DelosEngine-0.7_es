# coding: utf-8

try:
  (0.00062, 0.4).joins
except Exception:
    datos_error = debug.error()
    print (repr(datos_error))

"""

Permite extraer la información detallada del error para usarlo de forma personalizada

#### obtendrás un diccionario con los siguientes valores ####

>> datos_error = debug.error() # extrayendo diccionario
>> print (repr(datos_error))
{
    '$file$'  : archivo "modulo" donde esta el error, 
    '$line$'  : numero de linea donde esta el error
    '$type$'  : tupla con los valores del tipo de error,
    '$error$' : extracto del código del error,
    '$debug$' : numero de linea donde se imprimirá la depuración personalizada del error,
}


"""
