import turtle
import math
import pyb

def f(x):
    return math.exp(x)

X = pyb.linspace(-1, 1, 1000)

puntos = []

for x in X:
    puntos.append((x, f(x)))

turtle.pencolor("#FF0082")
turtle.pensize(4)
pyb.draw_points(puntos, 100, 100, 0, 0)

turtle.mainloop()