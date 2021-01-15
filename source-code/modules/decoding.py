# coding: utf-8

#--------------------------------------------------------------------------------------------------

"""
  Autor: Andrade Echarry -> 'ALF'

  Pais : Venezuela

  Uso : funcione avanzda de decodificado (unicode) de caracteres

  Licencia : GNU GPL v3 <http://www.gnu.org/licenses/>

  Copyright (C) 2019 Andrade Echarry -> 'ALF'. All rights reserved.

"""

import ctypes, os, sys

#--------------------------------------------------------------------------------------------------

# saber si se esta posicionado en la consola
def CONSOLE_isConsole():
	try:
		return sys.stdout.isatty()
	except:
		return False

#--------------------------------------------------------------------------------------------------

# soporte para Windows !el Ogro del unicode en Python xD!
def func_custom_unicode_subprocess(text):
	if os.name == 'nt':
		try:
			text = unicode(text, "utf-8")
		except:
			try:
				text = unicode(text, "iso8859-15")
			except:
				pass

		buf = ctypes.create_unicode_buffer(512)
		if ctypes.windll.kernel32.GetShortPathNameW(text, buf, len(buf)):
			return buf.value
	else:
		return text

#--------------------------------------------------------------------------------------------------

def func_custom_unicode(text=False, toUnicode=True, subprocess=False):
	"""funcion de decodificación unicode de caracteres
	"""

	if text == False: return False

	DEFAULT_ENCODING = 'utf-8'

	respaldo = text

	def main(text, toUnicode, subprocess):
		if subprocess:
			return func_custom_unicode_subprocess(text)

		if sys.version_info[0] < 3:
			if CONSOLE_isConsole():
				if type(text) == unicode:
					try:
						return text.encode(sys.getfilesystemencoding()).decode("iso8859-15")
					except:
						return text

		def decode3(string):
			if CONSOLE_isConsole():
				return str(bytes(string, DEFAULT_ENCODING), DEFAULT_ENCODING)
			else:
				return str(bytes(string, DEFAULT_ENCODING), "iso8859-15")

		if sys.version_info[0] > 2: return decode3(text)


		if toUnicode:
			if not CONSOLE_isConsole():
				try:
					text = unicode(text, "utf-8")
				except:
					try:
						text = unicode(text, "iso8859-15")
					except:
						pass
			else:
				try:
					text = unicode(text)
				except:
					pass

		try:
		   return text.decode('utf-8')
		except:
			try:
				return text.decode('iso8859-15')
			except:
				try:
					return text.encode('utf-8')
				except:
					try:
						return text.encode('iso8859-15')
					except:
						return text

	result = main(text, toUnicode, subprocess)

	return result

#--------------------------------------------------------------------------------------------------

funcion    = func_custom_unicode
name_space = "unicode"

#--------------------------------------------------------------------------------------------------

## convirtiendo función a método de objeto
CPythonBuiltin.create(
	((str, bytes), name_space, funcion)
)

if sys.version_info[0] < 3:
	CPythonBuiltin.create(
		((unicode,), name_space, funcion)
	)
