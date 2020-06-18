#!/usr/bin/python
# coding: utf-8

#--------------------------------------------------------------------------------------------------

"""
  Autor    : Sunfur Thanos

  Pais     : Venezuela

  Sistema  : Windows / Linux / Mac OS X | x32 / x64

  Uso      : permite borrar DelosEngine (no requiere permisos administrativos)

  Licencia : GNU GPL v3 <http://www.gnu.org/licenses/>

  Copyright (C) 2019-2020 Sunfur Thanos. All rights reserved.

"""

if not hasattr(__builtins__, "delos"): print ("Error: DelosEngine no esta instalado :("); exit()

#--------------------------------------------------------------------------------------------------

console.clear()

#--------------------------------------------------------------------------------------------------

coyotito = 0x0 if not isConsole else 0.8

#--------------------------------------------------------------------------------------------------

setWorkingDir()

#--------------------------------------------------------------------------------------------------

# quitar modulo (MAIN)
def RemoveApp(exterminate=False, directorio_install=False):
    __GOD__  = delos.Delos_plantilla_Autorun

    if exterminate == True: return RemoveApp_ALL()

    if directorio_install == False: directorio_install = delos.__file__.path.dir
    FrameWork_path_path    = directorio_install.path.join("DelosEngine.pyc")
    autorun_FrameWork_path = directorio_install.path.join("usercustomize.py")

    # borrando auto-iniciado
    if autorun_FrameWork_path.path.isfile:
      autorun_FrameWork_path.path.save(
          autorun_FrameWork_path.path.read().Replace(__GOD__)
        ).close()

    # borrando modulo delos2
    FrameWork_path_path.path.delete()

    # comprobando todo
    return False if FrameWork_path_path.path.isfile else True

def RemoveApp_ALL():
    import site

    if delos.sys.version_info[:2] <= (2, 6): directorio_install = site.USER_SITE
    else: directorio_install = site.getusersitepackages()

    match = directorio_install.path.dir.path.dir.path.join("*", "site-packages").path.autocomplete

    if type(match) is list:
        # multi busqueda
        for item in match:
            validar = RemoveApp(directorio_install=item)
            if not validar: return False
    else:
        # busqueda unitaria
        if match:
            validar = RemoveApp(directorio_install=match)
            if not validar: return False

    return True

#--------------------------------------------------------------------------------------------------

# Activa la eliminación en todas las versiones de Python
All_pythons = True
# Desinstalando DelosEngine
if not RemoveApp(exterminate=All_pythons):
  exit(
    "Error: No se puede eliminar (DelosEngine)",
    0.8
  )

#--------------------------------------------------------------------------------------------------

Sleep ("Info: (DelosEngine) fue borrado exitosamente", coyotito)
