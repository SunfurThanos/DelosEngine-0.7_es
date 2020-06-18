# coding: utf-8

# autocompletar una ruta
ruta = "C:\Python26\*\site-packages\py2exe"
match = ruta.path.autocomplete

if type(match) is list:
    # multi busqueda
    for item in match:
        print (item)
else:
    # busqueda unitaria
    if match:
        print (match)
    else:
        # sin busqueda :(
        print ("no se pudo auto-completar")
