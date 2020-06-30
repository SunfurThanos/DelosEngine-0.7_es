# coding: utf-8

###### herramientas de corte ¡HIGH PERFORMANCE! ######

#--------------------------------------------------------------------------------------------------

resultado = "hola mundo como estas".cut(" ")

print (resultado)

#--------------------------------------------------------------------------------------------------

resultado = "hola mundo como estas".cut(" ", delete=False)

print (resultado)

#--------------------------------------------------------------------------------------------------

resultado = "hola mundo como estas".cut(" ", delete=False, start=2)

print (resultado)

#--------------------------------------------------------------------------------------------------

resultado = "hola mundo como estas Vlz".cut(" ", delete=False, start=2, end=2)

print (resultado)

#--------------------------------------------------------------------------------------------------

entrada = """
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf58.7.100
  Duration: 00:03:24.22, start: 0.000000, bitrate: 511 kb/s
    Stream #0:0(und): Video: h264 (Constrained Baseline) (avc1 / 0x31637661), yuv420p(tv, bt709), 640x360 [SAR 1:1 DAR 16:9], 408 kb/s, 29.97 fps, 29.97 tbr, 30k tbn, 59.94 tbc (default)
    Metadata:
      handler_name    : VideoHandler
    Stream #0:1(eng): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 96 kb/s (default)
    Metadata:
      handler_name    : SoundHandler
At least one output file must be specified

"""

resultado = entrada.cut("\n").getIn("Duration:").cut(",")\
.cut(":", delete=False, group=True, start=1, end=1).strip()

print (resultado)

#--------------------------------------------------------------------------------------------------

resultado = "hola mundo copa | como estas".cut("|").cut(" ", group=True)

print (resultado)

#--------------------------------------------------------------------------------------------------

entrada = "siki dsjjdsa dssda diki dsakkdsa daskksd siki dsakkd dsakdsa"

print (
  entrada.cut("siki", delete=False).cut("diki", delete=False).group(2).strip()
  )

#--------------------------------------------------------------------------------------------------

print (
  "Id/residen-evil mode/Gtk-3 id/2048 mode/capcom mode/UIX-4".cut(" ").getIn("mode")
  )

#--------------------------------------------------------------------------------------------------

entrada = """

+--------------------------------------+------------+------+
| ID                                   | Label      | CIDR |
+--------------------------------------+------------+------+
| 431c9014-5b5d-4b51-a357-66020ffbb123 | test1      | None |
| 27a74fcd-37c0-4789-9414-9531b7e3f126 | External   | None |
| 5a2712e9-70dc-4b0e-9281-17e02f4684c9 | management | None |
| 7aa697f5-0e60-4c15-b4cc-9cb659698512 | Internal   | None |
+--------------------------------------+------------+------+

"""

labels = ["test1", "External", "management", "Internal"]

for label in labels:
  for linea in entrada.cut("\n"):
    colum = linea.cut("|").strip()
    if label in colum:
      print (
        "%s: %s" % (colum[1], colum[0])
        )

#--------------------------------------------------------------------------------------------------

for item in entrada.cut("\n"):
  elements = item.cut("|").strip()
  if "External" in elements:
    print (
      elements[0]
      )

#--------------------------------------------------------------------------------------------------

print (
  [2, 3, 3, 4, 5, 6].group(4)
  )
