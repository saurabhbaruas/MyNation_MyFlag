import turtle

wn= turtle.Screen()
wn.title("My Beloved INDIA")
turtle.bgcolor("skyblue")
turtle.pensize(4)

#circle1
turtle.color("white")
turtle.penup()
turtle.setpos(-150,120)
turtle.pendown()
turtle.speed(5)#slowest

for i in range(1):
	turtle.circle(50)

#sQUARE
turtle.penup()
turtle.setpos(-50,50)
turtle.pendown()

turtle.color("red")
turtle.speed(1)

for i in range(4):
	turtle.forward(100)
	turtle.right(90)

#Rectangle
turtle.penup()
turtle.setpos(100, -100)
turtle.pendown()

turtle.color("green")
turtle.speed(1)

for i in range(2):
	turtle.forward(150)
	turtle.right(90)
	turtle.forward(70)
	turtle.right(90)

#Text Adding
turtle.penup(); turtle.setpos(0,200);turtle.pendown(); turtle.color("black")

turtle.write("Text in Turtle", move=True, align="left", font=("Serif", 28))

#circleText
turtle.penup();turtle.setpos(-170,90);turtle.pendown();turtle.color("white")
turtle.write("Circle", move=True, align="left", font=("Serif", 18))

#Square Text
turtle.penup(); turtle.setpos(-50,70); turtle.pendown(); turtle.color("red")
turtle.write("Square", move=False,align="left",font=("Serif",18))




#Rectangle Text
turtle.penup(); turtle.setpos(100,-80); turtle.pendown(); turtle.color("green")

turtle.write("Rectangle", move=False,align="left", font=("Serif", 18))

for i in range(100):
	turtle.circle(0)














# #circle2
# turtle.color("yellow")
# turtle.speed(10)

# for i in range(2):
# 	turtle.circle(75)

# turtle.penup()
# turtle.setpos(150, -150)
# turtle.pendown()


# #circle3
# turtle.color("red")
# turtle.speed(0) #max

# for i in range(2):
# 	turtle.circle(75)



