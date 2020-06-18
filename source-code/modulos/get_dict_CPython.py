# coding: utf-8

#-------------------------------------------------------------------------

"""
  Autor: Sunfur Thanos

  Pais : Venezuela

  Uso : permite personalizar objetos del Built-in (change builtin types at runtime)

  Licencia : GNU GPL v3 <http://www.gnu.org/licenses/>

  Copyright (C) 2019-2020 Sunfur Thanos. All rights reserved.

"""

#--------------------------------------------------------------------------------------------------

# NOTA : este modulo falta por documentación, soy de esos informáticos raros que le da fastidio comentar código, ya que simplemente no los necesita para escribir, leer y re-escribir.

#--------------------------------------------------------------------------------------------------

import ctypes
import sys
import os
import time

try:
    import tempfile
except: pass

try:
    import __builtin__ as builtin_instance
except:
    import builtins as builtin_instance

#-------------------------------------------------------------------------

__version__ = 7.0

__build__   = (__version__, "18/06/2020", "06:09:01 AM")

__author__  = 'Sunfur Thanos'

__email__   = 'hormigence123@gmail.com'

#-------------------------------------------------------------------------

Builtin_get_dict = ctypes.pythonapi._PyObject_GetDictPtr
Builtin_get_dict.restype = ctypes.POINTER(ctypes.py_object)
Builtin_get_dict.argtypes = [ctypes.py_object]

#-------------------------------------------------------------------------


def Get_Builtin_object(object):
    return Builtin_get_dict(object).contents.value

#-------------------------------------------------------------------------


class CPython_get_builtin_change_value(object):

    def __init__(self, ar=0xCC4336DA):
        super(CPython_get_builtin_change_value, self).__init__()

    @property
    def Jhon_konnor(self):
        class Jhon_konnor(object):

            @staticmethod
            def create(*args):
                for objs, key, value in args:
                    for OBJ in objs:
                        builtin = type(OBJ)
                        if builtin == type:
                            builtin = OBJ
                        Get_Builtin_object(builtin)[key] = value

        return Jhon_konnor()

#-------------------------------------------------------------------------

builtin_instance.builtin_instance = builtin_instance

#-------------------------------------------------------------------------

builtin_instance.CPythonBuiltin = CPython_get_builtin_change_value().Jhon_konnor

#-------------------------------------------------------------------------

builtin_instance.Get_Builtin_object = Get_Builtin_object

#-------------------------------------------------------------------------

## soporte de xrange en Python3 ##
try:
    xrange
except:
    xrange = range

builtin_instance.xrange = xrange

#-------------------------------------------------------------------------

## saber si estas ejecutando el programa desde una consola (return bool) ##

def CONSOLE_isConsole():
    try:
        return sys.stdout.isatty()
    except:
        return False

builtin_instance.isConsole = CONSOLE_isConsole()

#-------------------------------------------------------------------------

## conectar (callback) al evento de cierre de la consola ##

def Linux_ConsoleEvent_close(on_exit):
    import signal
    signal.signal( signal.SIGHUP, handler )
    def handler(signum, frame):
        on_exit()

def MASTER_ConsoleEvent_close(on_exit):
    if isConsole:
        import sys
        if sys.platform.startswith('win'):
            import ctypes
            import sys
            from time import sleep
            from ctypes import c_int, WINFUNCTYPE
            from ctypes import wintypes

            def MADRE(self):
                on_exit()

            HandlerRoutine = WINFUNCTYPE(wintypes.BOOL, wintypes.DWORD)
            ctrl_handler = HandlerRoutine(MADRE)
            SetConsoleCtrlHandler = ctypes.windll.kernel32.SetConsoleCtrlHandler
            SetConsoleCtrlHandler.argtypes = (HandlerRoutine, wintypes.BOOL)
            SetConsoleCtrlHandler.restype = wintypes.BOOL
            if not SetConsoleCtrlHandler(ctrl_handler, 1): os._exit(0)
            return ctrl_handler, SetConsoleCtrlHandler
        else:
            Linux_ConsoleEvent_close(on_exit)

#-------------------------------------------------------------------------

## funcion para borrar depuración de la consola ##

def console_clear_debug():
    if isConsole:
        if sys.platform.startswith('win'):
            os.system("cls")
        else:
            try:
                os.system("tput reset")
            except:
                os.system("clear")

