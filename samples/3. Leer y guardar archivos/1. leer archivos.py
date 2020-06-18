# coding: utf-8

todo = "archivos - leer.py".path.read() # lee todo el archivo y lo cierra automáticamente

#-------------------------------------------------------------------------

bytes = "../imagen.jpeg".path.read() # DelosEngine es productivo, ya que lee de manera automática archivos planos y binarios ¡sin que especifiques que tipo de archivo es!

#-------------------------------------------------------------------------

bytes = "../imagen.jpeg".path.read(48).close() # lee los primeros (48) bits del archivo

#-------------------------------------------------------------------------

linea15 = "archivos - leer.py".path.read(line=15) # leer linea 15 de este archivo

#-------------------------------------------------------------------------

# lectura continuada (ejemplo 1)

lector, leido1 = "archivos - leer.py".path.read(400)
lector, leido2 = lector.read(200)
lector.close()

#-------------------------------------------------------------------------

# lectura continuada (ejemplo 2)

lector, leido1 = "archivos - leer.py".path.read(400)
leido2 = lector.read(200).close()

#-------------------------------------------------------------------------

"""

// capturar métodos del (File Objects native Python) //

>> instancia = "archivos - leer.py".path.read(True)
>> objeto = instancia.instance # capturando objeto deseado
>> print (objeto) # imprimiendo objeto

"""
