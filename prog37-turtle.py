import turtle

turtle.home()

f = open("turtle.txt")

for linea in f:
    if linea == "" or linea == "\n":
        continue

    aux = linea.split(" ")

    comando = aux[0]
    valor = int(aux[1])

    if comando == "avanzar":
        turtle.forward(valor)
    elif comando == "izquierda":
        turtle.left(valor)
    elif comando == "derecha":
        turtle.right(valor)

turtle.mainloop()