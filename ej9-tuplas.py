# Guardar en una lista llamada `puntos`
# los siguientes puntos que definen a un
# cuadrilatero: (0, 1) (8, 3) (7, 9) (-1, 2)

puntos = [(0, 1), (8, 3), (7, 9), (-1, 2)]

for p in puntos:
    # Desempaquetamiento explicito
    x, y = p
    print "X:", x, "Y:", y

# Desempaquetamiento implicito
for x, y in puntos:
    print "X:", x, "Y:", y