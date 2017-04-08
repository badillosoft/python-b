import os

print os.getcwd()

try:
    os.mkdir("hola")
    print "La carpeta <hola> fue creada"
except:
    print "La carpeta <hola> ya existe"

os.chdir("hola")

print os.getcwd()

f = open("hola.txt", "w")

f.write("Hola mundo\n")

f.close()