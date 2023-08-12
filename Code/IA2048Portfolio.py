import random
import turtle as tl
import time
import tkinter as tk
import math

board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
global score
score=0
global space
space=True
global pattern
pattern=0


#tl.speed(0)
#tl.ht()
#tl.tracer(10000)

def draw():
    tl.seth(0)
    tl.up()
    tl.goto(-200,200)
    tl.down()
    tl.width(4)
    for k in range(0,5):
        tl.up()
        tl.goto(-200,200-k*100)
        tl.down()
        tl.seth(0)
        tl.fd(400)

    tl.seth(270)
    tl.up()
    tl.goto(-200,200)
    tl.down()
    tl.width(4)
    for k in range(0,5):
        tl.up()
        tl.goto(-200+k*100,200)
        tl.down()
        tl.seth(270)
        tl.fd(400)



def numbers(board):
    for i in range(0,4):
        for j in range(0,4):
            style=('Courier', 30, 'bold')
            tl.up()
            tl.goto(-150+j*100,130-i*100)
            tl.down()
            tl.write(board[i][j], align='center', font=style)

def move(input, board):
    global score
    global boardmemory
    global space
    global pattern
    if input==1: #1=up
        for i in range(0,4):
            for j in range(0,3):
                if board[j][i]==board[j+1][i]:
                    board[j][i]=board[j][i]*2
                    score=score+board[j][i]
                    board[j+1][i]=0
                elif (j==0 or j==1) and board[j][i]==board[j+2][i] and board[j+1][i]==0:
                    board[j][i]=board[j][i]*2
                    score=score+board[j][i]
                    board[j+2][i]=0
                elif j==0 and board[j][i]==board[j+3][i] and board[j+1][i]==0 and board[j+2][i]==0:
                    board[j][i]=board[j][i]*2
                    score=score+board[j][i]
                    board[j+3][i]=0
        for k in range(0,3):
            for i in range(1,4):
                for j in range(0,4):
                    if board[-i][j]!=0 and board[-i-1][j]==0:
                        board[-i-1][j]=board[-i][j]
                        board[-i][j]=0

    elif input==2: #2=down
        for i in range(0,4):
            for j in range(0,3):
                if board[j][i]==board[j+1][i]:
                    board[j+1][i]=board[j+1][i]*2
                    score=score+board[j+1][i]
                    board[j][i]=0
                elif (j==0 or j==1) and board[j][i]==board[j+2][i] and board[j+1][i]==0:
                    board[j+2][i]=board[j+2][i]*2
                    score=score+board[j+2][i]
                    board[j][i]=0
                elif j==0 and board[j][i]==board[j+3][i] and board[j+1][i]==0 and board[j+2][i]==0:
                    board[j+3][i]=board[j+3][i]*2
                    score=score+board[j+3][i]
                    board[j][i]=0
        for k in range(0,3):
            for i in range(0,3):
                for j in range(0,4):
                    if board[i][j]!=0 and board[i+1][j]==0:
                        board[i+1][j]=board[i][j]
                        board[i][j]=0

    elif input==3: #3=right
        for i in range(0,3):
            for j in range(0,4):
                if board[j][i]==board[j][i+1]:
                    board[j][i+1]=board[j][i+1]*2
                    score=score+board[j][i+1]
                    board[j][i]=0
                elif (i==0 or i==1) and board[j][i]==board[j][i+2] and board[j][i+1]==0:
                    board[j][i+2]=board[j][i+2]*2
                    score=score+board[j][i+2]
                    board[j][i]=0
                elif i==0 and board[j][i]==board[j][i+3] and board[j][i+1]==0 and board[j][i+2]==0:
                    board[j][i+3]=board[j][i+3]*2
                    score=score+board[j][i+3]
                    board[j][i]=0
        for k in range(0,3):
            for i in range(0,4):
                for j in range(0,3):
                    if board[i][j]!=0 and board[i][j+1]==0:
                        board[i][j+1]=board[i][j]
                        board[i][j]=0
    else: #4=left
        for i in range(0,3):
            for j in range(0,4):
                if board[j][i]==board[j][i+1]:
                    board[j][i]=board[j][i]*2
                    score=score+board[j][i]
                    board[j][i+1]=0
                elif (i==0 or i==1) and board[j][i]==board[j][i+2] and board[j][i+1]==0:
                    board[j][i]=board[j][i]*2
                    score=score+board[j][i]
                    board[j][i+2]=0
                elif i==0 and board[j][i]==board[j][i+3] and board[j][i+1]==0 and board[j][i+2]==0:
                    board[j][i]=board[j][i]*2
                    score=score+board[j][i]
                    board[j][i+3]=0
        for k in range(0,3):
            for i in range(0,4):
                for j in range(0,3):
                    if board[i][j]==0 and board[i][j+1]!=0:
                        board[i][j]=board[i][j+1]
                        board[i][j+1]=0
    L=[]
    a=0
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j]==0:
                L.append([i,j])
                a=a+1

    b=1
    if a==0:
        b=0
        for i in range(0,4):
            for j in range(0,4):
                if i==0 and j==0:
                    if board[i][j]==board[i+1][j] or board[i][j]==board[i][j+1]:
                        b=b+1
                elif i==0 and j==3:
                    if board[i][j]==board[i+1][j] or board[i][j]==board[i][j-1]:
                        b=b+1
                elif i==0:
                    if board[i][j]==board[i+1][j] or board[i][j]==board[i][j-1] or board[i][j]==board[i][j+1]:
                        b=b+1
                elif i==3 and j==0:
                    if board[i][j]==board[i-1][j] or board[i][j]==board[i][j+1]:
                        b=b+1
                elif i==3 and j==3:
                    if board[i][j]==board[i-1][j] or board[i][j]==board[i][j-1]:
                        b=b+1
                elif i==3:
                    if board[i][j]==board[i-1][j] or board[i][j]==board[i][j-1] or board[i][j]==board[i][j+1]:
                        b=b+1
                elif i==3 and j==0:
                    if board[i][j]==board[i-1][j] or board[i][j]==board[i][j+1]:
                        b=b+1
                elif j==3:
                    if board[i][j]==board[i-1][j] or board[i][j]==board[i][j-1] or board[i][j]==board[i+1][j]:
                        b=b+1

    if board!=boardmemory and a!=0 and b!=0:
        space=add(board)
        pattern=pattern*10+input

    if b==0:
        space=False

    boardmemory=[]
    for k in range(0,4):
        boardmemory.append(board[k].copy())

    return(board)


