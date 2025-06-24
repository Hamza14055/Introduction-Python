import turtle
square = turtle.Turtle()
sides = 4
length = 70 
square.color("red")
for i in range (sides):
    square.forward(length)
    square.right(90)
turtle.done()