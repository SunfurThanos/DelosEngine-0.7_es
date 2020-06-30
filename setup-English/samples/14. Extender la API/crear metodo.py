# coding: utf-8

def funct_convertir_stringToList(callback): return list(callback)

#--------------------------------------------------------------------------------------------------

# tipos de objetos donde se les atribuirá el nuevo método a crear
objs_types = (str, u"ó", bytes,)

# nombre a utilizar para nuestro nuevo método
name_space = "list"

# función a utilizar para nuestro nuevo método
funct_callback = funct_convertir_stringToList

#--------------------------------------------------------------------------------------------------

#### creando método ¡xD! ####
CPythonBuiltin.create(
    (objs_types, name_space, funct_callback),
)

#--------------------------------------------------------------------------------------------------

# probando método
print (
    "hola mundo".list()
)
