import pyb

def f(x):
    return x ** 2

def area_trapecio(x1, y1, x2, y2):
    base = x2 - x1
    altura = (y1 + y2) / 2.
    return base * altura

def integral_trapecio(a, b, n):
    X = pyb.linspace(a, b, n)
    Y = [f(x) for x in X]

    I = 0

    for i in range(0, n - 1):
        x1 = X[i]
        y1 = Y[i]

        x2 = X[i + 1]
        y2 = Y[i + 1]

        I = I + area_trapecio(x1, y1, x2, y2)

    return I

def F(x):
    return x ** 3 / 3.

a = -5
b = 5

Ir = F(b) - F(a)

for n in range(3, 301, 10):
    In = integral_trapecio(a, b, n)
    print In, abs(In - Ir)