import turtle
atiii = turtle.Turtle()
for i in range(4):
    atiii.color("orange", "blue")
    atiii.begin_fill()
    atiii.forward(100)
    atiii.left(90)
    atiii.forward(100)
    atiii.left(90)
    atiii.forward(100)
    atiii.left(90)
    atiii.forward(100)
    atiii.end_fill()
    atiii.penup()
    # atiii.right(90)
    atiii.forward(100)
    atiii.pendown()

atiii.clear()
turtle.done()