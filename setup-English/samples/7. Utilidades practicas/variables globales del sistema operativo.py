# coding: utf-8

#### Función inteligente para extraer variables globales del sistema. ####

# extrayendo directorio de configuracion de programas para (windows y Unix)
windows = "%APPDATA%"
unix = "~"
Appdata = SystemVars(windows, unix)
print (Appdata)
