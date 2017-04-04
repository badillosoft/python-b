def recta(x, x1, y1, x2, y2):
    m = float(y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    y = m * x + b
    return y

def ult2(L, x):
    for s in range(1, len(L)):
        if x <= L[s]:
            return (s - 1, s)
    return (s - 1, s)

def interpol(P, x):
    X, Y = zip(*P)
    (i, s) = ult2(X, x)
    x1, y1 = P[i]
    x2, y2 = P[s]
    y = recta(x, x1, y1, x2, y2)
    return y

import math

puntos = [(i, math.sin(i / 10.)) for i in range(-100, 100)]

for x in range(-100, 100):
    y = interpol(puntos, x)
    print x, y

# python alg3.py > puntos2.txt
# gnuplot
# gnuplot> plot "puntos2.txt" with lines
# gnuplot> exit