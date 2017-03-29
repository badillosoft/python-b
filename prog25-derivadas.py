import turtle
import math
import pyb

def f(x):
    return x**2 - math.sin(x)

def fp(x):
    h = 0.0001
    return (f(x + h) - f(x - h)) / (2. * h)

X = pyb.linspace(-2, 2, 21)

Y = []
Yp = []

for x in X:
    y = f(x)
    yp = fp(x)

    Y.append(y)
    Yp.append(yp)

print X
print Y
print Yp

turtle.pencolor("blue")
pyb.draw_points(zip(X, Y), 40, 40, 0, 0)
turtle.pencolor("red")
pyb.draw_points(zip(X, Yp), 40, 40, 0, 0)

turtle.mainloop()