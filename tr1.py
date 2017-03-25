# Dibujar un poligono regular de n lados
# usando turtle

import turtle as t
import math

n = int(raw_input("Dame el numero de lados: "))

r = 100

puntos = []

# i pertenece a [0, n) i=1,2,3,...,n-1
for i in range(0, n):
    # xi = r * cos(i * 2 * PI / n)
    # yi = r * sin(i * 2 * PI / n)
    xi = r * math.cos(i * 2 * math.pi / n)
    yi = r * math.sin(i * 2 * math.pi / n)
    puntos.append( (xi, yi) )

print puntos

t.penup()

for x, y in puntos:
    t.goto(x, y)
    t.pendown()

xo, yo = puntos[0]

t.goto(xo, yo)

t.hideturtle()

raw_input("Pulsa una tecla para salir")