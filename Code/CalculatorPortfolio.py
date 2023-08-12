
#une calculatrice sur Tkinter
import tkinter as tk

master = tk.Tk()
master.geometry("350x600")

#initialisation des variables 
global x
x=0
global y
y=0
global w
w=0
global z
z=0
global a
a=0
global b
b=0
global c
c=0
global d
d=0
global e
e=0
global f
f=0
global g
g=0
global h
h=0
global k
k=0
global i
i=0
global j
j=0
global l
l=0
global m
m=0


def calculator():#affichage des boutons de la calculette
    master.title("Nello's calculator")
    BG = tk.Button(master, text="",width=45,height=40,bg="gold").grid(columnspan=10,rowspan=10)
    A = tk.Button(master, text="1",width=11,height=5,command=AA,bg="light blue").grid(row=4,column=1,columnspan=2)
    B = tk.Button(master, text="2",width=10,height=5,command=BB,bg="light blue").grid(row=4,column=3,columnspan=2)
    C = tk.Button(master, text="3",width=10,height=5,command=CC,bg="light blue").grid(row=4,column=5,columnspan=2)
    D = tk.Button(master, text="4",width=11,height=5,command=DD,bg="light blue").grid(row=3,column=1,columnspan=2)
    E = tk.Button(master, text="5",width=10,height=5,command=EE,bg="light blue").grid(row=3,column=3,columnspan=2)
    F = tk.Button(master, text="6",width=10,height=5,command=FF,bg="light blue").grid(row=3,column=5,columnspan=2)
    G = tk.Button(master, text="7",width=11,height=5,command=GG,bg="light blue").grid(row=2,column=1,columnspan=2)
    H = tk.Button(master, text="8",width=10,height=5,command=HH,bg="light blue").grid(row=2,column=3,columnspan=2)
    I = tk.Button(master, text="9",width=10,height=5,command=II,bg="light blue").grid(row=2,column=5,columnspan=2)
    J = tk.Button(master, text="0",width=22,height=5,command=JJ,bg="light blue").grid(row=5,columnspan=5)
    K = tk.Button(master, text=".",width=10,height=5,command=KK,bg="light blue").grid(row=5,column=5,columnspan=2)
    L = tk.Button(master, text="=",width=10,height=11,command=LL,bg="light blue").grid(column=7,columnspan=2,row=4,rowspan=2)
    M = tk.Button(master, text="+",width=10,height=11,command=MM,bg="light blue").grid(row=2,column=7,columnspan=2,rowspan=2)
    N = tk.Button(master, text="-",width=10,height=5,command=NN,bg="light blue").grid(row=0,column=7,columnspan=2)
    O = tk.Button(master, text="*",width=10,height=5,command=OO,bg="light blue").grid(row=0,column=5,columnspan=2)
    P = tk.Button(master, text="÷",width=10,height=5,command=PP,bg="light blue").grid(row=0,column=3,columnspan=2)
    Q = tk.Button(master, text="DEL",width=11,height=5,command=QQ,bg="light blue").grid(row=0,column=1,columnspan=2)
    R = tk.Button(master, text="",width=19,height=5,bg="light green").grid(row=6,column=2,columnspan=2)
    RR = tk.Button(master, text="",width=4,height=5,bg="light pink").grid(row=6,column=4,columnspan=2)
    RRR = tk.Button(master, text="",width=19,height=5,bg="light green").grid(row=6,column=6,columnspan=2)
    S = tk.Button(master, width=45,height=5,bg="orangeRed").grid(row=8,columnspan=8)
    

#x=le nombre avec lequel on veut faire des calculs
#(il est donc choisi en fonction des boutons sur lesquels appuient l'utilisateur)
def calcul(): #donne la valeur du nombre de l utilisateur a x
    global x
    global y
    global a
    if a==5:
        x=x+y/10
        a=50
    elif a==50:
        x=x+y/100
        a=500
    elif a==500:
        x=x+y/1000
        a=5000
    elif a==5000:
        x=x+y/10000
        a=50000
    elif a==50000:
        x=x+y/100000
        a=500000
    elif a==500000:
        x=x+y/1000000
        a=5000000
    elif a==5000000:
        x=x+y/10000000
        a=50000000
    elif a==50000000:
        x=x+y/100000000
        a=500000000
    else:
        x=x*10+y
    RRR = tk.Button(master, text=x,width=19,height=5,bg="light green").grid(row=6,column=6,columnspan=2)

def QQ():#delete
    global x
    x=0
    global y
    y=0
    global w
    w=0
    global z
    z=0
    global a
    a=0
    global b
    b=0
    global c
    c=0
    global d
    d=0
    global e
    e=0
    global f
    f=0
    global g
    g=0
    global h
    h=0
    global k
    k=0
    global i
    i=0
    global j
    j=0
    global l
    l=0
    global m
    m=0
    S = tk.Button(master, width=45,height=5,bg="orangeRed").grid(row=8,columnspan=8)
    R = tk.Button(master, width=19,height=5,bg="light green").grid(row=6,column=2,columnspan=2)
    RR = tk.Button(master, width=4,height=5,bg="light pink").grid(row=6,column=4,columnspan=2)
    RRR = tk.Button(master, width=19,height=5,bg="light green").grid(row=6,column=6,columnspan=2)


