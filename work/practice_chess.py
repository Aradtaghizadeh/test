from turtle import ht, speed, goto, up, down, begin_fill, end_fill, lt, fd, bk, rt, done
ht()
x = 20
speed(0)
up()
goto(-4*x, -4*x)
down()
for i in range(8):
    for j in range(8):
        begin_fill()
        for k in range(4):
            fd(x)
            lt(90)
        if (j+i)%2==1:
            end_fill()
        fd(x)
    bk(8*x)
    lt(90)
    fd(x)
    rt(90)
done()
        