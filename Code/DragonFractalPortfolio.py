import turtle as tl
import numpy as np

tl.speed(0)
tl.screensize(canvwidth=10000,canvheight=10000)
C=['red','blue','yellow','green']
def Motif(l):
    tl.fd(l)
    #tl.circle(10,18)


def CI():
    return([270])

def DragonFractal(l,n):
    Path=CI()
    LastPath=[]
    for i in range(0,n):
        Path=np.concatenate((Path,LastPath))
        LastPath=[]
        for k in range(1,len(Path)+1):
            LastPath.append((Path[-k]-90)%360)

    a=0
    for k in range(0,len(Path)):
        if k==2**a:
            tl.color(C[a%4])
            a=a+1
        tl.seth(Path[k])
        Motif(l)



tl.tracer(1000)
DragonFractal(2,16)

tl.exitonclick()


