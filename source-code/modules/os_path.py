# coding: utf-8

#--------------------------------------------------------------------------------------------------

"""
  Autor: Andrade Echarry -> 'ALF'

  Pais : Venezuela

  Uso : mejora y simplificación de (os + shutil)

  Licencia : GNU GPL v3 <http://www.gnu.org/licenses/>

  Copyright (C) 2019-2020 Andrade Echarry -> 'ALF'. All rights reserved.

"""

#--------------------------------------------------------------------------------------------------

# NOTA : este modulo falta por documentación, soy de esos informáticos raros que le da fastidio comentar código, ya que simplemente no los necesita para escribir, leer y re-escribir.

#--------------------------------------------------------------------------------------------------

import ctypes, os, sys

#--------------------------------------------------------------------------------------------------

### glob ###
class Class_os_path_GLOB(object):
	def __init__(self, arg):
		super(Class_os_path_GLOB, self).__init__()
		self.property = arg

	def buscar_patron(self, path, goto):
		import re
		goto = goto.replace(".","\.").replace("*",".*")
		recompilar  = re.compile(goto)
		return any(
				recompilar.findall( path.unicode() )
			)

	def find(self, pattern=False):

		if pattern == False:
			# self.property = self.property.path.normalize
			pattern   = self.property.path.file
			self.property = self.property.path.dir

		if not type(pattern) == list: pattern = [pattern]

		for item in os.listdir(self.property):
			path = os.path.join(self.property, item)
			for goto in pattern:
				if self.buscar_patron(path, goto):
					yield path

#--------------------------------------------------------------------------------------------------

### os.listdir ###
class Class_os_path_while_listdir(object):
	def __init__(self, arg):
		super(Class_os_path_while_listdir, self).__init__()
		self.property = arg

	def get_listdir(self):
		for item in os.listdir(self.property):
			path = os.path.join(self.property, item)
			yield path

#--------------------------------------------------------------------------------------------------

