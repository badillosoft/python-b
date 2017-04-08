import os

path = "/home/aulae5"

archivos = os.listdir(path)

for nombre in archivos:
    if os.path.isdir(path + "/" + nombre):
        print nombre