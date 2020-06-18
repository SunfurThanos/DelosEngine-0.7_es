# coding: utf-8

# b"q"    = q
# b"\x03" = ctrl+c

if not isConsole: exit("Ejecute este script en una consola :)")

while True:
    print ("presione la tecla (q) o (ctrl+c) para salir...")
    if console.event() in (b"q", b"\x03"): exit()
