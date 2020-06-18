# coding: utf-8

# iterar los archivos de un directorio 

for path in "./".path.listdir():
    pass

#-------------------------------------------------------------------------

# buscar todos los archivos .txt - ejemplo 1

for archivo in "./*.txt".path.find():
    pass

#-------------------------------------------------------------------------

# buscar todos los archivos .txt - ejemplo 2

for archivo in "./".path.find("*.txt"):
    pass

#-------------------------------------------------------------------------

# buscar todos los archivos que empiecen por (M) y tengan una extensión (.txt), también buscar todos los archivos con una extensión (.py)

for archivo in "./".path.find(["m*.txt", "*.py"]):
    pass
