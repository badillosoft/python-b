import random

palabras = ["papa", "apple", "rojo", "dulce", "juan"]

print random.choice(palabras)

# Crear un archivo llamado palabras.txt
# que contenga 1000 palabras aleatorias
# +1: dejar un espacio entre cada palabra
# +1: dejar un salto de linea cada 10 palabras

f = open("palabras.txt", "w")

cont = 0
for i in range(0, 1000):
    f.write(random.choice(palabras))
    f.write(" ")

    cont += 1

    if cont == 50:
        f.write("\n")
        cont = 0