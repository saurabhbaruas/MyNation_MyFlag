import turtle

colors = ["red", "green", "blue", "yellow", "purple", "orange", "white"]
colors1 = ["red", "yellow", "red", "yellow", "red", "yellow", "red"]

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(35):
    # for color in ["white"]:
    for color in colors:
        turtle.color(color)
        turtle.left(12)

        turtle.forward(130)
        turtle.left(90)
        turtle.forward(130)
        turtle.left(90)
        turtle.forward(130)
        turtle.left(90)
        turtle.forward(130)
        turtle.left(90)

for i in range(1000):
    turtle.circle(0)
