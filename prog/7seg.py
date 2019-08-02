import turtle
import time
#setup screen

wn = turtle.Screen()
wn.setup(width=300,height=500)
wn.bgcolor("Black")

#create segment
a = turtle.Turtle()
a.hideturtle()
a.shape("square")
a.shapesize(stretch_wid = 1,stretch_len = 5)
a.color("white")
a.speed(0)

b = turtle.Turtle()
b.hideturtle()
b.shape("square")
b.shapesize(stretch_wid = 1,stretch_len = 5)
b.color("white")
b.penup()
b.goto(0,200)
b.speed(0)

c = turtle.Turtle()
c.hideturtle()
c.shape("square")
c.shapesize(stretch_wid = 1,stretch_len = 5)
c.color("white")
c.penup()
c.goto(0,-200)
c.speed(0)

d = turtle.Turtle()
d.hideturtle()
d.shape("square")
d.shapesize(stretch_wid = 5,stretch_len = 1)
d.color("white")
d.penup()
d.goto(100,100)
d.speed(0)

e = turtle.Turtle()
e.hideturtle()
e.shape("square")
e.shapesize(stretch_wid = 5,stretch_len = 1)
e.color("white")
e.penup()
e.goto(100,-100)
e.speed(0)

f = turtle.Turtle()
f.hideturtle()
f.shape("square")
f.shapesize(stretch_wid = 5,stretch_len = 1)
f.color("white")
f.penup()
f.goto(-100,100)
f.speed(0)

g = turtle.Turtle()
g.hideturtle()
g.shape("square")
g.shapesize(stretch_wid = 5,stretch_len = 1)
g.color("white")
g.penup()
g.goto(-100,-100)
g.speed(0)

#functions
def zero():
    a.hideturtle()
    b.showturtle()
    c.showturtle()
    d.showturtle()
    e.showturtle()
    f.showturtle()
    g.showturtle()

def one():
    a.hideturtle()
    b.hideturtle()
    c.hideturtle()
    d.showturtle()
    e.showturtle()
    f.hideturtle()
    g.hideturtle()

def two():
    a.showturtle()
    b.showturtle()
    c.showturtle()
    d.showturtle()
    e.hideturtle()
    f.hideturtle()
    g.showturtle()

def three():
    a.showturtle()
    b.showturtle()
    c.showturtle()
    d.showturtle()
    e.showturtle()
    f.hideturtle()
    g.hideturtle()

def four():
    a.showturtle()
    b.hideturtle()
    c.hideturtle()
    d.showturtle()
    e.showturtle()
    f.showturtle()
    g.hideturtle()

def five():
    a.showturtle()
    b.showturtle()
    c.showturtle()
    d.hideturtle()
    e.showturtle()
    f.showturtle()
    g.hideturtle()

def six():
    a.showturtle()
    b.showturtle()
    c.showturtle()
    d.hideturtle()
    e.showturtle()
    f.showturtle()
    g.showturtle()

def seven():
    a.hideturtle()
    b.showturtle()
    c.hideturtle()
    d.showturtle()
    e.showturtle()
    f.hideturtle()
    g.hideturtle()

def height():
    a.showturtle()
    b.showturtle()
    c.showturtle()
    d.showturtle()
    e.showturtle()
    f.showturtle()
    g.showturtle()

def nine():
    a.showturtle()
    b.showturtle()
    c.showturtle()
    d.showturtle()
    e.showturtle()
    f.showturtle()
    g.hideturtle()


zero()
time.sleep(1)
one()
time.sleep(1)
two()
time.sleep(1)
three()
time.sleep(1)
four()
time.sleep(1)
five()
time.sleep(1)
six()
time.sleep(1)
seven()
time.sleep(1)
height()
time.sleep(1)
nine()
time.sleep(1)

wn.mainloop()
