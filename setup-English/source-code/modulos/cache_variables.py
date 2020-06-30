# coding: utf-8

#--------------------------------------------------------------------------------------------------

"""
  Autor: Sunfur Thanos

  Pais : Venezuela

  Uso : funciones avanzadas de cache de variables (memoria de slots)

  Licencia : GNU GPL v3 <http://www.gnu.org/licenses/>

  Copyright (C) 2019-2020 Sunfur Thanos. All rights reserved.

"""

import ctypes, os, sys

#--------------------------------------------------------------------------------------------------

##### unir dos diccionarios en uno solo #####

def unir_diccionarios(dict1, dict2):
	result = dict1
	for key, value in dict2.items():
		result[key] = value
	return result

CPythonBuiltin.create(
	((type({}),), "join", unir_diccionarios),
)

#--------------------------------------------------------------------------------------------------

def Dir_get_modules(dict):
    """extraer del diccionario solo los objetos de tipo módulos"""
    import inspect
    result = {}
    for key, value in dict.items():
        if inspect.ismodule(value):
            result[key] = value
    return result

def Dir_get_funtions(dict):
    """extraer del diccionario solo las funciones"""
    import inspect
    result = {}
    for key, value in dict.items():
        if inspect.isfunction(value):
            result[key] = value
    return result

def Dir_get_string(dict):
    """extraer del diccionario solo los objetos de tipo string"""
    result = {}
    Unicode = u""
    for key, value in dict.items():
        if type(value) in ( type(""), type(Unicode), bytes ):
            result[key] = value
    return result

def Dir_get_Int(dict):
    """extraer del diccionario solo los de tipo numero entero"""
    result = {}
    Unicode = u""
    for key, value in dict.items():
        if type(value) == int:
            result[key] = value
    return result

def Dir_get_Float(dict):
    """extraer del diccionario solo los de tipo numero de punto flotante"""
    result = {}
    Unicode = u""
    for key, value in dict.items():
        if type(value) == float:
            result[key] = value
    return result

def Dir_get_Long(dict):
    """extraer del diccionario solo los de tipo numero LONG (py2<_*py3)"""
    result = {}
    Unicode = u""
    for key, value in dict.items():
        if type(value) == type(0xCC4336DA):
            result[key] = value
    return result

#--------------------------------------------------------------------------------------------------

# convertiendo funciones a metodos de objeto

CPythonBuiltin.create(
  ((type({}),), "packLong", Dir_get_Long),
)

CPythonBuiltin.create(
  ((type({}),), "packInt", Dir_get_Int),
)

CPythonBuiltin.create(
  ((type({}),), "packFloat", Dir_get_Float),
)

CPythonBuiltin.create(
  ((type({}),), "packString", Dir_get_string),
)

CPythonBuiltin.create(
	((type({}),), "packModules", Dir_get_modules),
)

CPythonBuiltin.create(
    ((type({}),), "packFunctions", Dir_get_funtions),
)
