# coding: utf-8

### leer 5 bytes desde una posición determinada ###

# genera la instancia de lectura
instancia = "cursor - guardar.py".path.read(True)

# coloca el cursor de lectura en el byte 10
instancia.cursor(10)

# lee solo 5 bytes desde la nueva posición del cursor
print (instancia.read(5).close())

#------------------------------------------------------------------------------------------------

### leer los primeros 8 bytes luego saltar a una nueva posición en el cursor ###

# lee los primeros 8 bytes
instancia, leido = "cursor - guardar.py".path.read(8)
print (leido)

# lee la posicion actual del cursor
print (instancia.get_cursor)

# salta al byte 10 y lee solo 5 bytes desde la nueva posición y cierra el archivo
print (instancia.read(10, 5).close())
