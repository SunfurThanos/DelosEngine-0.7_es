
## crear ruta de (archivo|directorio) temporal con nombre fijo
ruta = TmpPath("data-sunfur.delos")
# print (ruta)

#--------------------------------------------------------------------------------------------------

## crear ruta de (archivo|directorio) temporal con nombre automatico
ruta = TmpPath("*.delos")
# print (ruta)

#--------------------------------------------------------------------------------------------------

## crear ruta de (archivo|directorio) temporal de forma automatica
ruta = TmpPath()
# print (ruta)

#--------------------------------------------------------------------------------------------------

## crear ruta de (archivo|directorio) temporal con nombre automatico y ruta personalizada
ruta = TmpPath("*.delos", dir="./")
# print (ruta)
