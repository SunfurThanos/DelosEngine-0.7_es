# coding: utf-8

##### Auto formateo de texto #####

"""

# Nota : esta herramienta es la mejora por mucho de la función nativa para string llamada "format" (formateo de cadenas de caracteres), el sistema puede ¡averiguar mágicamente! donde y cuales son los objetos involucrados en el formateo de texto deseado, con lo cual te puedes ahorrar una gran carga de trabajo ¡obteniendo un gran flujo de trabajo muy productivo y eficaz!, manteniendo la integridad de las distintas versiones de Python.

    * sintax sample
        - string.Format | string.toF

    *NOTA* : es compatible con Python 2.5 o superior ¡FULL compatibilidad!

"""

#--------------------------------------------------------------------------------------------------

#### ejemplo 1 ####
self = NameSpace()
self.intelModel = "Intel Core i7-8700K"
self.GpuNvidia = "NVIDIA GeForce GTX 2080"
self.emotion = "xD"
self.cores = 87

print ("CPU : {intelModel} | GPU : {GpuNvidia} / Cores : {cores}".Format)
print

#--------------------------------------------------------------------------------------------------

#### ejemplo 2 ####
CondorDracula = {"cpu_temp": 86.3, "disc_temp": 54}

print ("CPU temperatura: {cpu_temp} C / disco temperatura: {disc_temp} C".Format)
print

#--------------------------------------------------------------------------------------------------

#### ejemplo 3 ####
nombre_user = "Condorito"
OSsystem = "Skynet Luc/7"

print ("Estimado Sr. {nombre_user}, su sistema {OSsystem} y {GpuNvidia}...".Format)
print

#--------------------------------------------------------------------------------------------------

#### ejemplo 4 ####
centavos = (50000).xfloat()
activate_oferta = True
oferta = ", !Oferta! {emotion}" if activate_oferta else ""
producto = "queso palmito"
promo = "El {producto} cuesta"

print ("Sr. {nombre_user} {promo} {centavos} Bs{oferta}".Format)
print

#--------------------------------------------------------------------------------------------------

#### ejemplo 5 ####

def funcion_suma():
	return 2+2

cadena = "hola mundo"
print ("esta cadena '{cadena}' tiene una longitud: {cadena.len}".toF)
print
print ("la suma es: '{funcion_suma}' / creada en la funcion: '{funcion_suma.__name__}'".toF)
print

#--------------------------------------------------------------------------------------------------

#### ejemplo 6 (variables globales del sistema operativo) ####

if isWindows:
	print ("$APPDATA".toF)
else:
	print ("$~".toF)


if isWindows:
	print ("$APPDATA$ | hello world | {nombre_user}".toF)
else:
	print ("$~$ | hello world | {nombre_user}".toF)