class Class_os_path_custom(object):
	def __init__(self, arg=0x492F4B61):
		super(Class_os_path_custom, self).__init__()
		self.arg = arg

	@staticmethod
	@property
	def SunfurX(text):

		def get_mimetype(file, data=False):
			bufsize = 512

			if not data:
				data = open(file, "rb").read(bufsize)
			else:
				data = data[:bufsize]

			char = list('\n\t\r\x08')
			for cursor in range(31, 196):
				char+=[chr(cursor)]

			if data!='':
				for elem in data:
					try:
						elem = ord(elem)
					except: pass
					if not chr(elem) in char:
						return "BINARY"
			else:
			     return 'VACIO'

			return 'PLAIN'

		class JhonKonnor(object):
			def __init__(self):
				super(JhonKonnor, self).__init__()
				self.property = text

				clase1 = Class_os_path_while_listdir(self.property)
				self.listdir = clase1.get_listdir

				clase2 = Class_os_path_GLOB(self.property)
				self.find = clase2.find

				if any(setCustom_method_Path):

					for name, extruct in setCustom_method_Path:

						# if type(extruct) != property:
						# 	extruct.callback = self.property
						# else:
						# 	extruct.fget.callback = self.property

						setattr(
							self.__class__, name,
							extruct
						)


			def ejecutar_userMetodo(self, funcion):
				funcion()


			@property
			def size(self):
				file = self.property

				def FilePeso(archivo):
					suffixes = ['BYTES', 'KB', 'MB', 'GB', 'TB', 'PB']
					i = 0
					while archivo >= 1024 and i < len(suffixes)-1:
					     archivo /= 1024.
					     i += 1
					if suffixes[i] == 'BYTES':
						f = str('%.0f' % archivo)
					else:
						f = str('%.2f' % archivo)[0:-1]
					return (f, suffixes[i])


				class JhonKonnor:
					@property
					def value(self):
						if not os.path.isfile(file): return False
						return os.path.getsize(file)

					@property
					def info(self):
						if not os.path.isfile(file): return False
						return FilePeso(os.path.getsize(file))

				return JhonKonnor()




			@property
			def open(self):
				file = self.property

				def Open_path(PATH, optionXXX):
					import subprocess
					cmd = ['explorer.exe']
					if optionXXX:
						cmd += [optionXXX]
					cmd += [PATH]

					subprocess.Popen\
					(
						cmd,

						creationflags=0x00000008
					);

				class JhonKonnor(object):
					def __init__(self, arg):
						super(JhonKonnor, self).__init__()
						self.archivo = arg

					def startfile(self, file):
						import subprocess
						if sys.platform.startswith('darwin'):
						    subprocess.call(('open', file))
						elif os.name == 'nt':
						    os.startfile(file)
						elif os.name == 'posix':
						    subprocess.call(('xdg-open', file))

					def file(self):
						if not os.path.isfile(self.archivo): return False
						self.startfile(self.archivo)
						return True

					def dir(self):
						if os.path.isfile(self.archivo):
							self.archivo = os.path.split(self.archivo)[0]
						else:
							if not os.path.isdir(self.archivo): return False
						self.startfile(self.archivo)
						return True

					def explorer(self):
						if not os.path.isfile(self.archivo):
							if not os.path.isdir(self.archivo):
								return False

						optionXXX = '/select,'
						if os.path.isdir(self.archivo): optionXXX = False


						if os.name == 'nt':
							Open_path(self.archivo, optionXXX)
						else:
							return False

						return True

				return JhonKonnor(file)




			def delete(self): # borrar archivos y carpetas en modo recusivo
				archivo = self.property; import shutil

				if not os.path.isfile(archivo):
					if not os.path.isdir(archivo):
						return False

				if os.path.isfile(archivo):
					try:
						os.remove(archivo)
					except:
						return False

				if os.path.isdir(archivo):
					try:
						shutil.rmtree(archivo)
					except:
						return False

				return True

			@property
			def autocomplete(self):
				SUMA = []
				anterior = False
				data = self.property.path.normalize
				RAIZ = data.cut("*")

				if type(data.path.normalize.cut("*")) != list: return False

				for item in RAIZ:
				    if anterior == False:
				        anterior = item
				    else:
				        if not anterior == False:
				            if not any(SUMA):
				            	if anterior.path.isExist:
				                	for dir in anterior.path.listdir():
				                	    rutita = (dir + item).path.normalize
				                	    if rutita.path.isExist:
				                	        SUMA+=[rutita]
				            else:
				                TMP = []
				                for co_anterior in SUMA:
				                    try:
				                    	if co_anterior.path.isExist:
				                        	for dir in co_anterior.path.listdir():
				                        	    rutita = (dir + item).path.normalize
				                        	    if rutita.path.isExist:
				                        	        TMP+=[rutita]
				                    except:
				                        continue

				                if any(TMP):
				                    SUMA=TMP

				if len(SUMA) == 1: return SUMA[0]
				if not any(SUMA): return False
				return SUMA


			def copy(self, new):
				archivo = self.property; import shutil

				NEW = new

				if not os.path.isfile(archivo):
					if not os.path.isdir(archivo):
						return False

				if os.path.isdir(new):
					new = os.path.join(new, os.path.basename(archivo))

				if os.path.isfile(archivo):
					try:
						shutil.copyfile(archivo, new)
					except:
						return False

				if os.path.isdir(archivo):
					try:
						shutil.copytree(archivo.path.normalize, new.path.normalize)
					except:
						return False

				return True


			def rename(self, new):
				archivo = self.property

				if not os.path.isfile(archivo):
					if not os.path.isdir(archivo):
						return False

				os.rename(archivo, new)


			def move(self, new):
				archivo = self.property; import shutil

				if not os.path.isfile(archivo):
					if not os.path.isdir(archivo):
						return False

				if os.path.isdir(new):
					new = os.path.join(new, os.path.basename(archivo))

				try:
					shutil.move(archivo, new)
				except:
					return False

				return True


			@property
			def drive(self):
				archivo = self.property

				if not os.path.isfile(archivo):
					if not os.path.isdir(archivo):
						return False

				return os.path.splitdrive(archivo)[0]


			def mkdir(self):
				archivo = self.property
				try: os.mkdir(archivo)
				except: return False
				return archivo

			def mkdirs(self):
				archivo = self.property
				try: os.makedirs(archivo)
				except: return False
				return archivo


			@property
			def walkFile(self):
				for root, dirs, files in os.walk(self.property, topdown=False):
				    for name in files:
				    	archivo = root.path.join(name)
				    	yield root, archivo


			def save(self, data="", mode=False): # file_api (file->save)
				archivo = self.property

				if type(data) in (int, float, type(0xCC4336DA)): data = str(data)

				if not len(data) == 0:
					if type(data) in (str, bytes):
						type_data = get_mimetype(file=False, data=data) # "BINARY", 'PLAIN'
					else:
						if not type(data) == list:
							type_data = 'PLAIN'
						else:
							type_data = "LIST"
				else:
					type_data = 'PLAIN'

				fileFunct = ctypes.ClassFileApp_save(self, get_mimetype)
				fileFunct.run(archivo, data, type_data, mode)

				return fileFunct


			@property
			def iter(self):
				archivo = self.property

				if get_mimetype(archivo) == "BINARY":
					instance = open(archivo, "rb")

				if get_mimetype(archivo) in ('PLAIN', 'VACIO'):
					instance = open(archivo)

				for NUM, DATA in enumerate(instance):
					NUM+=1
					yield (NUM, DATA)


			def read(self, bufsize=False, line=False, lines=False): # file_api (file->read)
				archivo = self.property

				if not os.path.isfile(archivo): return False

				fileFunct = ctypes.ClassFileApp_read(self, get_mimetype)
				void = fileFunct.run(archivo, bufsize, line, lines)

				return void



			def join(self, *arg): return os.path.join(self.property, *arg)

			@property
			def isnull(self):
				if not os.path.isfile(self.property): return False
				return get_mimetype(self.property) == 'VACIO'

			@property
			def isbinary(self):
				if not os.path.isfile(self.property): return False
				return get_mimetype(self.property) == "BINARY"

			@property
			def istext(self):
				if not os.path.isfile(self.property): return False
				return get_mimetype(self.property) == "PLAIN"

			@property
			def isdir(self):
				return os.path.isdir(self.property)

			@property
			def isfile(self):
				return os.path.isfile(self.property)

			@property
			def isExist(self):
				return os.path.exists(self.property)


			@property
			def relative(self):
				try:
					return os.path.relpath(self.property)
				except:
					return self.property

			@property
			def normalize(self):
				return os.path.abspath(os.path.normpath(self.property))

			@property
			def isNormalize(self):
				return os.path.isabs(self.property)

			@property
			def isRelative(self):
				return not os.path.isabs(self.property)


			@property
			def file(self):
				return os.path.basename(self.property)

			@property
			def name(self):
				return os.path.splitext(os.path.basename(self.property))[0]

			@property
			def ext(self):
				extension = os.path.splitext(os.path.basename(self.property))[-1]
				if len(extension) != 0:
					if extension[0] == ".":
						extension = extension[1:]
				return extension

			def change_ext(self, new_ext):
				name = self.property.path.name
				ext  = self.property.path.ext
				dir = self.property.path.dir
				return dir.path.join(name+"."+new_ext)

			@property
			def dir(self):
				return os.path.split(self.property)[0]

		return JhonKonnor()

