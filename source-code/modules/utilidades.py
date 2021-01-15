# coding: utf-8

#-------------------------------------------------------------------------

"""
  Autor: Andrade Echarry -> 'ALF'

  Pais : Venezuela

  Uso : utilidaes para string y int or float

  Licencia : GNU GPL v3 <http://www.gnu.org/licenses/>

  Copyright (C) 2019-2020 Andrade Echarry -> 'ALF'. All rights reserved.

"""

#--------------------------------------------------------------------------------------------------

# NOTA : este modulo falta por documentación, soy de esos informáticos raros que le da fastidio comentar código, ya que simplemente no los necesita para escribir, leer y re-escribir.

#--------------------------------------------------------------------------------------------------

import ctypes, os, sys

#-------------------------------------------------------------------------

class ClassName(object):

    def __init__(self):
        super(ClassName, self).__init__()

    @staticmethod
    def encode(string, encoding='utf-8', errors='strict'):

        if encoding == "hexadecimal":
            return ClassName().convertBin(string)

        if encoding == "web-image":
            import base64
            if sys.version_info[0] < 3:
                return 'data:image;base64,%s' % (base64.b64encode(string))
            else:
                return 'data:image;base64,%s' % (str(base64.b64encode(string), "utf-8"))

        if encoding == "web-url":

            import urllib

            path = string

            if sys.version_info[0] > 2:
                import urllib.parse
                import urllib.request
                path = os.path.abspath(path)
                return 'file:' + urllib.request.pathname2url(path)
            else:
                from urllib import pathname2url
                path = os.path.abspath(path)
                return 'file:' + pathname2url(path)

        return string.xencode(encoding, errors)

    @staticmethod
    def decode(string, encoding='utf-8', errors='strict'):

        if encoding == "hexadecimal":
            dockerY = NameSpace()
            string = "dockerY.xdecode = '%s'" % (string)
            exec (compile(string, "<string>", "exec"))
            return dockerY.xdecode

        if sys.version_info[0] > 2:
            return string
        else:
            return string.xdecode(encoding, errors)


    @staticmethod
    def convertBin(c):
        lista  = list("\n\t\r\a\f\v\b")
        chain  = c
        result = ""
        for char in chain:
            if not char in lista:
                result+="\\x" + "{0:x}".format(ord(char))
            else:
                result+=repr(char).replace("'","")
        return result


    @staticmethod
    @property
    def len_bytes(chain):
        try:
            return len(str(chain))
        except:
            return len(chain)

    @staticmethod
    @property
    def tipo_obj(self):
        import inspect
        if inspect.isclass(self): return "class"
        if inspect.isfunction(self): return "function"
        if inspect.ismethod(self): return "method"
        if inspect.ismodule(self): return "module"
        if inspect.isbuiltin(self): return "builtin"
        if inspect.isgenerator(self): return "generator"
        return type(self)

    @staticmethod
    @property
    def any(self):
        return any(self)


    @staticmethod
    @property
    def to_hash(self): return hash(self)


    @staticmethod
    def bytesPeso(archivo):
        if not type(archivo) in (int, float, type(0xAA17B0A5)):
            archivo = len(archivo)

        suffixes = ['BYTES', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while archivo >= 1024 and i < len(suffixes) - 1:
            archivo /= 1024.
            i += 1
        if suffixes[i] == 'BYTES':
            f = str('%.0f' % archivo)
        else:
            f = str('%.2f' % archivo)[0:-1]
        return (f, suffixes[i])


    @staticmethod
    def Get_memory_size(data_obj, bytes_=False):
        result = sys.getsizeof(data_obj)
        return result if bytes_ else result.size().join(" ")


    @staticmethod
    def to_float(obj, maxi=False):

        if not type(obj) in (float, int):
            obj = float(obj)

        if not maxi == False:
            dockerZ_SUKIII = NameSpace()
            exec ('dockerZ_SUKIII.x = float("%.' + str(maxi) + 'f" % (obj))')
            return dockerZ_SUKIII.x
        else:
            return float(obj)

    @staticmethod
    def to_xfloat(obj):

        obj = int(str(obj).replace(".", ""))

        def addComa(snum):
            s = snum
            i = s.index('.')
            while i > 3:
                i = i - 3
                s = s[:i] + ',' + s[i:]
            return s

        n = obj
        vale = '%s' % (addComa('%.2f' % (float(n))))
        if vale[-3:] == ".00":
            vale = vale[:-3].replace(",", ".")

        return vale


    @staticmethod
    @property
    def toNumber(string):
        try:
            return int(string)
        except ValueError:
            return string.float(len(string))


    @staticmethod
    @property
    def toString(number): return str(number)

    @staticmethod
    def toPositive(cadena):
        string = str(cadena).Replace("-")
        try:
        	try:
        		return int(string)
        	except ValueError:
        		return string.float(len(string))
        except:
        	return cadena

    @staticmethod
    def toReverse(cadena):

        number = False
        if type(cadena) in (int, float, type(0xCC4336DA),):
            number = True
            cadena = str(cadena)

        if type(cadena) in (list, tuple):
            return [token for token in reversed(cadena)]

        tmp = ""
        for token in reversed(cadena):
            tmp+=token

        if number: return tmp.toN

        return tmp


    @staticmethod
    def toNegative(cadena):
        string = "-" + str(cadena)
        try:
            try:
                return int(string)
            except ValueError:
                return string.float(len(string))
        except:
            return cadena

    @staticmethod
    def toSeconds(valor):
        from decimal import Decimal
        total = 0x0
        h = valor.split(':')[0]
        total += 60 * 60 * Decimal("%.0f" % int(h))
        m = valor.split(':')[1]
        total += 60 * Decimal("%.0f" % int(m))
        s = valor.split(':')[2]
        total += Decimal("%.0f" % int(s.split('.')[0]))
        total = str(total)
        segundos = total.split('.')[0]

        try:
        	segundos = int(segundos) + ( float( '0.'+ valor.split('.')[1] ) )
        except:
        	segundos = int(segundos)

        return segundos

    @staticmethod
    def toHms(valor, mode=False):
        import math as Math;

        def modo_avanzado(seconds):
            try:
               long
            except:
               long = int
            seconds = long(round(seconds))
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)
            years, days = divmod(days, 365.242199)

            minutes = long(minutes)
            hours = long(hours)
            days = long(days)
            years = long(years)

            duration = []
            if years > 0:
                duration.append('%d año' % years + 's'*(years != 1))
            else:
                n1 = 0
                if days > 0:
                    duration.append('%d dia' % days + 's'*(days != 1))
                    n1 = 1

                n2 = 0
                if hours > 0:
                    if n1 == 1:
                      duration.append('con %d hora' % hours + 's'*(hours != 1))
                    else:
                      duration.append('%d hora' % hours + 's'*(hours != 1))
                    n2 = 1

                n3 = 0
                if minutes > 0:
                    if n2 == 1:
                      duration.append('y %d minuto' % minutes + 's'*(minutes != 1))
                    else:
                      duration.append('%d minuto' % minutes + 's'*(minutes != 1))
                    n3 = 1

                if seconds > 0:
                    if n3 == 1:
                      duration.append('con %d segundo' % seconds + 's'*(seconds != 1))
                    else:
                      duration.append('%d segundo' % seconds + 's'*(seconds != 1))

            return ' '.join(duration)

        if mode:
        	return modo_avanzado(valor)

        def pad(self):
        	return self if self > 9 else "0" + str(self)

        return [
        pad(int(valor / 3600)),
        pad(int(valor % 3600 / 60)),
        pad(int(valor % 60)),
        ].join(':');

    @staticmethod
    def toMs(seconds):
    	return int(seconds * 1000)

    @staticmethod
    def toNs(seconds):
    	return int(seconds * 1000000000)

    @staticmethod
    @property
    def toFormat(string, objecto=0x03E5146A):
        import re
        isDict = False
        isNULL = False

        recompilar = re.compile(r"(\$[a-z|~|A-Z|-|_|0-9]+)\$")
        lista_BSA = recompilar.findall( string )
        if any(lista_BSA):
            for item in lista_BSA:
                ruta = SystemVars(item)
                if ruta: string = string.replace(item+"$", ruta)

        recompilar = re.compile(r"(\$[a-z|~|A-Z|-|_|0-9]+)?$")
        lista_BSA = recompilar.findall( string )
        if any(lista_BSA):
            for item in lista_BSA:
                ruta = SystemVars(item)
                if ruta: string = string.replace(item, ruta)

        try:
            caller = sys._getframe(1)
        except ValueError:
            Locals = sys.__dict__
            Globals = sys.__dict__
        else:
            Locals = caller.f_locals # f_locals, f_globals
            Globals = caller.f_globals

        if objecto==0x03E5146A:
            isNULL = True
            objecto = Locals

        if not type(objecto) == dict:
            if hasattr(objecto, "__dict__"):
                objecto = objecto.__dict__
            else:
                objecto = {}
        else:
            dict_new = {}
            isDict = True
            ORIGINAL_dict = objecto
            for objecto in ORIGINAL_dict.values():
                if hasattr(objecto, "__dict__"):
                    dict_new.update(objecto.__dict__)
            if any(dict_new):
                objecto = dict_new

            recompilar = re.compile(r"{(.*?)}")
            lista = recompilar.findall( string )
            if not any(lista): return string

            valid = 0
            if isDict:
                for item in lista:
                    data_method = item.cut(".", delete=False, start=1, end=1)
                    if type(data_method) == list:
                        if data_method[1] == ".":
                            item = data_method[0]
                    for objec_tpmZxhip in ORIGINAL_dict.keys():
                        if objec_tpmZxhip == item: valid += 1

                if valid != 0x0:
                    objecto = ORIGINAL_dict

            STRING_topic = string
            NADA_parse = False
            NEY = False

            var_method_active = False

            for item in lista:

                REAL_bytes = item

                data_method = item.cut(".", delete=False, start=1, end=1)
                if type(data_method) == list:
                    if data_method[1] == ".":
                        var_method_active = True
                        Xitem = "{%s}" % (item)
                        item = data_method[0]

                start = "{%s}" % (item)


                if not item in objecto:
                    if not item in dict_new:
                        end = "?"
                        for key, value in ORIGINAL_dict.items():
                            if type(value) == dict:
                                for key2, value2 in value.items():
                                    if item == key2: end = value2
                    else:
                        end =  dict_new[item]
                    NADA_parse = True
                else:
                    end =  objecto[item]

                import inspect


                if end == "?":
                    try:
                        active = True
                        cupperDEsZZ      = NameSpace()
                        cupperDEsZZ.neo  = False
                        A, B = STRING_topic.cut(["{", "}"])
                        A, B = B.split("(")
                        cupperDEsZZ.data = ORIGINAL_dict[A]
                    except Exception as cuca:
                        # print cuca
                        active = False

                    if active:
                        cmd = "try: cupperDEsZZ.neo = cupperDEsZZ.data(%s\nexcept: pass" % (B)
                        # print cmd
                        exec (cmd)
                        if cupperDEsZZ.neo:
                            end = cupperDEsZZ.neo







                if end == "?":
                    try:
                        active = True
                        cupperDEsZZ      = NameSpace()
                        cupperDEsZZ.neo  = False
                        A, B = item.split("(")
                        cupperDEsZZ.data = ORIGINAL_dict[A]
                    except Exception as cuca:
                        # print cuca
                        active = False

                    if active:
                        cmd = "try: cupperDEsZZ.neo = cupperDEsZZ.data(%s\nexcept: pass"
                        exec (cmd)
                        # print cmd
                        # exit()
                        if cupperDEsZZ.neo:
                            end = cupperDEsZZ.neo


                if var_method_active:
                    method_add = data_method[2]
                    cupperDEsZZ = NameSpace()
                    cupperDEsZZ.data = end
                    cmd = "cupperDEsZZ.neo = cupperDEsZZ.data.%s" % (method_add)
                    exec (cmd)
                    end = cupperDEsZZ.neo
                    var_method_active = False
                    string = string.replace(Xitem, str(end).Format)
                    continue
                else:
                    if inspect.isfunction(end):
                        cmd = "cupperDEsZZ.neo = cupperDEsZZ.data.%s" % (data_method[2])
                        end = end()
                        # print "YES"

                string = string.replace(start, str(end).Format)

        return string

