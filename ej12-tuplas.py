import turtle as t

puntos = [
    (100, 0, "red"),
    (100, 100, "blue"),
    (0, 100, "green"),
    (0, 0, "yellow")
]

t.pensize(10)

for x, y, color in puntos:
    t.pencolor(color)
    t.goto(x, y)

raw_input()