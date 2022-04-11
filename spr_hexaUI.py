import turtle

colors = ["red", "green", "blue", "yellow", "purple", "orange", "white"]

t=turtle.Pen()
turtle.bgcolor("black")
t1=turtle.Turtle()
t1.speed(0)

for i in range(250):
	t.pencolor(colors[i%6])
	t.width(i/100 + 2)
	t.forward(i)
	t.left(59)

for i in range(1000):
	turtle.circle(0)