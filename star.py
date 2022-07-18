import turtle
star = turtle.Turtle()
star.getscreen().bgcolor('green')
star.speed(100)
star.penup()
star.goto(-200,100)
star.pendown()
def sTar(turtle, size):
    if size<=10:
        return
    else:
        turtle.color('yellow', 'red')
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            sTar(turtle, size/3)
            turtle.left(216)
        turtle.end_fill()
sTar(star, 210)
turtle.done()