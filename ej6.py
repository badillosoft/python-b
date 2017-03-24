# -*- coding: utf-8 -*-

# El número a es divisible por b
# Si a MOD b = 0

sp = 0
si = 0

for i in range(1, 101):
    if i % 2 == 0:
        sp = sp + i
    else:
        si = si + i

print "La suma de pares es:", sp
print "La suma de impares es:", si