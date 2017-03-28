import turtle

def celda(r, ox, oy):
    turtle.penup()
    turtle.goto(ox, oy)

    turtle.forward(r)
    turtle.left(120)

    turtle.pendown()
    turtle.forward(r)
    turtle.left(60)
    turtle.forward(r)
    turtle.left(60)
    turtle.forward(r)
    turtle.left(60)
    turtle.forward(r)
    turtle.left(60)
    turtle.forward(r)
    turtle.left(60)
    turtle.forward(r)
    turtle.left(120)
    turtle.penup()

    turtle.forward(r)

for i in range(0, 10):
    for j in range(0, 10):
        celda(20, j * 20, i * 20)

raw_input()