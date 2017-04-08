import zlib

# 1. Abrir el archivo en modo de lectura binario
f = open("cat.zlib", "rb")

# 2. Leemos todos los datos y los guardamos en una
# variable
datac = f.read()

f.close()

print len(datac)

# 3. Descomprimimos los datos
data = zlib.decompress(datac)

print len(data)

print 100. * len(datac) / len(data)

# 4. Guardar los datos comprimidos en un archivo
# 5. Abrir el archivo en modo escritura binaria
f = open("cat2.jpg", "wb")

f.write(data)

f.close()