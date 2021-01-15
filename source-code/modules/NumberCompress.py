# coding: utf-8

#--------------------------------------------------------------------------------------------------

"""
  Autor: Andrade Echarry -> 'ALF'

  Pais : Venezuela

  Uso : compresión de números

  Licencia : GNU GPL v3 <http://www.gnu.org/licenses/>

  Copyright (C) 2019-2020 Andrade Echarry -> 'ALF'. All rights reserved.

"""

#--------------------------------------------------------------------------------------------------

# diccionario de permutaciones (N**2)
Compresslayer1_encoders = {
'09': 'm', '6-': '\x80', '6.': '\x91', '04': 's', '60': 'v', '61': '*', '62': '\x9c',
'63': ')', '64': 'V', '65': 'b', '66': '\x0c', '90': '\x85', '68': "'", '69': '\x1c',
'24': '/', '25': 'h', '26': 'f', '27': '~', '20': '\x19', '21': '\x03', '22': '\t',
'23': '\x8d', '.3': 'u', '28': '\n', '29': ';', '.8': '\x9a', '.9': '`', '.0': 'g',
'.1': '\x12', '.2': '&', '96': '$', '.4': '@', '.5': '+', '.6': '\x8e', '.7': '\x01',
'11': '\x90', '9-': ' ', '9.': 'a', '99': 'E', '98': 'k', '12': 'H', '2-': 'L', '91': 'T',
'59': 'A', '93': '\x1e', '92': 'O', '95': '\x08', '94': 'F', '97': 'q', '14': '[', '1-': 'd',
'10': 'j', '13': '\x81', '2.': '\x15', '15': 'Y', '58': 'N', '17': 'z', '16': 't', '19': 'R',
'18': '\x06', '57': 'W', '-.': 'X', '51': 'r', '50': '\x1b', '53': '\x1f', '52': '\x1d',
'5-': '\\', '--': '\x0f', '-7': '\x8c', '5.': 'w', '-1': 'M', '-0': ':', '-3': '\x8f',
'54': 'i', '-9': 'Q', '-8': 'D', '1.': 'p', '30': 'y', '8.': 'U', '8-': '\x13', '67': '\x96',
'88': 'l', '89': '\x86', '82': 'K', '83': '%', '80': '?', '81': '\x0b', '86': '\x0e', '87': '.',
'84': 'G', '85': 'P', '02': '\x97', '-5': '\r', '00': '\x99', '01': '\x82', '06': 'C', '07': 'I',
'48': '(', '05': '"', '46': '|', '47': ']', '44': '_', '45': '<', '42': 'J', '43': '\x14',
'40': '\x02', '41': '\x93', '4.': 'Z', '4-': '>', '0.': '#', '0-': '\x89', '56': '\x84',
'78': '\x98', '03': 'o', '7.': '\x8a', '7-': 'n', '-2': '\x8b', '77': '=', '76': 'e',
'75': '\x16', '74': '\x18', '73': 'B', '72': '^', '71': '\x87', '70': 'x', '-6': '\x94',
'-4': '\x9b', '79': '\x05', '.-': '\x92', '39': '\x04', '38': '\x95', '..': '!', '55': '\x17',
'33': 'S', '32': '\x07', '31': '\x1a', '49': 'c', '37': '\x11', '36': '\x83', '35': ',',
'34': '\xd2', '3.': '\x88', '3-': '\x10', '08': '\x7f'
}

Compresslayer2_encoders = {
	"0" : '\xff',
	"1" : '\xfe',
	"2" : '\xfd',
	"3" : '\xfc',
	"4" : '\xfb',
	"5" : '\xfa',
	"6" : '\xf9',
	"7" : '\xf8',
	"8" : '\xf7',
	"9" : '\xf6',
}

#--------------------------------------------------------------------------------------------------

def func_compressNumber(cadena):
	"""comprimiendo bytes numéricos de una cadena
	"""
	result = ""

	for char in str(cadena).group(2):
		if not char[-1] == False:
			llave = char.join()
			result+=Compresslayer1_encoders[llave]
		else:
			result+=Compresslayer2_encoders[char[0]]

	return result

def func_decompressNumber(cadena):
	"""descomprimiendo bytes numéricos de una cadena
	"""
	def RUN():
		result2 = ""
		for char in cadena:
			active = False
			for key, value in Compresslayer1_encoders.items():
				if value == char:
					active = True
					result2+=key

			if not active:
				for key, value in Compresslayer2_encoders.items():
					if value == char:
						active = True
						result2+=key

		return result2

	try: result2 = RUN()
	except: return False

	return result2

#--------------------------------------------------------------------------------------------------

## generando los correspondientes métodos

BYTES = b""
STR   = ""
UNi   = u""

CPythonBuiltin.create(
    ((int, float, 0xCC4336DA, str, BYTES, UNi,), "toCompress", func_compressNumber),
    ((str, STR, BYTES, UNi,), "toDecompress", func_decompressNumber),
)