class _Builting_console_clear_debug(object):

    def __init__(self):
        self.retorno = ""

    def __repr__(self):
        console_clear_debug()
        return self.retorno

    def __call__(self):
        console_clear_debug()
        if isConsole: print (self.retorno)

    def write(self, *args):
        console_clear_debug()
        print (self.retorno)

builtin_instance.clear = _Builting_console_clear_debug()

#-------------------------------------------------------------------------

## funcion para crear NameSpace ##

class NameSpaceDelos2(object):

    def __init__(self, *args):
        super(NameSpaceDelos2, self).__init__()
        self.nsBackeng = "NameSpace"
        self.include_object_name_custom = ""


    def getx(self):
        return self.nsBackeng

    def setx(self, value):
        self.nsBackeng = value

    name_space = property(getx, setx)


    def include(self, *NewObject):

        if len(NewObject) != 1:
            for item in NewObject:
                self.include(item)
            return 0xAA17B0A5
        else:
            NewObject = NewObject[0]

        import inspect

        def index_dict_Z(diccionario):
            lista = []
            for name in diccionario.keys():
                lista+=[name, diccionario[name]]
            return lista

        if type(NewObject) == dict:
            name, NewObject = index_dict_Z(NewObject)
            self.include_object_name_custom = name
        else:
            self.include_object_name_custom = ""

        if inspect.isfunction(NewObject):
            self.addFuction(
                NewObject,
                self.include_object_name_custom or NewObject.__name__
            )
        else:
            if type(NewObject) == property:
                self.addFuction(
                    NewObject,
                    self.include_object_name_custom or NewObject.fget.__name__
                )
            else:
                if inspect.isclass(NewObject.__class__):
                    self.addClass(NewObject)


    def addClass(self, NewObject):

        if self.include_object_name_custom != "":
            name = self.include_object_name_custom or NewObject.__name__
            setattr(
                self.__class__,
                name,
                NewObject
            )
            return 0x2857674D

        diccionario = NewObject.__dict__
        for name, funcion in diccionario.items():
            if not name[:2] == "__":
                setattr(
                    self.__class__,
                    name,
                    funcion
                )

        diccionario = NewObject.__class__.__dict__
        for name, funcion in diccionario.items():
            if not name[:2] == "__":
                setattr(
                    self.__class__,
                    name,
                    funcion
                )



    def addFuction(self, funcion, NOMBRE):
        setattr(self.__class__, NOMBRE, funcion)


    def __repr__(self):
        return "%s" % (self.name_space)

builtin_instance.NameSpace = NameSpaceDelos2

#-------------------------------------------------------------------------

## Cambiar el color del texto en la consola ##

if os.name == 'nt':
    if isConsole:
        import struct

        def CChat_Reset_attributes(handle):
            csbi = ctypes.create_string_buffer(22)
            res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
            assert res

            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            return wattr

        STD_OUTPUT_HANDLE = -11
        handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        reset = CChat_Reset_attributes(handle)

        def CChat_set_color(value):
            stdout_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
            ctypes.windll.kernel32.SetConsoleTextAttribute(stdout_handle, value)

        def CChat_reset_color():
            ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)


def set_change_color_textConsole(string=False, color=False):
    if color == False or string == False:
        if isConsole:
            CChat_reset_color()
        return string
    if os.name == 'nt':
        if isConsole:
            CChat_set_color(color)
            return string
    return string

#-------------------------------------------------------------------------

## funcion de timeout ##

def func_Cpython_timeSleep(number, function=False, *args):

    if type(function) in (int, float, type(0xCC4336DA)):
        print (number)
        time.sleep(function)
        return 0x00

    time.sleep(number)

    uni = u"h"
    bi = b"h"

    if type(function) in (type(uni), type(bi), type("h")):
        print (function); return 0x00

    if function != False: function(*args)

builtin_instance.Sleep = func_Cpython_timeSleep

#-------------------------------------------------------------------------

## entry-text, con soporte para color ##

def raw_input_custom(string, colorA=False, colorB=False):

    if colorA == False or colorB == False:
    	return entryText(string)

    def color_blanco_Thread():
        time.sleep(0.05);
        CChat_set_color(colorB)

    if os.name == 'nt':
        if isConsole:
            try:
                from threading import Thread as proceso
                CChat_set_color(colorA);
                proceso(target=color_blanco_Thread).start()
            except ImportError:
                console.color(False)
                echo (console.color(string, colorA))
                console.color(False)
                echo (console.color("", colorB))
                string = ""

        resultado = entryText(string)
        console.color(False)

        return resultado
    else:
        return entryText(string)


