import turtle


wn= turtle.Screen()
wn.setup(918, 620)
wn.title("MY LOVELY INDIA")

t = turtle.Turtle()

t.speed(10)

for i in range(24):  # For 24 AshokChakra O
		t.forward(50)
		t.penup()
		t.setpos(0,0)
		t.pendown()
		t.right(15)  # 350/24

t.setposition(0, -51)
t.circle(52)
t.penup()

t.speed(5)

t.setposition(-450, 120)  # Orange Sec
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.forward(900)
t.left(90)
t.forward(180)
t.left(90)
t.forward(900)
t.left(90)
t.forward(180)
t.end_fill()
t.penup()

t.setposition(-450, -120)  # Grren Sec
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.right(270)
t.forward(900)
t.right(90)
t.forward(180)
t.right(90)
t.forward(900)
t.right(90)
t.forward(180)
t.end_fill()

for i in range(100):
	turtle.circle(0)
	turtle.penup(); turtle.setpos(90,-70);turtle.pendown(); turtle.color("black")
	turtle.write("-by hbaruas", move=False, align="left", font=("Serif", 8))
