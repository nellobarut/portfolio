#import matplotlib.pyplot as plt
#import numpy as np
import tkinter as tk
import copy


#####################GRILLE#########################
                                                   #
                                                   #
G0 =   [3,4,5,  0,0,0,  7,0,8,\
        6,1,0,  0,8,3,  5,4,9,\
        7,9,0,  0,4,5,  0,0,6,\
        0,0,0,  1,5,7,  0,0,0,\
        0,0,0,  0,6,4,  9,0,0,\
        0,7,1,  9,0,0,  4,0,0,\
        0,0,9,  0,2,0,  6,0,4,\
        0,5,0,  0,1,0,  0,0,0,\
        2,0,6,  0,0,0,  3,0,0]
                                                   #
                                                   #
####################################################

#3,4,5,  6,9,1,  7,2,8,\
#6,1,2,  7,8,3,  5,4,9,\
#7,9,8,  2,4,5,  1,3,6,\

#9,6,4,  1,5,7,  2,8,3,\
#5,2,3,  8,6,4,  9,1,7,\
#8,7,1,  9,3,2,  4,6,5,\

#1,3,9,  5,2,8,  6,7,4,\
#4,5,7,  3,1,6,  8,9,2,\
#2,8,6,  4,7,9,  3,5,1]






class caseclass:
    def __init__(self, line, col, square, value, previousvalue, initialvalue, possible):
        self.line = line
        self.col = col
        self.square = square
        self.value = value
        self.previousvalue = previousvalue
        self.initialvalue = initialvalue
        self.possible = possible

class lineclass:
    def __init__(self, value, notpossible):
        self.value = value
        self.notpossible = notpossible

class colclass:
    def __init__(self, value, notpossible):
        self.value = value
        self.notpossible = notpossible

class squareclass:
    def __init__(self, value, notpossible):
        self.value = value
        self.notpossible = notpossible

def affichage(Grille):
    master = tk.Tk()
    master.title("Nello's Sudoku Solver")
    master.geometry("1000x500")

    for k in range(0,81):
        if Grille[k].initialvalue != 0:
            color = 'blue'
        else:
            color = 'black'

        if Grille[k].value == 0:
            text = Grille[k].possible
            color = 'black'
        else:
            text = Grille[k].value

        button = tk.Button(master, text=text, fg=color, padx=10, pady=10, borderwidth=1)
        button.grid(row=Grille[k].line, column=Grille[k].col)


    master.mainloop()


