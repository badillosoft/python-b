# Crear una lista vacia y agregar los
# elementos multiplos de 7 o multiplos de 11
# en el intervalo [1, 215]

a = []

for i in range(1, 216):
    if i % 7 == 0 or i % 11 == 0:
        a.append(i)

print a

print float(sum(a)) / len(a)