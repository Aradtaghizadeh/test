from turtle import *
ht()
speed(0)
up()
goto(-200, -200)
down()
begin_fill()
for u in range(4):
    for i in range(4):
        fd(50)
        lt(90)
    fd(100)
end_fill()
up()
goto(-200, -100)
down()
begin_fill()
for u in range(4):
    for i in range(4):
        fd(50)
        lt(90)
    fd(100)
end_fill()
up()
goto(-200, 0)
down()
begin_fill()
for u in range(4):
    for i in range(4):
        fd(50)
        lt(90)
    fd(100)
end_fill()
up()
goto(-200, 100)
down()
begin_fill()
for u in range(4):
    for i in range(4):
        fd(50)
        lt(90)
    fd(100)
end_fill()
up()
goto(-150, -150)
down()
begin_fill()
for u in range(3):
    for i in range(4):
        fd(50)
        lt(90)
    fd(100)
fd(50)
lt(90)
for s in range(4):
    fd(50)
    lt(90)
end_fill()
up()
goto(-150, -50)
down()
begin_fill()
for u in range(2):
    for i in range(4):
        fd(50)
        lt(-90)
    fd(100)
fd(50)
lt(-90)
for s in range(4):
    fd(50)
    lt(-90)    
end_fill()
fd(100)
begin_fill()
for u in range(2):
    for i in range(4):
        fd(50)
        lt(-90)
    fd(100)
for s in range(4):
    fd(50)
    lt(-90)
end_fill()  
lt(-90) 
fd(100)
begin_fill()
for u in range(2):
    for i in range(4):
        fd(50)
        lt(90)
    fd(100)
end_fill()
backward(100)
right(90)
fd(50)
begin_fill()
for i in range(4):
    fd(50)
    lt(90)
end_fill()
fd(100)
begin_fill()
for i in range(4):
    fd(50)
    lt(90)
end_fill()
right(90)
fd(50)
begin_fill()
for i in range (4):
    fd(50)
    lt(90)
end_fill()
right(90)
fd(50)
begin_fill()
for i in range (4):
    fd(50)
    lt(90)
end_fill()
up()
goto(-200, -200)
down()
for i in range(4):
    fd(400)
    lt(90)
done()