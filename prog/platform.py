import turtle
import math
import time

wn = turtle.Screen()
wn.title("Turtle Platform")
wn.bgcolor("#ADD8E6")
wn.setup(width=1400,height=374)
wn.tracer(0)

#shape
turtle.register_shape("mario.gif")


class Pen(turtle.Turtle):
    #maze creator
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.shape("square")
        self.speed(0)
        self.penup()

class Player(turtle.Turtle):
    #player
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.speed(0)

    #player mvt
    def goright(self):
        if (self.xcor()+24,self.ycor()) not in walls:
            self.goto(self.xcor()+24,self.ycor())
    def goleft(self):
        if (self.xcor()-24,self.ycor()) not in walls:
            self.goto(self.xcor()-24,self.ycor())

    def gravity(self):
        if (self.xcor(),self.ycor()-24) not in walls:
            time.sleep(0.5)
            self.goto(self.xcor(),self.ycor()-24)
    def jump(self):
        if (self.xcor(),self.ycor()+24) not in walls:
            self.goto(self.xcor(),self.ycor()+48)

    def victory(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        dist = math.sqrt(a**2 + b**2)
        if dist < 5:
            return True
        else:
            return False

#win block
class Sortie(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("blue")
        self.penup()

#obstacles
class Obstacle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.shape("square")
        self.color("red")

#level design
lvl = [""]
lvl1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X                     O                        OOX",
"X                     O                        OOX",
"X                         X                 X  OOX",
"X                        X                 X   OOX",
"X                     XXX  O              X     OX",
"X                 XXX      O            XX       X",
"X             XXX          O XXXX    XX       X  X",
"X         XXX              O      XX            SX",
"XP    XXX                  O                    XX",
"XXXXX                      O                     X",
"XOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

lvl.append(lvl1)

#setup
def setuplevel(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            caracter = level[y][x]
            screen_x = -688 + (x*24)
            screen_y = 175 - (y*24)
            if caracter == "X":
                pen.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))

            if caracter == "O":
                obstacle.goto(screen_x,screen_y)
                obstacle.stamp()
                obs.append((screen_x,screen_y))

            if caracter == "P":
                player.goto(screen_x,screen_y)

            if caracter == "S":
                sortie.goto(screen_x,screen_y)

pen = Pen()
player = Player()
obstacle = Obstacle()
sortie = Sortie()

walls = [""]
obs = [""]

#config the maze
setuplevel(lvl[1])

#control player
turtle.listen()
turtle.onkey(player.goleft,"Left")
turtle.onkey(player.goright,"Right")
turtle.onkey(player.jump,"space")

#main loop
while ((player.victory(sortie) == False) and (player.xcor(),player.ycor()) not in obs):
    wn.update()
    player.gravity()

#final output
if player.victory(sortie) == True:
    print("Bravo, vous avez terminee le premier niveau")
else:
    print("Perdu, retentez votre chance plus tard")
