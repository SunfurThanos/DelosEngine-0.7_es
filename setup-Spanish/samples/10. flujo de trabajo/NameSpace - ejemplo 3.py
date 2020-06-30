# coding: utf-8

def funct_saludar(self):
    self.saludos += 1
    return self.saludo.toF

#-------------------------------------------------------------------------

class ClassName:
    def __init__(self):
        self.conteoM = 0
        self.saludos = 0
        self.textoM  = "the matrix {conteoM}"
        self.saludo  = "hola mundo {saludos}"

    @property
    def Contar(self):
        self.conteoM += 1
        return self.textoM.toF

    def despedida(self):
        return "\nAdios mundo cruel :)"

#-------------------------------------------------------------------------

clase_a_unir = ClassName()

#-------------------------------------------------------------------------

espacio = NameSpace()

#-------------------------------------------------------------------------

espacio.include(
    clase_a_unir,
    funct_saludar
)

#-------------------------------------------------------------------------

Sleep (espacio.Contar, 0.4)
Sleep (espacio.Contar, 0.4)
Sleep (espacio.Contar, 0.4)

#-------------------------------------------------------------------------

print ("")

#-------------------------------------------------------------------------

Sleep (espacio.funct_saludar(), 0.4)
Sleep (espacio.funct_saludar(), 0.4)
Sleep (espacio.funct_saludar(), 0.4)

#-------------------------------------------------------------------------

exit (espacio.despedida(), 0.8)
