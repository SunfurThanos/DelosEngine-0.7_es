# coding: utf-8

# guardado sencillo de texto
"archivo Z.txt".path.save("hola mundo").close()

#--------------------------------------------------------------------------------------------------

# guardado sencillo de numeros
"numero de registro.txt".path.save(0xCC4336DA).close()

#--------------------------------------------------------------------------------------------------

# guardado continuado
archivo = "archivo.txt"
guardar = archivo.path.save("hola mundo")
guardar.save("\nvale vale nos vemos").close()

#--------------------------------------------------------------------------------------------------

# guardado continuado ¡sin sobre-escribir! (agrega nuevos bytes al final del archivo)
archivo.path.save(b", hola mundo 2", "+").close()

#--------------------------------------------------------------------------------------------------

# guardar una lista directamente en el archivo sin pasar por intermediarios

lista = []
for pointer in xrange(1, 300):
  lista+=[pointer]

"lista de texto.txt".path.save(lista).close()

#--------------------------------------------------------------------------------------------------

# guardar datos binarios (bytes) ¡DelosEngine es productivo, tanto para leer como para guardar! xD
dato_imagen = "../imagen.jpeg".path.read()
"imagen-copy.jpeg".path.save(dato_imagen).close()

#--------------------------------------------------------------------------------------------------

# crear un archivo vació, si el archivo no es cerrado "close()", se puede seguir escribiendo datos en el posteriormente, ya sea datos planos o binarios. ¡DelosEngine xD!
instancia = "archivo vacio.txt".path.save().close()

#--------------------------------------------------------------------------------------------------

# guardando continuado en multi-linea - ejemplo 1
instancia = "texto multi-linea 1.txt".path.save("[inicio de pagina xD]")

for numero in xrange(20):
    instancia.save("hola mundo %s" % (numero), line=True)

instancia.save("[fin de pagina xD]", line=True).close()

#--------------------------------------------------------------------------------------------------

# guardando continuado en multi-linea - ejemplo 2
instancia = "texto multi-linea 2.txt".path.save()

instancia.save("[inicio de pagina xD]", line="\n\n\n")

for numero in xrange(10):
    instancia.save("hola mundo %s" % (numero), line=True)

instancia.save("[fin de pagina xD]", line="\n\n\n\n").close()

#--------------------------------------------------------------------------------------------------

# asignando el tipo de escritura "encoding-bytes" de forma manual
"modo manual.txt".path.save("hola mundo", "w").close() # w, wb, a+, ...

#--------------------------------------------------------------------------------------------------


"""

// capturar métodos del (File Objects native Python) //

>> instancia = "archivo X-Men.txt".path.save()
>> objeto = instancia.instance # capturando objeto deseado
>> print (objeto) # imprimiendo objeto
>> print (objeto.mode) # verificando el modo de escritura activado (w, wb, a+, ...)

"""
