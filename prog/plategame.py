#import
import turtle
import random

#screen
wn = turtle.Screen()
wn.bgcolor("Black")
wn.setup(width=600,height=600)
wn.title("Plate game by Shayane Kathchera")
wn.tracer(0)

#Plate
plate = turtle.Turtle()
plate.color("white")
plate.shape("square")
plate.shapesize(stretch_len = 5)
plate.penup()
plate.goto(0,-250)
plate.speed(0)

#ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ball.penup()
ball.goto(random.randint(-250,250),250)
ball.dx = 3
ball.dy = -3
g = 0.01

#fonctions
def plateL():
    x = plate.xcor()
    x -= 20
    plate.setx(x)

def plateR():
    x = plate.xcor()
    x += 20
    plate.setx(x)

#Keyboard binding
wn.listen()
wn.onkey(plateL,"Left")
wn.onkey(plateR,"Right")

#main loop
while True:
    wn.update()

    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)
    ball.dy -= g

    if ball.ycor() < -240 and (ball.xcor() < plate.xcor() + 40 and ball.xcor() > plate.xcor() - 40):
        ball.sety(-240)
        ball.dy *= -1

    if ball.xcor() < -290:
        ball.dx *= -1
    if ball.xcor() > 290:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(250)