if sys.version_info[0] >= 3:
    raw_input = input

POLLO_raw_input = raw_input

def new_raw_input(DATAy):
    try:
        return POLLO_raw_input(DATAy)
    except(KeyboardInterrupt, EOFError, SystemExit):
        return False

entryText = new_raw_input
builtin_instance.raw_input = raw_input_custom

#-------------------------------------------------------------------------

## mejora de (input) ##

builtin_instance.input = new_raw_input

#-------------------------------------------------------------------------

## detect key in console ##

def detect_key_getch():
    if not isConsole: return False

    try:
        from msvcrt import getch
    except ImportError:
    	try:
    		import termios
    		import tty
    	except:
    		return False

    	def getch():  # getchar(), getc(stdin)  #PYCHOK flake
    	    fd = sys.stdin.fileno()
    	    old = termios.tcgetattr(fd)
    	    try:
    	        tty.setraw(fd)
    	        ch = sys.stdin.read(1)
    	    finally:
    	        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    	    return ch
    key = getch()
    if type(key) == str: key = bytes(key)
    return key

#-------------------------------------------------------------------------

## mejora de (exit) ##

def salir_code(generic=False, *TIME):
    import inspect, os

    def salir_ya():
        try: os._exit(0x00)
        except: sys.exit()
        sys.stdin.close()

    try:
        generic(*TIME); salir_ya()
    except:
        pass

    if generic != False:
        if type(generic) in (int, float):
            Sleep(generic)
        else:
            if any(TIME):
                TIME = TIME[-1]
                if not type(TIME) in (int, float):
                    print (generic)
                else:
                    print (generic)
                    Sleep(TIME)
            else:
                print (generic)

    salir_ya()


class ClassPy_Exit(object):

    def __repr__(self): self.__call__()

    def __call__(self, *code): salir_code(*code)

builtin_instance.exit = ClassPy_Exit()

#-------------------------------------------------------------------------

## funcion para crear archivos temporales ##
def create_file_temporal(pattern="*", dir=False):

    if not any(pattern): pattern = "*"

    ramdom = False
    if type(pattern.cut("*", delete=False)) == list:
        ramdom = True if pattern.cut("*", delete=False).len > 1 else False

    ruta_tmp = tempfile.gettempdir()
    pattern = pattern.cut("*")
    pattern = pattern.join() if type(pattern) == list else pattern

    if ramdom:
        result = tempfile.mktemp(pattern)
    else:
        result = os.path.join(ruta_tmp, pattern)

    if dir != False:
        return os.path.join(dir.path.normalize, result.path.file)
    return result

builtin_instance.TmpPath = create_file_temporal

#-------------------------------------------------------------------------

## funcion para controlar el metacity de una consola ##

def EventMetacity(metodo):
    import ctypes, os, msvcrt
    from ctypes import wintypes
    kernel32    = ctypes.WinDLL('kernel32', use_last_error=True)
    user32      = ctypes.WinDLL('user32', use_last_error=True)
    SW_MAXIMIZE = metodo
    kernel32.GetConsoleWindow.restype = wintypes.HWND
    kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
    kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
    user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

    def maximize_console(lines=None):
        fd = os.open('CONOUT$', os.O_RDWR)
        try:
            hCon = msvcrt.get_osfhandle(fd)
            max_size = kernel32.GetLargestConsoleWindowSize(hCon)
            if max_size.X == 0 and max_size.Y == 0:
                raise ctypes.WinError(ctypes.get_last_error())
        finally:
            os.close(fd)
        cols = max_size.X
        hWnd = kernel32.GetConsoleWindow()

        if cols and hWnd:
            if lines is None:
                lines = max_size.Y
            else:
                lines = max(min(lines, 9999), max_size.Y)

            user32.ShowWindow(hWnd, SW_MAXIMIZE)
    maximize_console()


# maximize: 3, minimize: 2, umanimize: 1, hide: 0

def maximizar_consola():
    try:
        EventMetacity(3)
        return True
    except Exception as e: pass
    return False

def manimizar_consola():
    try:
        EventMetacity(2)
        return True
    except Exception as e: pass
    return False

def Unmaximize_consola():
    try:
        EventMetacity(1)
        return True
    except Exception as e: pass
    return False

