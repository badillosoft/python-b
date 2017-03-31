# Manejo de Archivos

# Escritura de archivos

# 1. Abrir el archivo en modo escritura
# !!! Si el archivo ya existe se va a sobreescbir

f = open("hola2.txt", "a")

f.write("Hola mundo\n")
f.write("Texto despues\n del anterior\n")
f.write("Cuidado con poner\n saltos de linea manualmente")

f.close()