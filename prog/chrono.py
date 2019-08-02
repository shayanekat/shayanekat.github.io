#==============================================================
#                           Minuteur
#==============================================================

def minuteur(min,sec):
    #import
    import time
    import turtle

    #init screen
    wn = turtle.Screen()
    wn.bgcolor("Black")
    wn.setup(width=300,height=100)
    wn.tracer(0)
    wn.title("Minuteur")

    #time printer
    printer = turtle.Turtle()
    printer.color("white")
    printer.hideturtle()
    printer.speed(0)
    printer.write("{} : {}".format(min,sec),align="center",font=("Courier",24,"normal"))

    print(min,":",sec)

    #main prog
    while min !=0 or sec!=0 :
        if sec==0:
            min=min-1
            sec=60
        time.sleep(199/200)
        sec-=1
        printer.clear()
        printer.write("{} : {}".format(min,sec),align="center",font=("Courier",24,"normal"))
        print(min,":",sec)

    #main loop
    while True:
        wn.update()
    wn.mainloop()

minuteur(3,0)
