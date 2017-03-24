# Agregar y quitar elementos a listas

a = [1, 5, 21]

print a # [1, 5, 21]

a[1] = 9

print a # [1, 9, 21]

a.append(12)

print a # [1, 9, 21, 12]

a.append(8)

print a # [1, 9, 21, 12, 8]

a.pop()

print a # [1, 9, 21, 12]

a.pop(1)

print a # [1, 21, 12]

a.insert(0, 3) # en indice 0 inserta 3

print a # [3, 1, 21, 12]