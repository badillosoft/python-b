# -*- coding: utf-8 -*-

# Calcular la suma de los números naturales pares
# menores o iguales a 100

# Sumar todo x pertenece a [1, 100] y x es par

sp = 0

for x in range(2, 101, 2):
    sp = sp + x

print "La súma de pares es:", sp

# Sumar todo x pertenece a [1, 100] y x es impar

si = 0

for x in range(1, 101, 2):
    si = si + x

print "La suma de impares es:", si