G1 = []
for line in range(1,10):
    for col in range(1,10):
        square = (((line - 1) // 3) * 3 + 1 ) + (col - 1) // 3
        G1.append(caseclass(line, col, square, 0, 0, 0, [i for i in range(1,10)]))


for k in range(0,81):
    G1[k].initialvalue = G0[k]
    G1[k].value = G0[k]

Square1 = []
Line1 = []
Col1 = []
for k in range(1,10):
    Square1.append(squareclass(k, [0 for i in range(0, 9)]))
    Line1.append(lineclass(k, [0 for i in range(0, 9)]))
    Col1.append(colclass(k, [0 for i in range(0, 9)]))




def ReducePossibilities(Grille, Line, Col, Square):
    for k in range(0, 81):  # reduit les possibilites dans les lignes, colonnes, carres en fonction des valeurs deja dans la grille
        case = Grille[k]
        if case.value != 0:
            Line[case.line - 1].notpossible[case.value - 1] = case.value
            Col[case.col - 1].notpossible[case.value - 1] = case.value
            Square[case.square - 1].notpossible[case.value - 1] = case.value
            case.possible = [0,0,0,0,0,0,0,0,0]

        else:
            for i in range(1,10):
                if (i in Line[case.line - 1].notpossible) or (i in Col[case.col - 1].notpossible) or (i in Square[case.square - 1].notpossible):
                    case.possible[i - 1] = 0
        

    return(Grille, Line, Col, Square)


def NewValues(Grille, Line, Col, Square):
    for k in range(0, 81):
        case = Grille[k]
        if case.value == 0:
            L = case.possible.copy()  #seule possibilité dans la case
            while 0 in L:
                L.remove(0)
            if len(L) == 1:
                case.value = L[0]
                return (Grille)

            L = []
            for i in range(0,81):  #seule case avec x comme valeur possible dans le carre
                if Grille[i].square == case.square and Grille[i].value == 0:
                    L.append(Grille[i])

            for i in range(1,10):
                if i in Square[case.square - 1].notpossible:
                    break
                x = 0
                for j in range(0,len(L)):
                    if i in L[j].possible:
                        x = x + 1

                if x == 1:
                    for j in range(0, len(L)):
                        if i in L[j].possible:
                            for l in range(0,81):
                                if L[j] == Grille[l]:
                                    Grille[l].value = i
                            return (Grille)


            L = []
            for i in range(0, 81):  # seule case avec x comme valeur possible dans la ligne
                if Grille[i].line == case.line and Grille[i].value == 0:
                    L.append(Grille[i])

            for i in range(1, 10):
                if i in Line[case.line - 1].notpossible:
                    break
                x = 0
                for j in range(0, len(L)):
                    if i in L[j].possible:
                        x = x + 1

                if x == 1:
                    for j in range(0, len(L)):
                        if i in L[j].possible:
                            for l in range(0, 81):
                                if L[j] == Grille[l]:
                                    Grille[l].value = i
                            return (Grille)



                L = []
                for i in range(0, 81):  # seule case avec x comme valeur possible dans la colonne
                    if Grille[i].col == case.col and Grille[i].value == 0:
                        L.append(Grille[i])

                for i in range(1, 10):
                    if i in Col[case.col - 1].notpossible:
                        break
                    x = 0
                    for j in range(0, len(L)):
                        if i in L[j].possible:
                            x = x + 1

                    if x == 1:
                        for j in range(0, len(L)):
                            if i in L[j].possible:
                                for l in range(0, 81):
                                    if L[j] == Grille[l]:
                                        Grille[l].value = i
                                return (Grille)

    return(Grille)


def OneOnTwo(Grille, Line, Col, Square):
    affichage(Grille)
    global hyp
    for k in range(0,81):
        case = Grille[k]
        x = 0
        for i in range(0,len(case.possible)):
            if case.possible[i] != 0:
                x = x + 1
        if x == 2:
            hyp1 = 0
            hyp2 = 0
            for i in range(0,len(case.possible)):
                if case.possible[i] != 0:
                    if hyp1 == 0:
                        hyp1 = case.possible[i]
                    else:
                        hyp2 = case.possible[i]

            Ghyp1 = []
            Ghyp2 = []
            for j in range(0,81):
                Ghyp1.append(copy.copy(Grille[j]))
                Ghyp2.append(copy.copy(Grille[j]))

            Linehyp1 = []
            Colhyp1 = []
            Squarehyp1 = []
            Linehyp2 = []
            Colhyp2 = []
            Squarehyp2 = []
            for j in range(0,9):
                Linehyp1.append(copy.copy(Line[j]))
                Colhyp1.append(copy.copy(Col[j]))
                Squarehyp1.append(copy.copy(Square[j]))
                Linehyp2.append(copy.copy(Line[j]))
                Colhyp2.append(copy.copy(Col[j]))
                Squarehyp2.append(copy.copy(Square[j]))

            Ghyp1[k].value = hyp1
            Ghyp2[k].value = hyp2

            solver(Ghyp1, Linehyp1, Colhyp1, Squarehyp1)
            solver(Ghyp2, Linehyp2, Colhyp2, Squarehyp2)

            if Total(Ghyp1) == 405:
                return(Ghyp1)
            elif Total(Ghyp2) == 405:
                return(Ghyp2)
            else:
                if possible(Ghyp1):
                    OneOnTwo(Ghyp1, Linehyp1, Colhyp1, Squarehyp1)
                elif possible(Ghyp2):
                    OneOnTwo(Ghyp2, Linehyp2, Colhyp2, Squarehyp2)
                


            hyp = 0


def possible(Grille):
    for k in range(0,81):
        if Grille[k].possible == [0,0,0,0,0,0,0,0,0] and Grille[k].value == 0:
            return(False)
    return(True)


def Total(Grille):
    total = 0
    for k in range(0,81):
        total = total + Grille[k].value
    return(total)


hyp = 0
def solver(Grille, Line, Col, Square):
    global hyp
    n=0
    total=0
    while total != 405 and n < 50:
        n=n+1
        total = Total(Grille)
        Grille, Line, Col, Square = ReducePossibilities(Grille, Line, Col, Square)
        Grille = NewValues(Grille, Line, Col, Square)
    if Total(Grille) == 405:
        affichage(Grille)

    if Total(Grille) != 405 and hyp == 0:
        hyp = 1
        Grille=OneOnTwo(Grille, Line, Col, Square)

    #affichage(Grille)
    


solver(G1, Line1, Col1, Square1)






