# Poligono regular de 5 lados

import turtle
import math

r = 100

# Punto 1
x1 = r * math.cos(0 * 2 * math.pi / 5)
y1 = r * math.sin(0 * 2 * math.pi / 5)

# Punto 2
x2 = r * math.cos(1 * 2 * math.pi / 5)
y2 = r * math.sin(1 * 2 * math.pi / 5)

# Punto 3
x3 = r * math.cos(2 * 2 * math.pi / 5)
y3 = r * math.sin(2 * 2 * math.pi / 5)

# Punto 4
x4 = r * math.cos(3 * 2 * math.pi / 5)
y4 = r * math.sin(3 * 2 * math.pi / 5)

# Punto 5
x5 = r * math.cos(4 * 2 * math.pi / 5)
y5 = r * math.sin(4 * 2 * math.pi / 5)

turtle.goto(x1, y1)
turtle.goto(x2, y2)
turtle.goto(x3, y3)
turtle.goto(x4, y4)
turtle.goto(x5, y5)

turtle.goto(x1, y1)

turtle.ht()

raw_input("Pulsa una tecla para salir")