#--------------------------------------------------------------------------------------------------

builtin_instance.setCustom_method_Path = []
funcion    = Class_os_path_custom().SunfurX
name_space = "path"

#--------------------------------------------------------------------------------------------------

CPythonBuiltin.create(
	((str, bytes), name_space, funcion),
)

if sys.version_info[0] < 3:
	CPythonBuiltin.create(
		((unicode,), name_space, funcion),
	)

#--------------------------------------------------------------------------------------------------

### datos del sistema operativo ###

def func_GetSystem():
	def cpu_count():
	    if sys.platform == 'win32':
	        try:
	            num = int(os.environ['NUMBER_OF_PROCESSORS'])
	        except (ValueError, KeyError):
	            num = 0
	    elif sys.platform == 'darwin':
	        try:
	            num = int(os.popen('sysctl -n hw.ncpu').read())
	        except ValueError:
	            num = 0
	    else:
	        try:
	            num = os.sysconf('SC_NPROCESSORS_ONLN')
	        except (ValueError, OSError, AttributeError):
	            num = 0

	    if num >= 1:
	        return num
	    else:
	        return False

	system = {
	    "system": False,
	    "processor": False,
	    "architecture": False,
	    "cpu_count": False
	}

	import platform

	# system name
	system["system"] = platform.system()
	# processor
	system["processor"] = platform.processor()
	# architecture
	system["architecture"] = platform.machine()
	# cpu count
	system["cpu_count"] = cpu_count()

	return system

builtin_instance.GetSystem = func_GetSystem
builtin_instance.isWindows = sys.platform.startswith('win')
builtin_instance.isLinux   = sys.platform.startswith('linux')
builtin_instance.isMac     = sys.platform.startswith('darwin')

#--------------------------------------------------------------------------------------------------

### trabajando con variables globales del sistema operativo (environment variables) ###

def func_manipularEnvVars(*argumentos):

	def extractEnv_Windows(variable):
		copa1 = os.path.expandvars(variable)
		if copa1 != variable: return True, copa1
		return False, False

	def extractEnv_generic(variable):
		copa2 = os.path.expanduser(variable)
		if copa2 != variable: return True, copa2
		return False, False

	for item in argumentos:
		valid, result = extractEnv_Windows(item)
		if valid: return result

	for item in argumentos:
		valid, result = extractEnv_generic(item)
		if valid: return result

	return False

builtin_instance.SystemVars = func_manipularEnvVars
