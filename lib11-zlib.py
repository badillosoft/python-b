import zlib

# 1. Abrir el archivo en modo de lectura binario
f = open("cat.jpg", "rb")

# 2. Leemos todos los datos y los guardamos en una
# variable
data = f.read()

f.close()

print len(data)

# 3. Comprimimos los datos
datac = zlib.compress(data)

print len(datac)

print 100. * len(datac) / len(data)

# 4. Guardar los datos comprimidos en un archivo
# 5. Abrir el archivo en modo escritura binaria
f = open("cat.zlib", "wb")

f.write(datac)

f.close()