# Hacer que la tortuga dibije la siguiente lista
# de puntos

import turtle

puntos = [
    (100, 0),
    (50, 100),
    (50, -100),
    (0, 0),
    (-100, 0),
    (-50, 100),
    (-50, -100),
    (0, 0),
    (-50, 100),
    (50, 100),
    (25, 125),
    (50, 150),
    (-25, 125),
    (-50, 100),
    (50, 100),
    (0, 0)
]

for x, y in puntos:
    turtle.goto(x, y)

raw_input("...")