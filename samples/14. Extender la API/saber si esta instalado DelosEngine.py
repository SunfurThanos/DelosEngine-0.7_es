# coding: utf-8

msg_warning = "DelosEngine esta instalado pero no es Global (Built-in) :("
msg_error   = "No hay ninguna version de (DelosEngine) instalada :("
msg_info    = "DelosEngine si esta instalado :)"

#--------------------------------------------------------------------------------------------------

#### ejemplo 1 ####

print (msg_info if hasattr(__builtins__, "delos") else msg_error)

#--------------------------------------------------------------------------------------------------

#### ejemplo 2 ####

import inspect

valido = 0x000
if inspect.ismodule(eval('\x64\x65\x6c\x6f\x73')):
    valido = 0x001
    if not hasattr(__builtins__, '\x64\x65\x6c\x6f\x73'):
        mensaje_info = msg_warning
    else:
        mensaje_info = msg_info

print (mensaje_info if valido == 0x001 else msg_error)

# DESAFIO : ¡simplifica este ejemplo!

#--------------------------------------------------------------------------------------------------

#### ejemplo 3 ####

try: import DelosEngine; print (msg_info)
except ImportError: debug.error (msg_error)
