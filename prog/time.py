#import
import time
import turtle

#setup time
h = int(time.strftime("%I"))
m = int(time.strftime("%M"))
s = int(time.strftime("%s"))

#setup screen
wn = turtle.Screen()
wn.bgcolor("Black")
wn.setup(width=300,height=100)
wn.title("time digital")
wn.tracer(0)

#setup writer
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.speed(0)
pen.write("{} : {} : {}".format(h,m,s),align="center",font=("Courier",24,"normal"))

#mainloop
while True:
    #update time
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%s"))
    wn.update()
    time.sleep(1)
    pen.clear()
    pen.write("{} : {} : {}".format(h,m,s),align="center",font=("Courier",24,"normal"))

wn.mainloop()
