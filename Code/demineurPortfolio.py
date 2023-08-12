# This imports all functions in tkinter module
from tkinter import *
from tkinter.ttk import *
from tkinter import Tk, Button
import random
import time
import os



global start
start=0
global taille
print('Quelle taille doit faire la grille ?')
taille=int(input())
global posbombe
posbombe=0
global ze
ze=[]
global BombeRestante
BombeRestante=posbombe
global NBBombeRestante
NBBombeRestante=0
global bombeClick
bombeClick=0
10



global valeur
record=open("Demineur/RecordDemineur.txt", mode='r')
k=0
for row in record:
    if k==taille:
        valeur=row.split(' ')
        valeur=float(valeur[-1])
    k=k+1
print('le record pour ',taille,'est :',valeur)
record.close()


def BOMBE(x,y):
    global posbombe
    global BombeRestante
    global NBBombeRestante
    global bombeClick


    ze=[]
    nb_bombe=taille*taille*15//100
    NBBombeRestante=nb_bombe
    bombeClick=nb_bombe

    #print(x,y)

    VoisinStart=[]

    for k in range(0,3):
        if 0<=x-1+k<taille and 0<=y-1<taille:
            VoisinStart.append((x-1+k,y-1))
    for k in range(0,3):
        if 0<=x-1+k<taille and 0<=y+1<taille:
            VoisinStart.append((x-1+k,y+1))
    for k in range(0,3):
        if 0<=x-1+k<taille and 0<=y<taille:
            VoisinStart.append((x-1+k,y))

    #print(VoisinStart)


    posbombe=[]
    k=0
    while k!=nb_bombe:
        (i,j)=(random.randrange(0,taille),random.randrange(0,taille))
        #print(i,j)
        if (i,j) not in posbombe and (i,j) not in VoisinStart:
            posbombe.append((i,j))
            k=k+1
    #print(bombe)
    #print(posbombe)
    BombeRestante=list(posbombe)


#print(bombe,posbombe)



global z
global L
L=[]

master = Tk()
master.title("Nello's minesweeper")
#StartTime=time.time()
#timeTest=Button(f, text=time.time()-StartTime)
#timeTest.grid(column=0, row=0)



def NewRecord(temps):
    PartieEntiere=int(temps)
    PartieFractionnaire=(temps-PartieEntiere)*10**9
    if temps<valeur:
        record=open("Demineur/RecordDemineur.txt",mode='r')
        newrecord=open("Demineur/RecordDemineur2.txt",mode='w')
        k=0
        for row in record:
            if k==taille:
                newrow=row.split(' ')
                newrow[-1]=('%d' % temps)
                newrow[-1]='.'.join((newrow[-1],'%d' % PartieFractionnaire))
                test=' '.join((' '.join((newrow[0],newrow[1])),newrow[2]))
                test=test+'\n'
                newrecord.write(test)
            else:
                newrecord.write(row)
            k=k+1
        record.close()
        newrecord.close()
        newrecord=open("Demineur/RecordDemineur2.txt",mode='r')
        record=open("Demineur/RecordDemineur.txt",mode='w')
        for row in newrecord:
            record.write(row)
            #record.write('\n')
        newrecord.close()
        record.close()



def click(event):
    timeTest.configure(text=(time.time()-StartTime)*10**9//(10**9))
    global z
    global start

    if start==0:
        x = event.x_root - f.winfo_rootx()
        y = event.y_root - f.winfo_rooty()
        z = f.grid_location(x, y)
        BOMBE(z[0],z[1])
        start=1

    x = event.x_root - f.winfo_rootx()
    y = event.y_root - f.winfo_rooty()

    z = f.grid_location(x, y)

    if z in posbombe:
        master.destroy()
        print("LOOSER")
        print("LOOSER")
        print("LOOSER")
        print("LOOSER")
        print("LOOSER")
        print("LOOSER")
        print("LOOSER")
        print("LOOSER")
        print("LOOSER")

def click2(event):
    global bombeClick
    bombeClick=bombeClick-1
    timeTest.configure(text=(time.time()-StartTime)*10**9//(10**9))
    # Here retrieving the size of the parent
    # widget relative to master widget
    x = event.x_root - f.winfo_rootx()
    y = event.y_root - f.winfo_rooty()
    # Here grid_location() method is used to
    # retrieve the relative position on the
    # parent widget
    z = f.grid_location(x, y)
    # printing position
    L[z[0]][z[1]].configure(text ="!!!", bg='red')
    BombeRest.configure(text=bombeClick)
    gagne(z)
    #return(z)

# Frame widget, wil work as
# parent for buttons widget
f = Frame(master)
f.pack()


StartTime=time.time()
timeTest=Button(f, text=(time.time()-StartTime)*10**9//(10**9), width=4, height=2)
timeTest.grid(column=0, row=taille+1)
BombeRest=Button(f, text=bombeClick, width=4, height=2)
BombeRest.grid(column=1, row=taille+1)
f.pack()

def zero(x,y):
    M=[]
    a=0
    for k in range(0,3):
        if 0<=x-1+k<taille and 0<=y-1<taille and (x-1+k,y-1) not in ze:
            M.append((x-1+k,y-1))
    for k in range(0,3):
        if 0<=x-1+k<taille and 0<=y+1<taille  and (x-1+k,y+1) not in ze:
            M.append((x-1+k,y+1))
    if 0<=x-1<taille and 0<=y<taille and (x-1,y) not in ze:
        M.append((x-1,y))
    if 0<=x+1<taille and 0<=y<taille and (x+1,y) not in ze:
        M.append((x+1,y))


    for k in M:
        L[k[0]][k[1]].configure(text=voisin(k[0],k[1]), bg='pink')



def voisin(x,y):
    global ze
    M=[]
    a=0
    for k in range(0,3):
        if 0<=x-1+k<taille and 0<=y-1<taille:
            M.append((x-1+k,y-1))
    for k in range(0,3):
        if 0<=x-1+k<taille and 0<=y+1<taille:
            M.append((x-1+k,y+1))
    if 0<=x-1<taille and 0<=y<taille:
        M.append((x-1,y))
    if 0<=x+1<taille and 0<=y<taille:
        M.append((x+1,y))

    #print(x,y)
    #print(L)

    for k in range(0,len(M)):
        if (M[k][0],M[k][1]) in posbombe:
            a=a+1

    #print(a)
    if a==0:
        ze.append((x,y))
        zero(x,y)
    return(a)


def test():
    global posbombe

    x,y=z
    if (x,y) in posbombe:
        L[x][y].configure(text = "boom", bg='red')
    else:
        L[x][y].configure(text = voisin(x,y), bg='pink')


def gagne(z):
    global BombeRestante
    global NBBombeRestante

    if z in BombeRestante:
        BombeRestante.remove(z)
        NBBombeRestante=NBBombeRestante-1
    if NBBombeRestante==0:
        master.destroy()
        print('GG WP')
        print('GG WP')
        print('GG WP')
        print('GG WP')
        print('GG WP')
        print('GG WP')
        print('temps :',time.time()-StartTime)
        temps=time.time()-StartTime
        NewRecord(temps)




for i in range(0,taille):
    L.append([])
    for j in range(0,taille):
        L[i].append([])

for i in range(0,taille):
    for j in range(0,taille):
        L[i][j]=(Button(f, text="", width=4, height=2))
        L[i][j].grid(column=i, row=j)

for i in range(0,taille):
    for j in range(0,taille):
        L[i][j].configure(command=test)




# Here binding click method with mouse
master.bind("<Button-1>", click)
master.bind("<Button-3>", click2)


# infinite loop
mainloop()









