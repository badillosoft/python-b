import turtle

def click(x, y):
    print x, y
    turtle.goto(x, y)

sc = turtle.getscreen()

sc.onclick(click)

turtle.mainloop()