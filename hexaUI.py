import turtle

colors = ["red", "green", "blue", "yellow", "purple", "orange", "white"]

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(40):
    for color in ["white", "yellow"]:
        turtle.color(color)
        turtle.circle(100)
        turtle.left(10)

for i in range(1000):
    turtle.circle(0)
