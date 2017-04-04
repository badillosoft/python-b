def recta(x, x1, y1, x2, y2):
    m = float(y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    y = m * x + b
    return y

# python alg1.py > puntos.txt
# sudo apt-get install gnuplot-x11
# gnuplot
# gnuplot> plot "puntos.txt"
# gnuplot> exit
for x in range(-100, 100):
    # (1, 1) (7, 13)
    y = recta(x, 1, 1, 7, 13)
    print x, y