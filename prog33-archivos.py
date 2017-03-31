def invertir(linea):
    return "".join(list(linea)[::-1])

f = open("hola.txt")

for linea in f:
    print invertir(linea)

f.close()