def Hide_consola():
    try:
        EventMetacity(0)
        return True
    except Exception as e: pass
    return False


## modificar tamaño de fuente de la consola ##
def set_sizeFont_console(x, y, NameFont=False):
    if NameFont == False: NameFont = "Lucida Console"
    try:
        LF_FACESIZE       = 32
        STD_OUTPUT_HANDLE = -11

        import ctypes

        class COORD(ctypes.Structure):
            _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

        class CONSOLE_FONT_INFOEX(ctypes.Structure):
            _fields_ = [("cbSize",     ctypes.c_ulong),
                        ("nFont",      ctypes.c_ulong),
                        ("dwFontSize", COORD),
                        ("FontFamily", ctypes.c_uint),
                        ("FontWeight", ctypes.c_uint),
                        ("FaceName",   ctypes.c_wchar * LF_FACESIZE)]

        font              = CONSOLE_FONT_INFOEX()
        font.cbSize       = ctypes.sizeof(CONSOLE_FONT_INFOEX)
        font.nFont        = 0x00
        font.dwFontSize.X = x
        font.dwFontSize.Y = y
        font.FaceName     = NameFont
        handle            = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        ctypes.windll.kernel32.SetCurrentConsoleFontEx(handle, ctypes.c_long(False), ctypes.pointer(font))
    except Exception as e:
        pass

#-------------------------------------------------------------------------

## Cambiar titulo de la consola ##

def set_console_title(string):

    UNIX = b"\33]0;"

    if os.name == 'nt':
        if isConsole:
            os.system("title %s" % string)
            return True
    else:
        if isPython2:
            sys.stdout.write(UNIX + string + '\a')
            sys.stdout.flush()

        if isPython3:
            sys.stdout.buffer.write(UNIX + string + '\a')
            sys.stdout.buffer.flush()

    return True

#-------------------------------------------------------------------------

## implementación de (set_timeout) ##

def func_Cpython_timeOut(seconds, func, *arguments):
    from threading import Timer

    self = NameSpace()

    def funcion_JEDI(arguments):
        result = func(*arguments)
        if result:
            self.t = set_timeout(seconds, func, *arguments)
        return None

    self.t = Timer(seconds, funcion_JEDI, args=[arguments])
    self.t.start()

    return self.t

builtin_instance.set_timeout = func_Cpython_timeOut

#-------------------------------------------------------------------------

## implementación de (set_timeout) para @decorator ##


class Func_Timeout(object):

    def __init__(self, seconds=0.4):
        self.seconds = seconds

    def __call__(self, f):

        from functools import wraps

        @wraps(f)
        def wrapper(*args, **kwargs):
            def JEDI():
                return f(*args, **kwargs)

            set_timeout(self.seconds, JEDI)

        return wrapper

builtin_instance.Timeout = Func_Timeout

#-------------------------------------------------------------------------

## programación con multi-hilos ##

def set_threaded(func, *args):
    import threading
    t = threading.Thread(target=func, args=args)
    return t

builtin_instance.set_thread = set_threaded

#-------------------------------------------------------------------------

## programación con multi-hilos ##

def set_threaded(func):

    import threading
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()

    return wrapper

builtin_instance.threaded = set_threaded

#-------------------------------------------------------------------------

## auto-working dir ##
def func_WorkingDir(file=False):

    if file == False: file = sys.argv[0]

    if os.path.isdir(file):
        try: os.chdir(file); return True
        except: pass

    try: os.chdir(os.path.dirname(os.path.abspath(file))); return True
    except: pass

    return False

builtin_instance.setWorkingDir = func_WorkingDir

#-------------------------------------------------------------------------

## get working dir ##
def func_getWorkingDir():
    return os.getcwd()

builtin_instance.getWorkingDir = func_getWorkingDir

#-------------------------------------------------------------------------

## ¿ isRoot ? ##
def func_isRoot():
    if isWindows:
        directorio = SystemVars("%windir%").path.join("DelosEngine_protocoloIsRoot")
        if directorio.path.isdir: directorio.path.delete()
        validado = directorio.path.mkdir()
        if validado:
            directorio.path.delete()
            return True
        else:
            return False
    else:
        return os.geteuid() == 0

builtin_instance.isRoot = func_isRoot

#-------------------------------------------------------------------------

def getPythonVersion_funct():
    return sys.version_info[:3]

builtin_instance.getPythonVersion = getPythonVersion_funct()

#-------------------------------------------------------------------------