#-------------------------------------------------------------------------

#### generando los correspondientes métodos... ####

#-------------------------------------------------------------------------

# S.encode(encoding='utf-8', errors='strict')
# funct_oring_encode = Get_Builtin_object(str)["encode"]

# B.decode(encoding='utf-8', errors='strict')
# funct_oring_decode = Get_Builtin_object(bytes)["decode"]

BYTES = b""
STR   = ""
UNi   = u""

CPythonBuiltin.create(
    ((str, int, float, bytes, list, tuple), "len", ClassName().len_bytes),

    ((type(STR), type(UNi), type(BYTES),), "Format", ClassName().toFormat),

    ((type(STR), type(UNi), type(BYTES),), "toSeconds", ClassName().toSeconds),
    ((int, float,), "toHms", ClassName().toHms),
    ((int, float,), "toMs", ClassName().toMs),
    ((int, float,), "toNs", ClassName().toNs),


    ((int, float, str, ), "float", ClassName().to_float),
    ((int, float, str, ), "xfloat", ClassName().to_xfloat),

    ((UNi, STR, BYTES,), "hash", ClassName().to_hash),

    # ((str, bytes,), "xencode", funct_oring_encode),
    # ((str, bytes,), "encode", ClassName().encode),

    # ((str,), "xdecode", funct_oring_decode),
    # ((str,), "decode", ClassName().decode),

    ((str, bytes, int, float, list, tuple), "size", ClassName().bytesPeso),

    ((str, bytes, int, float, list, tuple, dict),
        "memory_size", ClassName().Get_memory_size),

    ((str, bytes, list, tuple,), "any", ClassName().any),
)

