#module import
import turtle
import random
import time

#setup screen
wn = turtle.Screen()
wn.setup(width=600,height=400)
wn.bgcolor("#ADD8E6")
wn.tracer(10)

s = 0

#setup score
score = turtle.Turtle()
score.penup()
score.color("white")
score.speed(0)
score.hideturtle()
score.goto(0,100)
score.write("{}".format(s),align="center",font=("Courier",50,"normal"))

#obstacle setup
haut = turtle.Turtle()
bas = turtle.Turtle()
haut.hideturtle()
bas.hideturtle()
haut.speed(0)
bas.speed(0)
haut.penup()
bas.penup()
haut.shape("square")
bas.shape("square")
haut.color("green")
bas.color("green")
haut.goto(300,200)
bas.goto(300,-200)
h = random.randint(1,19)
haut.shapesize(stretch_wid=h,stretch_len=1)
bas.shapesize(stretch_wid=19-h,stretch_len=1)

#create ground
sol=turtle.Turtle()
sol.shape("square")
sol.color("brown")
sol.penup()
sol.shapesize(stretch_len=30,stretch_wid=5)
sol.goto(0,-200)

#player
player = turtle.Turtle()
player.penup()
player.speed(0)
player.dy = 0
player.da = -0.02

#keyboard binding
def jump():
    player.sety(player.ycor())
    player.dy += 1.4
turtle.listen()
turtle.onkey(jump,"space")

#main loop
while True:
    wn.update()

    #move obstacle
    haut.showturtle()
    bas.showturtle()
    for i in range(600):
        haut.backward(1)

        #move player
        player.dy += player.da
        player.sety(player.ycor()+player.dy)

        #ground crash check
        if player.ycor() < -160:
            turtle.bye()

        #collision check
        uplim = 200-(h*12)
        downlim = uplim - 200
        if player.xcor() == haut.xcor() and (player.ycor() > uplim or player.ycor() < downlim) :
            turtle.bye()

        #score update
        if player.xcor() == haut.xcor():
            s+=1
            print(s)
            score.clear()
            score.write("{}".format(s),align="center",font=("Courier",50,"normal"))
        bas.backward(1)

    #move obstacle
    haut.hideturtle()
    bas.hideturtle()
    haut.penup()
    bas.penup()
    haut.goto(300,200)
    bas.goto(300,-200)
    h = random.randint(1,19)
    haut.shapesize(stretch_wid=h,stretch_len=1)
    bas.shapesize(stretch_wid=20-h,stretch_len=1)
