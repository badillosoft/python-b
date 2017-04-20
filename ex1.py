### VARIABLES

## Enteros

# Crear una variable de tipo entero leida
# desde el teclado sumarle 18 e imprimirla

a = int(raw_input("Dame un entero: ")) + 18

print a

## Flotantes

# Crear una variable de tipo flotante leida
# desde el teclado, dividirla entre 18 e imprimirla

b = float(raw_input("Dame un decimal: "))

print b / 18

## Booleanos

# Crear una variable que contenga True 
# si el usuario ingresa desde el teclado "SI"
# o que contenga False en otro caso

c = "SI" == raw_input("Esribe SI/NO: ")

#c = ["SI", "Si", "si"]\
#    .count(raw_input("Seguro? ")) == 1

### COLECCIONES

## Listas

# Crear una lista con 5 elementos cualesquiera

a = [1, 2, 3, 4, 5]

# Crear una lista con 1, 3, 5, 7, 9, ... 101

a = []

i = 1
while i <= 101:
    a.append(i)
    i += 2

a = []

for i in range(1, 102, 2):
   a.append(i)

# a = [i for i in range(1, 102, 2)]

# Crear una lista generada por
# 2 * i - 1 for i in range(1, 51)

a = []

for i in range(1, 51):
    a.append(2 * i - 1)

a = [2 * i - 1 for i in range(1, 51)]

## Tuplas

# Crear una tupla con 4 elementos cualesquiera
# y desempaquetar la tupla en las variables
# a, b, x, y

t = (1, 2, 3, 4)

a, b, x, y = t

a, b, x, y = (1, 2, 3, 4)

# Crear dos variables a, b que contengan
# numeros diferentes y asignar el valor
# de `a` a `b` y el valor de de `b` a `a`
# al mismo tiempo usando una tupla y el
# desempaquetamiento: a, b = (?, ?)

a = 1
b = 2

a, b = (b, a)

## Diccionarios

# Crear un diccionario que contenga 3 claves
# cualesquiera con 3 valores cualesquiera

d = { "a": 1, "b": 2, "c": 3 }

d = {
    "a": 1,
    "b": 2,
    "c": 3
}

# Crear un diccionario con las claves "x" y "y"
# la clave "x" debe contener el sin(0.78) y
# la clave "y" debe contener el cos(0.78)

# import math # math.sin, math.cos
# from math import *
from math import sin, cos

d = {
    "x": sin(0.78),
    "y": cos(0.78)
}