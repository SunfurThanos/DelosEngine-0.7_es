# coding: utf-8

#--------------------------------------------------------------------------------------------------

"""
  Autor: Sunfur Thanos

  Pais : Venezuela

  Uso : mejora y simplificación de (os.path) !MUERTE a la TIRANIA Python!

  Licencia : GNU GPL v3 <http://www.gnu.org/licenses/>

  Copyright (C) 2019-2020 Sunfur Thanos. All rights reserved.

"""

import ctypes, os, sys

#--------------------------------------------------------------------------------------------------

## implementacion para leer bytes en un archivo
class ClassFileApp_read(object):
	def __init__(self, arg, get_mimetype):
		super(ClassFileApp_read, self).__init__()
		self.self = arg
		self.type_read = get_mimetype


	def leer_una_linea(self): # leer una sola linea (high performance)

		if self.type_read(self.archivo) == "BINARY":
			self.instance = open(self.archivo, "rb")

		if self.type_read(self.archivo) in ('PLAIN', 'VACIO'):
			self.instance = open(self.archivo)

		for num, linea in enumerate(self.archivo.path.read(lines=True)):
			if (num+1) == self.line:
				return linea

		return False


	def leer_todas_lineas(self): # leer todas las lineas

		if self.type_read(self.archivo) == "BINARY":
			self.instance = open(self.archivo, "rb")

		if self.type_read(self.archivo) in ('PLAIN', 'VACIO'):
			self.instance = open(self.archivo)

		for NUM, DATA in enumerate(self.instance):
			NUM+=1
			yield (NUM, DATA)

	# kernel principal
	def run(self, archivo, bufsize, line, lines):
		self.archivo = archivo
		self.bufsize = bufsize
		self.line = line
		self.lines = lines

		if type(self.line) == int:
			return self.leer_una_linea()

		if self.lines == True:
			return self.leer_todas_lineas()

		if self.type_read(self.archivo) == "BINARY":
			self.instance = open(self.archivo, "rb")

			if bufsize == True: return self

			if type(self.bufsize) == int:
				select = self, self.instance.read(self.bufsize)
			else:
				select = self.instance.read()

			return select

		if self.type_read(self.archivo) in ('PLAIN', 'VACIO'):
			self.instance = open(self.archivo)

			if bufsize == True: return self

			if type(self.bufsize) == int:
				select = self, self.instance.read(self.bufsize)
			else:
				select = self.instance.read()

			return select

		return False

	# leer bytes
	def read(self, *args):

		if len(args) == 2:
			start = args[0]
			bufsize = args[1]
			self.cursor(start)
		else:
			bufsize = args[0]

		if bufsize == True: return self
		if not type(bufsize) == int: return self, False
		self.bufsize = bufsize
		return self, self.instance.read(bufsize)

	# cerrar instancia de lectura
	def close(self):
		self.instance.close()
		return False

	# cambiar posicion de lectura por index
	def cursor(self, number):
		self.instance.seek(number)

	# leer posicion del cursor de lectura
	@property
	def get_cursor(self):
		return self.instance.tell()

#--------------------------------------------------------------------------------------------------

## implementacion para guardar bytes en un archivo
class ClassFileApp_save(object):
	def __init__(self, arg, get_mimetype):
		super(ClassFileApp_save, self).__init__()
		self.self = arg
		self.type_read = get_mimetype
		self.IsFileNull = False

	# kernel principal
	def run(self, file, data, type_data, mode):
		self.file       = file
		self.type_data  = type_data
		self.mode       = mode
		self.use_cursor = False

		if mode in ("a+", "+"):
			self.mode = "r+b"

		if self.mode == "r+b":
			if not self.file.path.isfile:
				self.file.path.save().close()
				self.IsFileNull = True

		if not any(data):
			self.IsFileNull = True

		if self.mode == "w":  self.type_data = "PLAIN"
		if self.mode == "wb": self.type_data = "BINARY"
		if self.mode == "r+b": self.type_data = "BINARY"

		if self.mode == False:
			if self.type_data == "BINARY":
				self.mode = "wb"

			if self.type_data in ("PLAIN","LIST"):
				self.mode = "w"

		if self.type_data == "BINARY":
			self.instance = open(self.file, self.mode)
			if self.mode != "r+b":
				self.instance.write(data)
			else:
				if any(data):
					self.cursor_automatic()
					self.instance.write(data)
			return self

		if self.type_data == 'PLAIN':
			self.instance = open(self.file, self.mode)
			self.instance.write(data)
			return self

		if self.type_data == "LIST":
			self.instance = open(self.file, self.mode)
			self.escribir_lista(data, ready=False)
			return self

		return False

	# soporte para escribir un objeto tipo lista directamente en el archivo
	def escribir_lista(self, data, ready=False):

		salto = ""
		for num, pointer in enumerate(data):
			texto = str(pointer)
			if num == 1: salto = "\n"
			self.instance.write(salto+texto)

	# cursor automatico ideal para guardado continuado
	# posiciona el cursor siempre al final del archivo
	def cursor_automatic(self):
		pointer = self.file.path.size.value
		self.instance.seek(pointer)

	# kernel de guardar
	def save(self, datos, line=False):

		isLinea1 = False

		if self.mode == "r+b":
			if not self.use_cursor:
				self.cursor_automatic()
			self.instance.write(datos); return self

		if self.IsFileNull:
			self.instance.close()

			self.IsFileNull = False

			self.type_data = self.type_read(False, data=datos)

			if self.type_data == "BINARY":
				self.instance = open(self.file, "wb")
			else:
				self.instance = open(self.file, "w")

			isLinea1 = True


		if line != False:
			if not self.type_data == "LIST":
				if self.type_data == 'PLAIN':
					sep = "\n" if line == True else line
					if isLinea1:
						datos = datos + sep
					else:
						datos = sep + datos


		if not self.type_data == "LIST":
			self.instance.write(datos)
		else:
			self.escribir_lista(datos, ready=True)
		return self

	# cerrar archivo
	def close(self):
		self.instance.close()
		return self.file

	# mover cursor de lectura
	def cursor(self, number):
		self.use_cursor = True
		self.instance.seek(number)

	# leer bytes
	def read(self, *args):
		if len(args) == 2:
			start = args[0]
			bufsize = args[1]
			self.cursor(start)
		else:
			bufsize = args[0]
		return self, self.instance.read(bufsize)

	# eliminar los bytes de un archivo desde una determinada posicion
	def cut_from(self, *size):
		return self.instance.truncate(*size)

	# ver posicion del cursor de lectura
	@property
	def get_cursor(self):
		return self.instance.tell()

#--------------------------------------------------------------------------------------------------

## convirtiendo función a método de objeto
CPythonBuiltin.create(
	((ctypes,), "ClassFileApp_save", ClassFileApp_save),
	((ctypes,), "ClassFileApp_read", ClassFileApp_read)
)

#--------------------------------------------------------------------------------------------------

# hackeo blanco para poder cerrar un archivo abierto (en lectura) de forma productiva
# ejemplo : archivo.path.read(0x34).close() | archivo.path.save("Jhon Konnor").close()
def closeFileReadBit(tuple):
	if len(tuple) == 2:
		lector, leido = tuple
		if type(lector) in (ClassFileApp_read, ClassFileApp_save):
			return leido
		else:
			return tuple
	else:
		return tuple

## convirtiendo función a método de objeto
CPythonBuiltin.create(
	((type((0x0, 0x2)),), "close", closeFileReadBit),
)
