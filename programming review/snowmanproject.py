import turtle

turtle.speed(12)

#bottom
turtle.pensize(1)
turtle.penup()
turtle.sety(-200)
turtle.setx(0)
turtle.pendown()
turtle.circle(175)

#body
turtle.pensize(1)
turtle.penup()
turtle.sety(0)
turtle.setx(0)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(125)
turtle.end_fill()
turtle.color("black")
turtle.circle(125)

#head
turtle.penup()
turtle.sety(200)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.circle(75)
turtle.end_fill()
turtle.color("black")
turtle.circle(75)

#right eye
turtle.penup()
turtle.setx(25)
turtle.sety(275)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#left eye
turtle.penup()
turtle.setx(-25)
turtle.sety(275)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

#mouth
turtle.pensize(10)
turtle.penup()
turtle.sety(250)
turtle.pendown()
turtle.forward(50)

#buttons
turtle.penup()
turtle.sety(150)
turtle.setx(0)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()


turtle.penup()
turtle.sety(125)
turtle.setx(0)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()


turtle.penup()
turtle.sety(100)
turtle.setx(0)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#right arm
turtle.penup()
turtle.color("brown")
turtle.sety(145)
turtle.setx(125)
turtle.right(15)
turtle.pendown()
turtle.forward(85)
turtle.backward(30)
turtle.right(20)
turtle.forward(30)
turtle.backward(30)
turtle.left(40)
turtle.forward(30)

#left arm
turtle.penup()
turtle.color("brown")
turtle.sety(145)
turtle.setx(-125)
turtle.right(-15)
turtle.pendown()
turtle.forward(-85)
turtle.backward(-30)
turtle.right(-20)
turtle.forward(-30)
turtle.backward(-30)
turtle.left(-40)
turtle.forward(-30)

#hat
turtle.pensize(5)
turtle.penup()
turtle.goto(0,340)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

turtle.color("orange")
turtle.forward(100)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(100)