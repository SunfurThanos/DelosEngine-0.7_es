#!/usr/bin/python
# coding: utf-8

#--------------------------------------------------------------------------------------------------

"""
  Autor       : Sunfur Thanos

  Pais        : Venezuela

  Sistema     : Windows / Linux / Mac OS X | x32 / x64

  Dependencia : Python 2.5 o superior | x32 / x64

  Uso         : permite instalar DelosEngine en Python (no requiere permisos administrativos)

  Licencia    : GNU GPL v3 <http://www.gnu.org/licenses/>

  Copyright (C) 2019-2020 Sunfur Thanos. All rights reserved.

"""

### detectando que DelosEngine no este instalado ###
if hasattr(__builtins__, "delos"):
  console.clear()
  coyotito = 0x0 if not isConsole else 0.8
  exit ('Error: Ya existe una version anterior de DelosEngine (v%s)' % delos.__version__, coyotito)

#--------------------------------------------------------------------------------------------------

import shutil, sys, os, py_compile, site, zlib
from glob import glob as FindFile

#--------------------------------------------------------------------------------------------------

try: os.chdir(os.path.dirname(os.path.abspath(__file__)))
except: pass

#--------------------------------------------------------------------------------------------------

##### Diciéndole a Python donde esta la ruta de módulos personalizados #####
base_dir = os.path.split(__file__)[0]
base_library = os.path.join(base_dir, 'source-code/modulos')
sys.path.append(base_library)
base_library = os.path.join(base_dir, 'source-code')
sys.path.append(base_library)

#--------------------------------------------------------------------------------------------------

# modulos DelosEngine
from get_dict_CPython import *
from file_api         import *
from os_path          import *
from decoding         import *
from cache_variables  import *
from cut_tools        import *
from utilidades       import *

#--------------------------------------------------------------------------------------------------

console.clear()

#--------------------------------------------------------------------------------------------------

coyotito = 0x0 if not isConsole else 0.8

#--------------------------------------------------------------------------------------------------

Salida_tmp_py = "Delos_temporalZ.py"

#--------------------------------------------------------------------------------------------------

### unir todos los modulos en uno solo ###

MAIN = ""
BODY = ""
for archivo in "./source-code/modulos".path.listdir():
    if archivo.path.ext == "py":
      DATA = archivo.path.read()
      if archivo.path.name == "get_dict_CPython":
        MAIN = DATA
      else:
        BODY += DATA

result = MAIN + BODY
Salida_tmp_py.path.save(result.replace("\t", " ")).close()

#--------------------------------------------------------------------------------------------------

### convertir modulo a (pyc) y copiandolo al directorio de trabajo de Python ###

if sys.version_info[:2] <= (2, 6): directorio_install = site.USER_SITE
else: directorio_install = site.getusersitepackages()
FrameWork_path_path = os.path.join(directorio_install, "DelosEngine.pyc")
if not os.path.isdir(directorio_install): os.makedirs(directorio_install)

fileX = Salida_tmp_py
path_relative = os.path.relpath(fileX)
py_compile.compile(file=path_relative)
if os.path.isfile(fileX): os.remove(fileX)

if float(sys.version.split(" ")[0][:3]) >= 3:
  pycache = os.path.relpath(FindFile(os.path.join("__pycache__", "Delos_temporalZ.*"))[0])
  shutil.move(pycache, FrameWork_path_path )
  shutil.rmtree("__pycache__")
else:
  pycache = os.path.relpath(path_relative + "c")
  shutil.move(pycache, FrameWork_path_path)

#-------------------------------------------------------------------------

## crear auto-run de DelosEngine ##

def setAutoRun():
    __GOD__  = Delos_plantilla_Autorun

    directorio_install = FrameWork_path_path.path.dir
    autorun_FrameWork_path = os.path.join(directorio_install, "usercustomize.py")

    if autorun_FrameWork_path.path.isfile:
      data = __GOD__ + autorun_FrameWork_path.path.read()
      autorun_FrameWork_path.path.save(data).close()
    else:
      autorun_FrameWork_path.path.save(__GOD__).close()

    return True if autorun_FrameWork_path.path.isfile else False

if not setAutoRun():
	Sleep ("no se pudo agregar punto de auto-run para DelosEngine", coyotito)

#-------------------------------------------------------------------------

# info install

try:
  sys.path.append(directorio_install); import DelosEngine as delos
except Exception as mesageError:
	exit ("instalacion FALLIDA")

PESO = FrameWork_path_path.path.size.info.join(" ")
Python_version = getPythonVersion[:2].join('.')

result = "** Instalacion exitosa :)\n"
result += "APP directorio: '{directorio_install}'\n"
result += "APP peso: {PESO}\n"
result += "APP version: {delos.__version__}\n"
result += "Python version: {Python_version}"

Sleep (result.toF, coyotito)