def add(board):
    global space
    L=[]
    a=0
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j]==0:
                L.append([i,j])
                a=a+1

    if L==[]:
        space=False
        return(False)
    r=random.randrange(0,len(L))
    pos=L[r]
    if random.random()>=0.1:
        board[pos[0]][pos[1]]=2
    else:
        board[pos[0]][pos[1]]=4
    return(True)




def clear():
    for i in range(0,4):
        for j in range(0,4):
            tl.color('white')
            tl.seth(0)
            tl.up()
            tl.goto(-195+j*100,195-i*100)
            tl.down()
            tl.begin_fill()
            for k in range(0,4):
                tl.fd(90)
                tl.right(90)
            tl.end_fill()
            tl.color('black')

def reset():
    global board
    global score
    global pattern
    global space
    
    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    score = 0
    pattern = 0
    space = True



def database():
    for k in range(0,1000):
        reset()
        #draw()
        add()
        add()
        boardmemory=[]
        for k in range(0,4):
            boardmemory.append(board[k].copy())

        x=0
        while space:
            move(random.randrange(1,5))
            x=x+1

        #numbers()
        #tl.update()
        print(score)
        print(x)
        print(pattern)

        file=open("C:/Users/nello/Desktop/2048.txt","a")
        pattern=str(pattern)
        score=str(score)
        file.write(pattern)
        file.write(' score : ')
        file.write(score)
        file.write("\n")
        file.close()

    #tl.exitonclick()

    print('cest fini')


