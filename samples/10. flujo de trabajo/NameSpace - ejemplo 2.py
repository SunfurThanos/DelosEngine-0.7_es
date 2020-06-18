# coding: utf-8

def funcion_prueba1(self):
    sistema = GetSystem()
    diccionario = {
        "system" : sistema["system"],
        "architecture" : sistema["architecture"],
        "driver" : self.driver
    }
    return diccionario

#-------------------------------------------------------------------------

@property
def funcion_prueba2(self):
    return self.mensaje_movie.Format

#-------------------------------------------------------------------------

espacio = NameSpace()
espacio.driver = "GpuNvidia GTX 5080"
espacio.mensaje_movie = "the matrix, is film on {Age}"
espacio.Age = 1999

#-------------------------------------------------------------------------

espacio.include(funcion_prueba1)
espacio.include(funcion_prueba2)

#-------------------------------------------------------------------------

print (espacio.funcion_prueba1())
print (espacio.funcion_prueba2)


"""

#### funciones ¡Libres sin Tiranía :)! ####

En un "NameSpace" no solo puedes incluir de forma ordinaria funciones y valores, si no que ademas puedes emparentar funciones a la clase maestra del "NameSpace", esto permite como consecuencia que las funciones emparentadas puedan heredar el "self" de dicha clase, ¡haciendo que tu trabajo sea mas productivo e intuitivo!, por ejemplo puedes crear un archivo ".py" que contenga todas las funciones genéricas que luego puedes emparentar de forma genérica en todos los N "NameSpace" que hayas establecido...

Resumen : Te proporciona un código limpio, genérico y productivo

"""
