import turtle

window = turtle.Screen()

window.title("Circular Spiral 1")
turtle = turtle.Turtle()
turtle.speed(0)

turtle.penup()
turtle.setposition(-30, -30)

turtle.pendown()
turtle.pensize(1)


colors = ["red", "yellow", "blue", "green", "white"]

for i in range(1000):
  for c in ["red", "yellow"]:
    turtle.color(c)
    turtle.circle(i*2)
    turtle._rotate(5)
