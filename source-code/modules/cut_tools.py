# coding: utf-8

#--------------------------------------------------------------------------------------------------

"""
  Autor: Andrade Echarry -> 'ALF'

  Pais : Venezuela

  Uso : utilidades de cortes y remplazos

  Licencia : GNU GPL v3 <http://www.gnu.org/licenses/>

  Copyright (C) 2019-2020 Andrade Echarry -> 'ALF'. All rights reserved.

"""

import ctypes, os, sys

#--------------------------------------------------------------------------------------------------

__LONG__ = type(0xCC4336DA)

#--------------------------------------------------------------------------------------------------

def JhonKonnor_str_getIn_CORE(lista, string):
	"""extraer item de una lista por concurrencia
	"""
	retorno = []
	for item in lista:
		if string in item:
			retorno+=[item]
	return retorno

# convirtiendo función a método de objeto
CPythonBuiltin.create(
	((list,), "getIn", JhonKonnor_str_getIn_CORE),
)

#--------------------------------------------------------------------------------------------------

def JhonKonnor_str_strip_CORE(lista):
	"""eliminar espacios iniciales y finales de un item o cadena de String
	"""
	result = []
	for item in lista:
		if not type(item) in [type(0xDBBC4FD1), int, float]:
			if not type(item) in (list, tuple):
				if not item.isspace():
					item = item.strip()
			else:
				item = item.strip()
		result+=[item]
	return result

# convirtiendo función a método de objeto
CPythonBuiltin.create(
	((list,), "strip", JhonKonnor_str_strip_CORE),
)

#--------------------------------------------------------------------------------------------------

def CPython_leer_en_grupos_de_2_CORE(lista, value_range=0x002):
	"""agrupar items de una lista o String
	"""
	if not type(lista) in (tuple, list):
		lista = list(lista)

	if value_range < 2: return lista
	result = []
	conteo = 0
	tmp    = []
	for item in lista:
		if conteo == value_range:
			result+=[tmp]
			tmp=[item]
			conteo=1
		else:
			tmp+=[item]
			conteo+=1


	if any(tmp):
		if len(tmp) == value_range:
			result.append(tmp)
		else:
			for x in range(value_range-len(tmp)):
				tmp+=[False]
			result.append(tmp)

	return result

## convirtiendo función a método de objeto
CPythonBuiltin.create(
	((list, str, bytes,), "group", CPython_leer_en_grupos_de_2_CORE),
)

if sys.version_info[0] < 3:
	CPythonBuiltin.create(
		((unicode,), "group", CPython_leer_en_grupos_de_2_CORE),
	)

#--------------------------------------------------------------------------------------------------

def JhonKonnor_list_replace_item(lista, pos, new=False):
	"""remplazar item de una lista
	"""
	nuevo = []
	for num, pointer in enumerate(lista):
		if num == pos or pointer == pos:
			if new == False: continue
			pointer = new
		nuevo+=[pointer]
	return nuevo

# convirtiendo función a método de objeto
CPythonBuiltin.create(
	((list,), "replace", JhonKonnor_list_replace_item),
)

#--------------------------------------------------------------------------------------------------

def JhonKonnor_str_toString_CORE_join(lista, delimiter=""):
	"""convertir a lista a string de forma delimitada
	"""
	cola = []
	if type(lista) in [int, float, __LONG__]: lista = str(lista)
	for pointer in lista:
		if type(pointer) in [int, float, __LONG__]:
			pointer = str(pointer)
		cola+=[pointer]
	return delimiter.join(cola)

# convirtiendo función a método de objeto
CPythonBuiltin.create(
	((list, tuple, int, __LONG__, float, ), "join", JhonKonnor_str_toString_CORE_join),
)

#--------------------------------------------------------------------------------------------------

def JhonKonnor_str_replace_pattern(string, pattern="", new="", maxi=-1):
	"""remplazar bytes de una cadena String
	"""
	if type(pattern) in (list, tuple):
		for numero, item in enumerate(pattern):
			if type(maxi) == int:
				string = string.replace(item, new, maxi)
			else:
				try:
					string = string.replace(item, new, maxi[numero])
				except:
					string = string.replace(item, new, maxi[numero-1])

		return string
	else:
		return string.replace(pattern, new, maxi)

## convirtiendo función a método de objeto
CPythonBuiltin.create(
	((str, ), "Replace", JhonKonnor_str_replace_pattern),
)

if sys.version_info[0] < 3:
	CPythonBuiltin.create(
		((unicode,), "Replace", JhonKonnor_str_replace_pattern),
	)

#--------------------------------------------------------------------------------------------------

def JhonKonnor_cut_pattern(
	string,
	sep=" ",
	delete=True,
	group=False,
	start=False,
	end=False,
	BytesFile=False):
	"""herramienta de corte por delimitaciones parecida a (object.split)
	"""

	index = 0
	lista = []

	if type(sep) in (tuple, list):
		Zresult = string
		for pointer in sep:
			Zresult = Zresult.cut(pointer, delete, group, start, end, BytesFile)
		return Zresult

	if type(string) == list:
		lista = []
		for item in string:
			resultado = item.cut(sep, delete, group, start, end)
			if resultado == item: resultado = [item]
			if group:
				lista+=[resultado]
			else:
				lista+=resultado
		return lista


	def tercer_tiempo(lista, delete):
		if start == False: return lista

		recolector = ""
		resultado  = []
		vueltas    = 0x000
		focusStart = False

		for item in lista:
			if item == sep: vueltas += 0x01

			if delete:
			 	if item == sep: continue

			if vueltas < start:
				recolector += item
			else:
				if focusStart:
					resultado+=[item]
				else:
					resultado+=[recolector, item]
					focusStart = True

		if any(resultado):
			return resultado
		else:
			return lista


	def segundo_tiempo(listax, delete):
		if end == False: return tercer_tiempo(listax, delete)

		resultado = []
		vueltas   = 0x000
		recolector = ""

		for item in listax:
			if item == sep: vueltas += 0x01

			if vueltas <= end:
				if vueltas == end:
					if item == sep:
						resultado+=[item]
					else:
						recolector+=item
				else:
					resultado+=[item]
			else:
				if delete:
					if item == sep: continue
				recolector+=item

		if any(recolector): resultado+=[recolector]

		return tercer_tiempo(resultado, delete)


	Xdelete = delete
	if start != False:
		delete = False

	while True:
		pos   = string.find(sep, index)
		chuck = index
		index = pos+len(sep)

		if pos < 0:
			if any(lista):
				xp = [string[chuck:]]
				if any(xp): lista+=xp
				if delete:
					tmp = []
					for item in lista:
						if not sep == item:
							tmp+=[item]
					return segundo_tiempo(tmp, Xdelete)
				else:
					return segundo_tiempo(lista, Xdelete)
			else:
				return string
		else:
			if any(string[chuck:pos]):
				lista += [ string[chuck:pos], string[pos:index] ]
			else:
				lista += [ string[pos:index] ]

## convirtiendo función a método de objeto
CPythonBuiltin.create(
	((str, list, bytes,), "cut", JhonKonnor_cut_pattern),
)

if sys.version_info[0] < 3:
	CPythonBuiltin.create(
		((unicode,), "cut", JhonKonnor_cut_pattern),
	)