def isPython2_funct():
    return sys.version_info[0] == 2

builtin_instance.isPython2 = isPython2_funct()

def isPython3_funct():
    return sys.version_info[0] == 3

builtin_instance.isPython3 = isPython3_funct()

#-------------------------------------------------------------------------

def isPython27_funct():
    return sys.version_info[:2] == (2, 7)

builtin_instance.isPython27 = isPython27_funct()

def isPython26_funct():
    return sys.version_info[:2] == (2, 6)

builtin_instance.isPython26 = isPython26_funct()


#-------------------------------------------------------------------------

# funcion generica para color de texto en la consola
def FUNCTION_console_print(texto, Color):
    diccionario = {}
    diccionario[1] = ('0;31;40m', 12) # ROJO
    diccionario[2] = ('0;32;40m', 10) # VERDE
    diccionario[3] = ('2;33;40m', 14) # AMARRILLO
    diccionario[4] = ('0;34;40m',  1) # AZUL_OSCURO
    diccionario[5] = ('0;35;40m', 13) # MORADO
    diccionario[6] = ('0;36;40m', 11) # AZUL_MARINO
    diccionario[7] = ('0;37;40m',  8) # GRIS

    def console_print(texto, color):
        if isConsole:
            if isWindows:
                print (console.color(texto, color))
                console.color(False)
            else:
                print (('\x1B[%s' + texto + "\x1B[0m") % (color))
        else:
            print (texto)

    try:
        unix, Windows = diccionario[Color]
    except KeyError:
        unix, Windows = diccionario[0x1]

    if isWindows:
        console_print(texto, Windows)
    else:
        console_print(texto, unix)

#-------------------------------------------------------------------------

## clase de CONSOLE ##

ClassConsole_metodos = NameSpace()
ClassConsole_metodos.name_space = "<delos object at console:interaction>"

# borrar depuracion de la consola (proximamnete la UNIX)
ClassConsole_metodos.clear          = console_clear_debug
# tamaño normal de la consola (solo Windows)
ClassConsole_metodos.unmaximize     = Unmaximize_consola
# minimizar consola (solo Windows)
ClassConsole_metodos.minimize       = manimizar_consola
# ocultar consola (solo Windows)
ClassConsole_metodos.hide           = Hide_consola
# maximizar consola (solo Windows)
ClassConsole_metodos.maximize       = maximizar_consola
# tamaño de texto para la consola (solo Windows)
ClassConsole_metodos.FontFamily     = set_sizeFont_console
# titulo para la consola (solo Windows)
ClassConsole_metodos.title          = set_console_title
# detectar cierre de la consola
ClassConsole_metodos.EventClose     = MASTER_ConsoleEvent_close
# color de texto para la consola (solo Windows)
ClassConsole_metodos.color          = set_change_color_textConsole
# color de texto para la consola (multiplataforma)
ClassConsole_metodos.print_colorize = FUNCTION_console_print
# detectar teclas presionadas
ClassConsole_metodos.event          = detect_key_getch
#### agregar al builtins ####
builtin_instance.console            = ClassConsole_metodos

#-------------------------------------------------------------------------

## división con resultado en decimales ##

def Func_Math(variable, prec=8, float=True):
    import decimal

    decimal.getcontext().prec = prec

    resultado = variable.cut("/", delete=False)\
    .cut("*", delete=False)\
    .cut("+", delete=False)\
    .strip()

    tmp = ""
    for item in resultado:
        if not item in ("/","*","+"):
            tmp += "decimal.Decimal(%s)" % (item)
        else:
            tmp += item

    dockerXDU_blender268 = NameSpace()
    exec ('dockerXDU_blender268.__dict__.update({"neo":%s})' % (tmp))

    if float:
        return dockerXDU_blender268.neo
    else:
        return int(dockerXDU_blender268.neo)


builtin_instance.Math = Func_Math

#-------------------------------------------------------------------------

### funcion DEBUG ###

ignoreWarning = False
ignoreError = False

