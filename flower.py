import turtle
import math
flower = turtle.Turtle()
flower.speed(50)
flower.color('red', 'yellow')
flower.begin_fill()
for i in range(40):
    flower.forward(100)
    flower.left(170)
    flower.forward(200)
flower.end_fill()
flower.penup()
flower.forward(300)
flower.pendown()
flower.color('yellow', 'red')
flower.begin_fill()
for i in range(40):
    flower.forward(100)
    flower.left(170)
    flower.forward(200)
flower.end_fill()

flower.clear()



for i in range(900):
    flower.forward(math.sqrt(i))
    flower.left(i%180)
turtle.done()