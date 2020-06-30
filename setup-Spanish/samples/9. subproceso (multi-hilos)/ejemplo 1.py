# coding: utf-8

# funcion a utilizar para el (sub-proceso independiente)
def funcion(self, startNumber, endNumber):
    for number in xrange(startNumber, (endNumber+1)):
        self.concurrente=number
        Sleep(0.8)
    Sleep(0.5)

#-------------------------------------------------------------------------------------------------

# creando espacio de trabajo
espacio = NameSpace()
espacio.concurrente = False
espacio.inicio = 1
espacio.final = 4
espacio.anterior = False

#-------------------------------------------------------------------------------------------------

# ejecutando funcion en un (sub-proceso independiente) -> set_thread(function, *args)
instancia = set_thread(funcion, espacio, espacio.inicio, espacio.final)
instancia.start()

#-------------------------------------------------------------------------------------------------

# monitorizar (sub-proceso independiente)
while True:
    if espacio.concurrente:

        if espacio.anterior != espacio.concurrente:
            Sleep(espacio.concurrente, 0.5)
            espacio.anterior = espacio.concurrente

            if espacio.concurrente == espacio.final:
                exit ("Conteo terminado...", 0.8)