def functActivateFutureType():
    CPythonBuiltin.create(((object,), "type", ClassName().tipo_obj),)

builtin_instance.Get_ObjectsTypes = functActivateFutureType


if sys.version_info[0] < 3:
    # funct_oring_encodeU = Get_Builtin_object(unicode)["encode"]
    # funct_oring_decodeU = Get_Builtin_object(unicode)["decode"]

    CPythonBuiltin.create(
        ((unicode, long,), "len", ClassName().len_bytes),
        ((unicode, long,), "type", ClassName().tipo_obj),

        ((unicode, long, ), "size", ClassName().bytesPeso),

        ((unicode, long, ),
            "memory_size", ClassName().Get_memory_size),

        ((long,), "xfloat", ClassName().to_xfloat),

        # ((str, bytes,), "xencode", funct_oring_encode),
        # ((str, bytes,), "xencode", funct_oring_encode),

        # ((unicode,), "xencode", funct_oring_encodeU),

        # ((bytes,), "xdecode", funct_oring_decode),

        # ((unicode,), "xdecode", funct_oring_decodeU),

        # ((unicode, bytes,), "decode", ClassName().decode),

        ((unicode,), "any", ClassName().any),
    )

#-------------------------------------------------------------------------

### metodo "to"
CPythonBuiltin.create(
    ((type(STR), type(UNi), type(BYTES),), "toF", ClassName().toFormat),
    ((type(STR), type(UNi), type(BYTES),), "toN", ClassName().toNumber),
    ((int, float, 0xCC4336DA, str, BYTES, UNi,), "toS", ClassName().toString),

    ((int, float, 0xCC4336DA, str, BYTES, UNi,), "toPositive", ClassName().toPositive),
    ((int, float, 0xCC4336DA, str, BYTES, UNi,), "toNegative", ClassName().toNegative),


    ((type(STR), type(UNi), type(BYTES), list, tuple,), "toReverse", ClassName().toReverse),
    ((int, float, type(0xCC4336DA), str, BYTES, UNi,), "toReverse", ClassName().toReverse),
)
