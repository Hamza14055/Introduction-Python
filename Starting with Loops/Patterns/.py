import turtle
square = turtle.Turtle()
square.color("red")
square.speed=2
i=0
while i<4:
    square.forward(200)
    square.right(90)
    i+=1
turtle.done()