def printTreeError(mensaje=False, salir=True):
    controler = sys.exc_info()
    if not any(controler): return False
    error_mesage, error_type = controler[1].args[0], controler[0]
    sub_contoler = controler[2]
    lineError =  sub_contoler.tb_lineno
    newControler = sub_contoler.tb_frame
    line_prinDebug = newControler.f_lineno
    fileError = newControler.f_code.co_filename

    diccionario = ({
        "$error$" : error_mesage,
        "$type$"  : error_type.__name__,
        "$line$"  : str(lineError),
        "$debug$" : str(line_prinDebug),
        "$file$"  : fileError
    })

    if mensaje == False:
        diccionario.update(
            {
                "$type$" : (error_type, error_type.__name__),
            }
        )
        return diccionario

    mensaje = mensaje.replace(
        "$file$",
        diccionario["$file$"].unicode()
    )

    mensaje = mensaje.replace("$line$", diccionario["$line$"])
    mensaje = mensaje.replace("$type$", diccionario["$type$"])
    mensaje = mensaje.replace("$error$", diccionario["$error$"])
    mensaje = mensaje.replace("$debug$", diccionario["$debug$"])

    archivo = diccionario["$file$"]
    linea = int(diccionario["$line$"])
    pyc = ''
    if archivo.path.isfile:
        if not archivo.path.isbinary:
            # print (archivo.path.read(line=linea),)
            mensaje = mensaje.Replace("$code$", archivo.path.read(line=linea)[-1].strip())
        else:
            mensaje = mensaje.Replace("$code$", pyc)
    else:
        mensaje = mensaje.Replace("$code$", pyc)

    if not ignoreError:
        print (mensaje)

    if salir:
        try: os._exit(0x0)
        except: sys.exit()

    return mensaje


def func_warn(message):
    try:
        caller = sys._getframe(1)
    except ValueError:
        globals = sys.__dict__
        lineno = 1
    else:
        globals = caller.f_globals
        lineno = caller.f_lineno

    if '__name__' in globals:
        module = globals['__name__']
    else:
        module = "<string>"
    filename = globals.get('__file__')
    if filename:
        fnl = filename.lower()
        if fnl.endswith((".pyc", ".pyo")):
            filename = filename[:-1]
    else:
        if module == "__main__":
            try:
                filename = sys.argv[0]
            except AttributeError:
                filename = '__main__'
        if not filename:
            filename = module

    archivo = filename
    linea = str(lineno)

    mensaje = message.replace("$file$", archivo.unicode())
    mensaje = mensaje.replace("$line$", linea)
    if not ignoreWarning: print (mensaje)
    return mensaje


@property
def ExceptionType(self): return sys.exc_info()[0]

Python_functDebug_custom = NameSpace()
Python_functDebug_custom.error = printTreeError
Python_functDebug_custom.echo = sys.stdout.write
Python_functDebug_custom.warning = func_warn
builtin_instance.debug = Python_functDebug_custom
Python_functDebug_custom.include(ExceptionType) # comentar si se desea modificar ".include"

#-------------------------------------------------------------------------

# sunfur import module
# global yes_path_append
# yes_path_append = []

# def Sunfur_import(file):
#     import sys
#     try:
#         caller = sys._getframe(1)
#     except ValueError:
#         Globals = sys.__dict__
#     else:
#         Globals = caller.f_globals

#     name = file.path.name
#     directorio = file.path.dir
#     if not directorio in yes_path_append:
#         sys.path.append(directorio)
#         yes_path_append.append(directorio)

#     Globals[name] = __import__(name)

#     return Globals[name]

# include = Sunfur_import

#-------------------------------------------------------------------------

# documentacion estatica
Delos_plantilla_Autorun = '''# coding: utf-8
try: import __builtin__ as builtin
except: import builtins as builtin
import DelosEngine
builtin.delos = DelosEngine
delos.__doc__ = """FrameWork multiplataforma para Python.

Potente FrameWork de productividad.
"""
'''

#-------------------------------------------------------------------------

#### crear metodo aplication

@property
def funcion_pathExe(self):
    python_executable = sys.executable
    return python_executable if python_executable.path.isfile else False

@property
def funcion_pathFile(self): return sys.argv[0] if sys.argv[0].any else False

@property
def funcion_parameters(self):
    datos = sys.argv[1:]
    return datos if datos.any else False

@property
def funcion_pid(self):
    return os.getpid()

@property
def funcion_time(self):
    import time; return time.time()

aplication = NameSpace()
aplication.name_space = "<delos object at Python:aplication>"
aplication.include({"pathExe"    :    funcion_pathExe})
aplication.include({"pathFile"   :   funcion_pathFile})
aplication.include({"parameters" : funcion_parameters})
aplication.include({"pid"        :        funcion_pid})
aplication.include({"time"       :       funcion_time})
builtin_instance.Application = aplication
