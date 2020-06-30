# coding: utf-8

# codifica imagen a formato web (base64)
string = "../imagen.jpeg".path.read().encode("web-image")

data = """<meta charset="utf-8">
<div align="center">
    <img src="%s" style="width: 500px;">
</div>
""" % (string)

arhivo_html = "imagen_prueba1.html".path.save(data).close()

#-------------------------------------------------------------------------

# cadifica ruta de archivo a formato compatible con navegadores web (protocolo url local)
web_url = "../imagen.jpeg".encode("web-url")

data = """<meta charset="utf-8">
<div align="center">
    <img src="%s">
</div>""" % (web_url)

arhivo_html = "imagen_prueba2.html".path.save(data).close()
