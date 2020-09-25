# coding: utf-8

cadena = "hola mundo"
print (cadena.size())

# ----------------------------------------------------------------------------

cadena = 256**3
print (cadena.size())

# ----------------------------------------------------------------------------

neo = [1, 2, 3, 4]

print (neo.memory_size())

print ("hello world".memory_size())

print ("hello world".memory_size(True))

print (__file__.path.read().memory_size(True))

print (__file__.path.read().memory_size())