def KK():#la virgule 
    global a
    a=5


def LL():#le egal qui fait les calculs
    global x
    global w
    global z
    global b
    global c
    global d
    global e
    global f
    global g
    global a
    a=0
    g=f/x
    e=d*x
    z=x+w
    c=b-x
    if z>x:
        S = tk.Button(master, text=("=",z),width=45,height=5,bg="orangeRed").grid(row=8,columnspan=8)
        w=0
        x=0
    elif b>x:
        S = tk.Button(master, text=("=",c),width=45,height=5,bg="orangeRed").grid(row=8,columnspan=8)
        b=0
        x=0
    elif e>0:
        S = tk.Button(master, text=("=",e),width=45,height=5,bg="orangeRed").grid(row=8,columnspan=8)
        d=0
        x=0
    elif f>g:
        S = tk.Button(master, text=("=",g),width=45,height=5,bg="orangeRed").grid(row=8,columnspan=8)
        f=0
        x=0
    else:
        print("merde")


def NN():#soustraction
    global x
    global b
    if b>0:
        LL()
        b=c
    elif w>0:
        LL()
        b=z
    elif d>0:
        LL()
        b=e
    elif f>0:
        LL()
        b=g
    elif g>0:
        b=g
    elif e>0:
        b=e
    elif z>0:
        b=z
    else:
        b=x
        x=0
    R = tk.Button(master, text=b,width=19,height=5,bg="light green").grid(row=6,column=2,columnspan=2)
    RR = tk.Button(master, text="-",width=4,height=5,bg="light pink").grid(row=6,column=4,columnspan=2)
    RRR = tk.Button(master, width=19,height=5,bg="light green").grid(row=6,column=6,columnspan=2)
    global a
    a=0
def MM():#addition
    global x
    global w
    if w>0:
        LL()
        w=z
    elif b>0:
        LL()
        w=c
    elif d>0:
        LL()
        w=e
    elif f>0:
        LL()
        w=g
    elif g>0:
        w=g
    elif e>0:
        w=e
    elif z>0:
        w=z
    else:
        w=x
        x=0
    R = tk.Button(master, text=w,width=19,height=5,bg="light green").grid(row=6,column=2,columnspan=2)
    RR = tk.Button(master, text="+",width=4,height=5,bg="light pink").grid(row=6,column=4,columnspan=2)
    RRR = tk.Button(master, width=19,height=5,bg="light green").grid(row=6,column=6,columnspan=2)
    global a
    a=0
def OO():#multiplication
    global x
    global d
    if d>0:
        LL()
        d=e
    elif f>0:
        LL()
        d=g
    elif w>0:
        LL()
        d=z
    elif b>0:
        LL()
        d=c
    elif g>0:
        d=g
    elif e>0:
        d=e
    elif z>0:
        d=z
    else:
        d=x
        x=0
    R = tk.Button(master, text=d,width=19,height=5,bg="light green").grid(row=6,column=2,columnspan=2)
    RR = tk.Button(master, text="x",width=4,height=5,bg="light pink").grid(row=6,column=4,columnspan=2)
    RRR = tk.Button(master, width=19,height=5,bg="light green").grid(row=6,column=6,columnspan=2)
    global a
    a=0
def PP():#division
    global x
    global f
    if f>0:
        LL()
        f=g
    elif d>0:
        LL()
        f=e
    elif w>0:
        LL()
        f=z
    elif b>0:
        LL()
        f=c
    elif g>0:
        f=g
    elif e>0:
        f=e
    elif z>0:
        f=z
    else:
        f=x
        x=0
    R = tk.Button(master, text=f,width=19,height=5,bg="light green").grid(row=6,column=2,columnspan=2)
    RR = tk.Button(master, text="÷",width=4,height=5,bg="light pink").grid(row=6,column=4,columnspan=2)
    RRR = tk.Button(master, width=19,height=5,bg="light green").grid(row=6,column=6,columnspan=2)
    global a
    a=0

    
#donner la valeur a Y pour definir le nombre de l utilisateur
def AA():
    global y
    y=1
    calcul()
def BB():
    global y
    y=2
    calcul()
def CC():
    global y
    y=3
    calcul()
def DD():
    global y
    y=4
    calcul()
def EE():
    global y
    y=5
    calcul()
def FF():
    global y
    y=6
    calcul()
def GG():
    global y
    y=7
    calcul()
def HH():
    global y
    y=8
    calcul()
def II():
    global y
    y=9
    calcul()
def JJ():
    global y
    y=0
    calcul()

calculator()
tk.mainloop()


