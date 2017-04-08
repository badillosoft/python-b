# Algoritmo 1: Copiar una cadena en otra

s = "Hola mundo"

r = ""

for i in range(0, len(s)):
    r += s[i]

print "AG1", r

# Algoritmo 2: Limpiar una cadena de espacios repetidos

s = "texto         otro       sdasdasd    "

r = ""

uc = ""
for c in s:
    if c == " " and uc == " ":
        continue

    uc = c

    r += uc

print "AG2", r

# Algoritmo 3: Contar las palabras en una cadena

s = "anita         lava      la       tina      otra"

def reducir(s, k):
    r = ""
    uc = ""
    for c in s:
        if c == k and uc == k:
            continue
        uc = c
        r += uc
    return r

r = reducir(s, " ")

print "AG3", len(r.split(" "))

# Algoritmo 4: Invertir una cadena

s = "hola mundo"

r = ""
for i in range(len(s) - 1, -1, -1):
    r += s[i]

print "AG4", r

# Algoritmo 5: Copiar una cadena en otra pero solo los caracteres
# en mayuscula

s = "Hola Mundo ABCdefXy"

r = ""

alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for c in s:
    if c in alfabeto:
        r += c

print "AG5", r

# Algoritmo 6: Convertir una cadena en mayusculas

s = "HolA mundo esta es UNA cadena En Mayusculas y minusCULAS"

minusculas = list("abcdefghijklmnopqrstuvwxyz")
mayusculas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

alfabeto = { }

for i in range(0, len(minusculas)):
    c = minusculas[i]
    C = mayusculas[i]

    alfabeto[C] = c

r = ""

for c in s:
    if c in alfabeto:
        r += alfabeto[c]
    else:
        r += c

print "AG6", r