# coding: utf-8

# formateo de texto
numeros = "10000000096"
print ("cantidad: {numeros}".toF)

#--------------------------------------------------------------------------------------------------

# conversión de texto a numeros
numeros = "10000000096"
print (numeros.toN)

numeros = "0.438384223432"
print (numeros.toN)

#--------------------------------------------------------------------------------------------------

# conversión de numeros a texto
numeros = 10000000096
print (numeros.toS)

#--------------------------------------------------------------------------------------------------

# conversion de HMS a segundos
print ('00:00:56.17'.toSeconds())
print ('02:00:56'.toSeconds())

#--------------------------------------------------------------------------------------------------

# conversion de segundos a HMS
segundos = 7044.0
print (segundos.toHms())

segundos = 96443.5
print (segundos.toHms(True))

#--------------------------------------------------------------------------------------------------

# conversion de segundos a milisegundos
segundos = 0.029774
print (segundos.toMs())

#--------------------------------------------------------------------------------------------------

# conversion de segundos a nano-segundos
segundos = 0.031278
print (segundos.toNs())
