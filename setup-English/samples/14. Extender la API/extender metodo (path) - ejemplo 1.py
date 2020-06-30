# coding: utf-8

# función para el nuevo "sub:metodo" a crear
def funct_toC16(self):
    texto = self.property # "propiedad heredada de la clase (str.path)"
    return repr(texto.encode("utf-16"))

#--------------------------------------------------------------------------------------------------

# asignando un nuevo "sub-método" al método "str.path"
builtin_instance.setCustom_method_Path = [
    ("toC16", funct_toC16)
]

#--------------------------------------------------------------------------------------------------

# ejecutando nuestro "sub:metodo" creado
resultado = "hola mundo".path.toC16()
print (resultado)
