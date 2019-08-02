#————————————————————————————————————————————————————————#
#            Game in Python By Shayane Katchera          #
#————————————————————————————————————————————————————————#

#import
import turtle
import math

#screen setup
wn = turtle.Screen()
wn.bgcolor('black')
setup = turtle.Turtle()
setup.hideturtle()
setup.color("white")
setup.speed(0)
setup.pensize(3)
setup.penup()
setup.setposition(-300,-300)
setup.pendown()
for i in range(4):
    setup.forward(600)
    setup.left(90)
setup.penup()
setup.hideturtle()

#create player
player = turtle.Turtle()
player.color('blue')
speed = 1.5

#set keyboard binding
def turnLeft():
    player.left(90)

def turnRight():
    player.right(90)


turtle.listen()
turtle.onkey(turnLeft,"Left")
turtle.onkey(turnRight,"Right")

traj = []
#main prog
while (player.xcor(),player.ycor()) not in traj:
    traj.append((player.xcor(),player.ycor()))
    player.stamp()
    player.forward(speed)

    #boundary check
    if player.xcor() > 300 or player.xcor() < -300:
        player.penup()
        player.hideturtle()
        player.setposition(-player.xcor(),player.ycor())
        player.showturtle()
        player.pendown()
    if player.ycor() > 300 or player.ycor() < -300:
        player.penup()
        player.hideturtle()
        player.setposition(player.xcor(),-player.ycor())
        player.showturtle()
        player.pendown()

turtle.mainloop()
