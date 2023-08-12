from tkinter import *
import numpy as np

# coordonnees initiales
x01, y01 = 250, 400
x02, y02 = 600, 400
# vitesse initiale
alpha=np.pi*3/2
V0=80
frottement=0.95
# 'pas' du temps
h=0.01
z1=np.array([x01, y01, V0*np.cos(alpha), -V0*np.sin(alpha)])
z2=np.array([x02, y02, V0*np.cos(alpha), -V0*np.sin(alpha)])
def f(z):
    return np.array([z[2], z[3], 0, 9.81])


def rebond(z):
    centre=(400,400)
    #rayon est le vecteur normal a la tangente au point de contact
    rayon=(z[0] - centre[0], z[1] - centre[1])
    #a/b est le coefficient directeur de la tangente du cercle a l'endroit ou la balle rentre en collision
    a=rayon[0]
    b=rayon[1]



    i = 1
    if z[3] < 0:
        i = -1
    if z[1] < 400:
        a = -a

    V = np.sqrt(z[2] ** 2 + z[3] ** 2)
    alpha = np.arctan(a / b)
    beta = np.arctan(z[2] / V)
    gamma = beta - alpha

    T = V * np.cos(gamma)
    N = V * np.sin(gamma)

    V = V * frottement

    N = -N

    alphaprime = gamma - alpha
    z[2] = V * np.sin(alphaprime)
    z[3] = -V * np.cos(alphaprime) * i

    return(z)






def Euler():
    global z1, z2
    
    z1 = z1 + h*f(z1 + h/2*f(z1))
    dist1=np.sqrt((z1[0]-400)**2+(z1[1]-400)**2)
    if dist1>=375:
        z1 = rebond(z1)

    z2 = z2 + h*f(z2 + h/2*f(z2))
    dist2 = np.sqrt((z2[0] - 400) ** 2 + (z2[1] - 400) ** 2)
    if dist2 >= 375:
        z2 = rebond(z2)


    can1.coords(balle1, z1[0] - 15, z1[1] - 15, z1[0] + 15, z1[1] + 15)
    #can1.create_oval(z1[0], z1[1], z1[0], z1[1], width = 0, fill = 'red')
    can1.coords(balle2, z2[0] - 15, z2[1] - 15, z2[0] + 15, z2[1] + 15)
    #can1.create_oval(z2[0], z2[1], z2[0], z2[1], width = 0, fill = 'blue')
    V1=np.sqrt(z1[2]**2 + z1[3]**2)
    V2 = np.sqrt(z2[2] ** 2 + z2[3] ** 2)
    if V1>0.5 or V2>0.5:
        fen1.after(1, Euler)


# ========== Programme principal =============
# Creation de la fenetre principale :
fen1 = Tk()
fen1.title("Balle chaotique")
# creation du canvas :
H=W=800
can1 = Canvas(fen1, bg='dark grey', height=H, width=W)
can1.pack()
# creation de la balle
balle1 = can1.create_oval(x01 - 15, y01 - 15, x01 + 15, y01 + 15, width=1, fill='red')
balle2 = can1.create_oval(x02 - 15, y02 - 15, x02 + 15, y02 + 15, width=1, fill='blue')
cercle = can1.create_oval(10, 10, 790, 790, width=1)
# Lancement de la fonction Euler
Euler()
# demarrage de la boucle principale:
fen1.mainloop()