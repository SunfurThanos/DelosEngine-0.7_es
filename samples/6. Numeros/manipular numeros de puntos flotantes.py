# coding: utf-8

variable = 0.438384223432  # string, float, int

print (variable.float(2))  # convierte y manipula numeros de puntos flotantes

#-------------------------------------------------------------------------

variable = 10000000096  # string, float, long

# le inserta a una cadena de digitos las unidades de mil (numero de digito en grupo), obteniendo como resultado puntos flotantes con presicion refinada
print (variable.xfloat())
