# coding: utf-8

##### agregar una funcion pero con un nombre distinto #####

@property
def get_size_ZGHSSSD_uasdudas377ja(self):
    return 256**4

docker = NameSpace()
docker.include({"get_size":get_size_ZGHSSSD_uasdudas377ja})

valor = docker.get_size
print (valor)

#--------------------------------------------------------------------------------------------------

##### agregar una clase como un metodo independiente + un nombre distinto #####

class ClassName(object):
    def __init__(self, arg=False):
        super(ClassName, self).__init__()
        self.arg = arg

    def justicia(self):
        return "vivimos para luchar otro dia..."

docker = NameSpace()
docker.include({"clase_justicia":ClassName})

clase = docker.clase_justicia()
valor = clase.justicia()
print (valor)

#--------------------------------------------------------------------------------------------------

##### agregar una clase como un metodo independiente, conservando el nombre original #####

class ClassName(object):
    def __init__(self, arg=False):
        super(ClassName, self).__init__()
        self.arg = arg
        self.pais = ""

    def justicia(self):
        return "vivimos para luchar otro dia... {pais}".toF

docker = NameSpace()
docker.include({False:ClassName})

clase = docker.ClassName()
clase.pais = "***"
valor = clase.justicia()
print (valor)
