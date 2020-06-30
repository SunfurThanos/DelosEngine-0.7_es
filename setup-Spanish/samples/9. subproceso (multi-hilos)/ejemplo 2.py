# coding: utf-8

# funcion a utilizar para el (sub-proceso independiente), usando un decorador
class ClassMaestra(object):

    def __init__(self):
        super(ClassMaestra, self).__init__()
        self.concurrente = False
        self.inicio = 1
        self.final = 5
        self.anterior = False

    @threaded
    def funcion(self):
        for number in xrange(self.inicio, (self.final+1)):
            self.concurrente=number
            Sleep(0.8)
        Sleep(0.5)

#-----------------------------------------------------------------------------------------------

# creando espacio de trabajo
espacio = ClassMaestra()

#-----------------------------------------------------------------------------------------------

# ejecutando funcion en un (sub-proceso independiente)
espacio.funcion()

#-----------------------------------------------------------------------------------------------

# monitorizar (sub-proceso independiente)
while True:
    if espacio.concurrente:

        if espacio.anterior != espacio.concurrente:
            Sleep(espacio.concurrente, 0.5)
            espacio.anterior = espacio.concurrente

            if espacio.concurrente == espacio.final:
                exit ("Conteo terminado...", 0.8)