def movetest(input, board):
    boardmemory1 = []
    boardmemory2 = []
    for k in range(0, 4):
        boardmemory1.append(board[k].copy())
        boardmemory2.append(board[k].copy())

    board=boardmemory1

    global score
    global boardmemory
    global space
    global pattern

    if input == 1:  # 1=up
        for i in range(0, 4):
            for j in range(0, 3):
                if board[j][i] == board[j + 1][i]:
                    board[j][i] = board[j][i] * 2
                    board[j + 1][i] = 0
                elif (j == 0 or j == 1) and board[j][i] == board[j + 2][i] and board[j + 1][i] == 0:
                    board[j][i] = board[j][i] * 2
                    board[j + 2][i] = 0
                elif j == 0 and board[j][i] == board[j + 3][i] and board[j + 1][i] == 0 and board[j + 2][i] == 0:
                    board[j][i] = board[j][i] * 2
                    board[j + 3][i] = 0
        for k in range(0, 3):
            for i in range(1, 4):
                for j in range(0, 4):
                    if board[-i][j] != 0 and board[-i - 1][j] == 0:
                        board[-i - 1][j] = board[-i][j]
                        board[-i][j] = 0

    elif input == 2:  # 2=down
        for i in range(0, 4):
            for j in range(0, 3):
                if board[j][i] == board[j + 1][i]:
                    board[j + 1][i] = board[j + 1][i] * 2
                    board[j][i] = 0
                elif (j == 0 or j == 1) and board[j][i] == board[j + 2][i] and board[j + 1][i] == 0:
                    board[j + 2][i] = board[j + 2][i] * 2
                    board[j][i] = 0
                elif j == 0 and board[j][i] == board[j + 3][i] and board[j + 1][i] == 0 and board[j + 2][i] == 0:
                    board[j + 3][i] = board[j + 3][i] * 2
                    board[j][i] = 0
        for k in range(0, 3):
            for i in range(0, 3):
                for j in range(0, 4):
                    if board[i][j] != 0 and board[i + 1][j] == 0:
                        board[i + 1][j] = board[i][j]
                        board[i][j] = 0

    elif input == 3:  # 3=right
        for i in range(0, 3):
            for j in range(0, 4):
                if board[j][i] == board[j][i + 1]:
                    board[j][i + 1] = board[j][i + 1] * 2
                    board[j][i] = 0
                elif (i == 0 or i == 1) and board[j][i] == board[j][i + 2] and board[j][i + 1] == 0:
                    board[j][i + 2] = board[j][i + 2] * 2
                    board[j][i] = 0
                elif i == 0 and board[j][i] == board[j][i + 3] and board[j][i + 1] == 0 and board[j][i + 2] == 0:
                    board[j][i + 3] = board[j][i + 3] * 2
                    board[j][i] = 0
        for k in range(0, 3):
            for i in range(0, 4):
                for j in range(0, 3):
                    if board[i][j] != 0 and board[i][j + 1] == 0:
                        board[i][j + 1] = board[i][j]
                        board[i][j] = 0
    else:  # 4=left
        for i in range(0, 3):
            for j in range(0, 4):
                if board[j][i] == board[j][i + 1]:
                    board[j][i] = board[j][i] * 2
                    board[j][i + 1] = 0
                elif (i == 0 or i == 1) and board[j][i] == board[j][i + 2] and board[j][i + 1] == 0:
                    board[j][i] = board[j][i] * 2
                    board[j][i + 2] = 0
                elif i == 0 and board[j][i] == board[j][i + 3] and board[j][i + 1] == 0 and board[j][i + 2] == 0:
                    board[j][i] = board[j][i] * 2
                    board[j][i + 3] = 0
        for k in range(0, 3):
            for i in range(0, 4):
                for j in range(0, 3):
                    if board[i][j] == 0 and board[i][j + 1] != 0:
                        board[i][j] = board[i][j + 1]
                        board[i][j + 1] = 0

    return(boardmemory1==boardmemory2)



def nextmove():
    global score
    global space
    global board
    global boardmemory

    board1 = []
    board2 = []
    board3 = []
    board4 = []
    for k in range(0,4):
        board1.append(board[k].copy())
        board2.append(board[k].copy())
        board3.append(board[k].copy())
        board4.append(board[k].copy())

    B=[board1,board2,board3,board4]

    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0

    S=[s1,s2,s3,s4]

    for k in range(0,4):
        boardmemory = []
        for n in range(0, 4):
            boardmemory.append(B[k][n].copy())


        if movetest(k+1,B[k])==False:
            B[k] = move(k+1,B[k])

            boardmemoryTempo = []
            for n in range(0, 4):
                boardmemoryTempo.append(B[k][n].copy())

            x=0
            while x<80:
                B[k] = []
                for i in range(0,4):
                    B[k].append(boardmemoryTempo[i].copy())
                while space:
                    B[k] = move(random.randrange(1, 5), B[k])
                    S[k] = S[k] + score

                space = True
                x = x + 1
                score = 0

        else:
            S[k]=-1

    max = S[0]
    m = 1
    for k in range(1,4):
        if max < S[k]:
            m = k+1
            max = S[k]
    nextmove = m
    return(nextmove)


master=tk.Tk()
master.title("2048")
master.geometry("375x400")

def gridTkinter():
    global GridTk
    
    GridTk = []
    for i in range(0, 4):
        L= []
        for j in range(0, 4):
            L.append(tk.Button(master, text=str(i)+str(j), height = 6, width = 12))
            L[-1].grid(row=i,column=j)
        GridTk.append(L)
            
    #master.mainloop()
    
gridTkinter()

Color = ['#fef1a2', '#ffc04c', '#ffa500', '#ff7f50', '#d05134', '#FF0000', '#610B0B', '#01DF01', '#04B4AE', '#0040FF', '#FF00FF', '#8A084B', '#F7819F', '#088A68']

def updateTk():
    global GridTk
    global board
    global Color

    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] == 0:
                GridTk[i][j].config(text=str(board[i][j]), bg=Color[int(math.log2(1))])
            else:
                GridTk[i][j].config(text=str(board[i][j]), bg=Color[int(math.log2(board[i][j]))])
    
    master.after(1, montecarlo)     
            

def montecarlo():
    global board
    global space
    global score


    if space:
        board = move(nextmove(), board)
        updateTk()


reset()
add(board)
add(board)

montecarlo()

master.mainloop()




