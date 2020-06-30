# coding: utf-8

#### crear una funcion del "Built-in" ####

def funct_verCodigo_archivo(): return __file__.path.read()

#--------------------------------------------------------------------------------------------------

# agregando funcion al "Built-in"
builtin_instance.getFileCode = funct_verCodigo_archivo

# representando el nombre para esta funcion
getFileCode.func_name = "## lector de codigo MAIN ##"

# agregando documentacion
getFileCode.func_doc  = """
\t
getFileCode()

Permite leer el codigo del Script "MAIN" de tu aplicación.
"""

#--------------------------------------------------------------------------------------------------

# imprimiendo nombre de la funcion
print (getFileCode)

# imprimiendo documentación
print (getFileCode.__doc__)

# ejecutando función
print (getFileCode())
