# coding: utf-8

@property
def Func_custom(self):
    return self.property.encode("hexadecimal")

#--------------------------------------------------------------------------------------------------

builtin_instance.setCustom_method_Path = [
    ("toHex", Func_custom)
]

#--------------------------------------------------------------------------------------------------

resultado = "hello world".path.toHex
print (resultado)
