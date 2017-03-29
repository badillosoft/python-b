import turtle
import math

def f(x):
    return x * math.sin(x)

puntos = []

for x in range(-10, 10):
    y = f(x)
    puntos.append((x * 10, y * 10))

print puntos

turtle.penup()

for x, y in puntos:
    turtle.goto(x, y)
    turtle.pendown()

turtle.hideturtle()

turtle.mainloop()