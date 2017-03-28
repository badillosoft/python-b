import turtle
import math

def cuadrado(l, ox, oy, fill):
    # O
    turtle.penup()
    turtle.goto(ox, oy)

    # A
    turtle.fill(fill)
    turtle.forward(l / 2)
    turtle.left(90)
    turtle.pendown()

    #B
    turtle.forward(l / 2)
    turtle.left(90)

    # C
    turtle.forward(l)
    turtle.left(90)

    # D
    turtle.forward(l)
    turtle.left(90)

    # E
    turtle.forward(l)
    turtle.left(90)

    # A'
    turtle.forward(l / 2)
    turtle.left(90)
    turtle.penup()
    turtle.fill(False)

    # O'
    turtle.forward(l / 2)
    turtle.left(180)

def tablero(l, ox, oy):
    turtle.speed(0)
    for i in range(0, 8):
        for j in range(0, 8):
            cuadrado(l, i * l - 4 * l + ox, j * l - 4 * l + oy, (i + j) % 2 == 0)
    turtle.goto(ox, oy)

tablero(16, 0, 0)

tablero(16, 200, 200)

raw_input()