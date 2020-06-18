# coding: utf-8

# creando un NameSpace
def fuct_prueba(): return "hello world"

variable = NameSpace()
variable.x = (0, 2456, 256, 255, 56)
variable.y = (0, 0, 255, -1)
variable.funcion = fuct_prueba

print (variable.x)
print (variable.y)
print (variable.funcion())

#-------------------------------------------------------------------------

# agregando un nombre personalizado al "nameSpace"
variable = NameSpace()
variable.name_space = "<Sunfur Thanos-object>"
print (variable)


"""

#### ¿para que sirve el "NameSpace"? ####

Sirve para ordenar las funciones del código, de una manera sencilla y productiva :)

"""
