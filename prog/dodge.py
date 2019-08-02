#import
import turtle
import random

#setup screen
wn = turtle.Screen()
wn.title("Dodge the arrows")
wn.bgcolor("black")
wn.setup(width=400,height=600)
wn.tracer(0)

#player
player = turtle.Turtle()
player.shape("circle")
player.color("white")
player.hideturtle()
player.speed(0)
player.penup()
player.goto(0,-260)
player.showturtle()

#arrows
arrows = []
for i in range(20):
    arrows.append(turtle.Turtle())

for arr in arrows:
    arr.hideturtle()
    arr.speed(0)
    arr.color("white")
    arr.penup()
    arr.goto(random.randint(-190,190),300)
    arr.dy = random.randint(1,5)
    arr.showturtle()
    arr.rt(90)

#keyboard binding
def right():
    player.setx(player.xcor() + 10)
def left():
    player.setx(player.xcor() - 10)

turtle.listen()
turtle.onkey(right,"Right")
turtle.onkey(left,"Left")

#mainloop
while True:
    wn.update()
    for arr in arrows:
        arr.sety(arr.ycor() - arr.dy)

        #down check
        if arr.ycor() < -300 :
            arr.hideturtle()
            arr.goto(random.randint(-190,190),300)
            arr.dy = random.randint(1,5)
            arr.showturtle()

        #collision check
        if arr.xcor() < player.xcor() + 10 and arr.xcor() > player.xcor() - 10 and arr.ycor() == player.ycor():
            turtle.bye()
