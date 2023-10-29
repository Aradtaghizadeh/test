from turtle import*


def square(a, c="black"):
    pencolor(c)
    for i in range(4):
        fd(a)
        lt(90)
def teleport(x, y):
    up()
    goto(x,y)
    down()
    square(100,"red")
    teleport(-200, 100)
    square(50,"blue")
    teleport(-200, -200)
    square(25,"green")
    teleport(-400, 0)
    square(75)
    done()