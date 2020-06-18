# coding: utf-8

#--------------------------------------------------------------------------------------------------

### mejora del metodo (replace) del objeto (str|bytes|unicode)

# el metodo (Replace) soporta : str | unicode

print (
  "hola mundo".Replace(" ") # eliminar todos los espacios
  )

print (
  "hola mundo".Replace(" ", "@") # remplazar todos los espacios por (@)
  )

print (
  "hola mundo\tcomo estas".Replace([" ", "\t"], "-") # remplazar todos los espacios y tabulados por (-)
  )

print (
  "hola mundo como estas\tvale\tvale".Replace([" ", "\t"], "-", maxi=1) # remplazar la primera concurrencia de un espacio y tabulado por (-)
  )

print (
  "hola mundo como estas\tvale\tvale".Replace([" ", "\t"], "-", maxi=[2,1]) # remplazar las dos primeras concurrencias de un espacio por (-) y remplazar la primera concurrencia de un tabulado por (-)
  )

print (
  "hola mundo como estas\tvale\tvale".Replace([" ", "\t"], "-", maxi=[-1,1]) # remplazar todas las concurrencias de un espacio por (-) y remplazar la primera concurrencia de un tabulado por (-)
  )

#--------------------------------------------------------------------------------------------------

### convertir una lista a string mediante un delimitador

lista = []
for pointer in range(100):
  lista+=[pointer]

print (lista.join("|"))

#--------------------------------------------------------------------------------------------------

### soporte para remplazar un item de una lista

lista = ["ID", "MODE", "CHUCK"]

bobo = ["hola", 20, 99, 6, "neo", "morfeo"]

print (
  lista.replace(1, bobo)
  )

#--------------------------------------------------------------------------------------------------

print (
  lista.replace("ID", "identification")
  )
