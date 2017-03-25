import turtle
import math

def poligono(n, r):
    puntos = []

    for i in range(0, n):
        ai = i * 2 * math.pi / n
        xi = r * math.cos(ai)
        yi = r * math.sin(ai)

        puntos.append((xi, yi))

    turtle.penup()

    for xi, yi in puntos:
        turtle.goto(xi, yi)
        turtle.pendown()

    xo, yo = puntos[0]

    turtle.goto(xo, yo)

    turtle.penup()

    turtle.goto(0, 0)

#poligono(3, 50)
#poligono(4, 100)
#poligono(5, 150)
#poligono(6, 200)

for n in [3, 4, 5, 6, 7, 8, 9, 10]:
    poligono(n, 10 * n)

raw_input()