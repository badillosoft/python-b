A = [3, 6, 8, 4, 6, 5, 1, 2]

Ap = []

for i in range(1, len(A) + 1):
    x = min(A) # buscar menor (x) de [A]
    A.remove(x) # quitar (x) de [A]
    Ap.append(x) # agregar (x) a [Ap]

print Ap