import turtle
import random
red = 100

turtle.bgcolor("black")

colors = ["white", "red", "yellow", "cyan", "orange", "pink", "grey"]
turtle.pensize(7)

turtle.setpos(0, -100)
for i in range(6):
    turtle.color("cyan")
    turtle.forward(100)
    turtle.right(60)

for i in range(3):
    turtle.color("white")
    if(i == 0):
        turtle.left(60)
    else:
        turtle.left(120)
    turtle.forward(350)

turtle.color("yellow")
turtle.circle(150)

turtle.color("white")
turtle.right(120)
turtle.forward(200)
for i in range(4):
    turtle.color("white")
    turtle.forward(100)
    turtle.left(90)

turtle.color("orange")
turtle.right(90)
turtle.forward(250)
rad = 105
turtle.speed(10)
while rad != 15:
    turtle.color("orange")
    turtle.circle(red)
    rad -= 15

for i in range(100):
    turtle.circle(0)
