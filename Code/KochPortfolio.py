import turtle as tl

tl.speed(0)
tl.ht()
tl.tracer(1000)

tl.up()
tl.goto(-200, -200)
tl.down()

def koch(L, n):
    if n == 0:
        tl.fd(L)
        return()
    L = L / 3
    koch(L, n-1)
    tl.right(60)
    koch(L, n-1)
    tl.left(120)
    koch(L, n-1)
    tl.right(60)
    koch(L, n-1)

def fullkoch(L, n):
    for k in range(0, 3):
        koch(L, n)
        tl.left(120)



fullkoch(400, 8)
tl.update()
tl.exitonclick()