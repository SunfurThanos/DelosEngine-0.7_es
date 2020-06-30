# coding: utf-8

# delos.ignoreWarning = True

# creando un "warning"
mensaje = """
Mensaje : "Driver Q-Nvidia 15.02 x65" no se esta instalado, esto puede traer problemas de compatibilidad
Archivo : $file$
Linea   : $line$
"""
resultado = debug.warning(mensaje)
"registro de advertencias.txt".path.save(resultado, "+").close()



"""

Funcionamiento : la utilidad de "debug.warning" es mostrar advertencias "depuraciones" que puedan ser desactivadas durante la ejecución de un programa.



Desactivar : para desactivar un warning solo basta con modificar el valor de la variable "delos.ignoreWarning" a "True", esto sirve por si deseas hacer test sin los "warning", o si utilizas una API que tiene esos "warning" activado y no deseas que se muestren.

>> delos.ignoreWarning = True
>> debug.warning(mensaje)



NOTA : dado a que este tipo de warning puede ser modificado al 100%, también puede ser usado para depuraciones tipo "info"



Exportado : también es posible exportar el mensaje a un archivo externo, esto es útil por si tu aplicación es gráfica y compilada ".exe" :)

>> resultado = debug.warning(mensaje)
>> "registro de advertencias.txt".path.save(resultado).close()

"""
