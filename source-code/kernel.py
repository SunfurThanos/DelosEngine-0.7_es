# coding: utf-8

#-------------------------------------------------------------------------

"""
	Autor    : Sunfur Thanos

	Pais     : Venezuela

	Uso      : Entrada principal del nucleo de DelosEngine

	Licencia : GNU GPL v3 <http://www.gnu.org/licenses/>

	Copyright (C) 2019-2020 Sunfur Thanos. All rights reserved.

"""

# importando modulos (default) de Python
import os, sys, time, ctypes

#-------------------------------------------------------------------------

#  Diciéndole a Python donde esta la ruta de módulos personalizados
base_dir = os.path.split(__file__)[0x0]
base_library = os.path.join(base_dir, 'modulos')
sys.path.append(base_library)

#-------------------------------------------------------------------------

# CPython - funcion para modificar objetos del "built-in"
from get_dict_CPython import *

# CPython - mejora de (open::file*)
from file_api import *

# CPython - mejora de "os.path"
from os_path import *

# CPython - mejora de "str.decode(codec*)"
from decoding import *

# CPython - generacion de cache de variables
from cache_variables import *

# CPython - herramientas de cortes y remplazo
from cut_tools import *

# CPython - utilidades
from utilidades import *

# CPython - compresion numerica
from NumberCompress import *

#-------------------------------------------------------------------------

# area para prueba solitarias
