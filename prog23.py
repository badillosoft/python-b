import turtle
import math

def linspace(a, b, n):
    d = (b - a) / (n - 1.)

    X = []

    for i in range(0, n):
        x = a + i * d
        X.append(x)

    return X

print linspace(-1, 1, 2)
print linspace(-1, 1, 3)
print linspace(-1, 1, 4)
print linspace(-1, 1, 5)
print linspace(-1, 1, 11)