import turtle

def linspace(a, b, n):
    d = (b - a) / (n - 1.)

    x = []

    for i in range(0, n):
        x.append(a + i * d)

    return x

def draw_points(points, ex, ey, ox, oy):
    turtle.penup()

    for x, y in points:
        turtle.goto(x * ex + ox, y * ey + oy)
        turtle.pendown()

    turtle.penup()
    turtle.goto(ox, oy)