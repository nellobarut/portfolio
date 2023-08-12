import turtle as tl
from random import *



tl.speed(0)
tl.tracer(10000)
tl.ht()
tl.up()
tl.goto(-300,-300)
#tl.down()
for k in range(0,3):
    tl.fd(700)
    tl.left(120)


Sommet=[[-300,-300],[400,-300],[50.00,306.22]]


tl.up()
tl.goto(randrange(0,100),randrange(0,100))
tl.down()
tl.dot(4)


fractal=100000
for i in range(0,fractal):
    tl.up()
    x=tl.xcor()
    y=tl.ycor()
    a=randrange(0,3)
    tl.goto((x+Sommet[a][0])/2,(y+Sommet[a][1])/2)
    tl.down()
    tl.dot(2)

tl.update()
print('finish')
tl.exitonclick()