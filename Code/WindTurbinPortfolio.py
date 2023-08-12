import numpy as np
import matplotlib.pyplot as plt
import math


#variable
rho=1.225 #masse volumique de l air
largeur=0.3 #largeur de la pale en metre
omega=np.pi/4 #vitesse de rotation en rad/s
r=40 #longueur de la pale en metre
phi=0 #angle d'écoulement
u=10 #vitesse du vent

file1=open("WindTurbin/naca_0012.txt","r")
file2=open("WindTurbin/naca_23012.txt","r")
file3=open("WindTurbin/naca_4412.txt","r")

def regpol(abs, ord, degre):
  abs = np.array(abs)
  ord = np.array(ord)
  degre = degre + 1
  n = abs.shape[0]
  X = np.full(n, 1, float)
  for k in range(1, degre + 1):
    X = np.c_[X, np.power(abs, k)]
  ome = np.dot(np.linalg.inv(np.dot(np.transpose(X), X)), np.dot(np.transpose(X), ord))

  Y = np.zeros(n, float)
  for k in range(degre):
    Y = Y + ome[k] * np.power(abs, k)
  return(Y, np.poly1d(ome))


def Graph(file,nb):
  alpha=[]
  Cd=[]
  Cl=[]

  a=0
  for row in file:
      if a==0:
          a=1
      else:
          x=row.split(',')
          alpha.append(float(x[0]))
          Cd.append(float(x[1]))
          Cl.append(float(x[2]))


  degre = 10
  Y1bis = regpol(alpha, Cd, degre)[0]    #polynome obtenu avec la regression polynomiale regpol
  Y2bis = regpol(alpha, Cl, degre)[0]    #polynome obtenu avec la regression polynomiale regpol
  polynome1=np.polyfit(alpha, Cd, degre) #polynome obtenu avec la regression polynomiale de numpy
  polynome2=np.polyfit(alpha, Cl, degre) #polynome obtenu avec la regression polynomiale de numpy
  Y1=[]
  Y2=[]
  X=[]
  x=-15
  n=len(alpha)
  step=35/n

  for k in range(0,n):
    y1=0
    y2=0
    for i in range(0,degre+1):
      y1=y1+polynome1[i]*x**(degre-i)
      y2=y2+polynome2[i]*x**(degre-i)
    Y1.append(y1)
    Y2.append(y2)
    X.append(x)
    x=x+step


  plt.plot(alpha, Cd, 'ro')
  plt.plot(X, Y1bis, c="blue", label="a la main")
  plt.plot(X, Y1, c='green', label="avec numpy")
  plt.legend()
  plt.axis([-15,20,0,0.15])
  plt.title("file%d" % nb)
  plt.xlabel('alpha')
  plt.ylabel('Cd')
  plt.show()

  plt.plot(alpha, Cl, 'ro')
  plt.plot(X, Y2bis, c="blue", label="a la main")
  plt.plot(X, Y2, c="green", label="avec numpy")
  plt.legend()
  plt.title("file%d" % nb)
  plt.xlabel('alpha')
  plt.ylabel('Cl')
  plt.axis([-15,20,-2,2])
  plt.show()

  return(Y1,Y2,X)


Graph(file1,1)
Graph(file2,2)
Graph(file3,3)


def Valeur(file,nb):
  alpha=[]
  Cd=[]
  Cl=[]

  a=0
  for row in file:
      if a==0:
          a=1
      else:
          x=row.split(',')
          alpha.append(float(x[0]))
          Cd.append(float(x[1]))
          Cl.append(float(x[2]))


  degre = 10
  polynome1=np.polyfit(alpha, Cd, degre) #polynome obtenu avec la regression polynomiale de numpy
  polynome2=np.polyfit(alpha, Cl, degre) #polynome obtenu avec la regression polynomiale de numpy
  Y1=[]
  Y2=[]
  X=[]
  x=-15
  n=len(alpha)
  step=35/n

  for k in range(0,n):
    y1=0
    y2=0
    for i in range(0,degre+1):
      y1=y1+polynome1[i]*x**(degre-i)
      y2=y2+polynome2[i]*x**(degre-i)
    Y1.append(y1)
    Y2.append(y2)
    X.append(x)
    x=x+step

  return(Y1,Y2,X)

def finesse(file, nb):
  file.seek(0)
  Cd,Cl,alpha=Valeur(file, nb)
  f=[]
  for k in range(0,len(Cd)):
    f.append(Cl[k]/Cd[k])

  n=len(alpha)
  max=0
  pos=200
  for k in range(5,len(f)):
    if max<f[k]:
      max=f[k]
      pos=k
  print('fmax',max,'alpha',(pos*35/len(f))-15)

  plt.plot(alpha, f)
  plt.grid()
  plt.title("file%d" % nb)
  plt.xlabel('alpha')
  plt.ylabel('Cl/Cd')
  plt.show()

  return((pos*35/n)-15)


finesse(file1, 1)
finesse(file2, 2)
finesse(file3, 3)


def Valeur(file,nb):
  alpha=[]
  Cd=[]
  Cl=[]

  a=0
  for row in file:
      if a==0:    #la premiere ligne des documents ne nous interessent pas
          a=1
      else:
          x=row.split(',')         #on crée 3 listes, une par colonne
          alpha.append(float(x[0]))
          Cd.append(float(x[1]))
          Cl.append(float(x[2]))


  degre = 10
  polynome1=np.polyfit(alpha, Cd, degre) #polynome obtenu avec la regression polynomiale de numpy
  polynome2=np.polyfit(alpha, Cl, degre) #polynome obtenu avec la regression polynomiale de numpy
  Y1=[]
  Y2=[]
  X=[]
  x=-15
  n=len(alpha)
  step=35/n

  for k in range(0,n):
    y1=0
    y2=0
    for i in range(0,degre+1):       #calcul de la valeur de cl ou cd avec les regression
      y1=y1+polynome1[i]*x**(degre-i)
      y2=y2+polynome2[i]*x**(degre-i)
    Y1.append(y1)                    #création des listes de cd ou cl pour les tracer avec matplotlib
    Y2.append(y2)
    X.append(x)                      #création de la liste des abscisses
    x=x+step

  return(Y1,Y2,X)

def finesse(file, nb):
  file.seek(0)                       #remet la lecture des documents a la ligen 0
  Cd,Cl,alpha=Valeur(file, nb)
  f=[]
  for k in range(0,len(Cd)):
    f.append(Cl[k]/Cd[k])            #création de la liste du module de finesse

  n=len(alpha)
  max=0
  pos=5
  for k in range(5,len(f)):          #on ne prend pas en compte les premieres valeurs (car les regressions sont moches en ces points)
    if max<f[k]:
      max=f[k]                       #pour la valeur amax de f, on note la valeur de alpha
      pos=k

  return((pos*35/n)-15)

def dFlfct(r,dr,rho,omega,alpha,file):
  file.seek(0)
  Alpha=[]
  Cl=[]
  dS=r*dr                      #élément de surface de dS (pale rectangulaire)

  a=0
  for row in file:
      if a==0:
        a=1
      else:
        x=row.split(',')
        Alpha.append(float(x[0]))
        Cl.append(float(x[2]))

  degre=10
  polynome=np.polyfit(Alpha, Cl, degre)
  Cl=0
  for k in range(0,degre+1):
    Cl=Cl+alpha**(degre-k)*polynome[k]    #on determine cl en alpha
  return((1/2)*rho*((u**2)+(omega*r)**2)*dS*Cl)  #on calcule la valeur de la force en r sur la surface dS



def dFdfct(r,dr,rho,omega,alpha,file):
  file.seek(0)
  Alpha=[]
  Cd=[]
  dS=r*dr

  a=0
  for row in file:
      if a==0:
        a=1
      else:
        x=row.split(',')
        Alpha.append(float(x[0]))
        Cd.append(float(x[1]))

  degre=10
  polynome=np.polyfit(Alpha, Cd, degre)
  Cd=0
  for k in range(0,degre+1):
    Cd=Cd+alpha**(degre-k)*polynome[k]    #on determien cd en alpha
  return(((1/2)*rho*(u**2+(omega*r)**2)*dS*Cd))  #on calcule la valeur de la force en r sur la surface dS




def dCfct(r,dFl,dFd,beta): #alpha = beta car phi = 0
  return(r*(dFl*np.cos(beta) + dFd*np.sin(beta)))   #force projeté sur les axes er et eteta



def Cfct(r, file, nb):
  C=0
  precision=1000   #on définit la précision de notre méthode d'intégration numérique
  step=r/precision
  alpha = finesse(file, nb)
  alpha = alpha*2*np.pi/360   #on met alpha en radiant
  for k in range(0,precision + 1):
    dFl = dFlfct(k*step,step,rho,omega,alpha,file)
    dFd = dFdfct(k*step,step,rho,omega,alpha,file)
    C = C + dCfct(k*step,dFl,dFd,alpha)  #on somme les valeurs de dC sur toute la longueur de la pale pour obtenir le couple total
  return(C)



def puissance(C,omega):
  return(C*omega)    #calcul de la puissance

p2=puissance(Cfct(r, file2, 2),omega)/1000 #puissance file2
p3=puissance(Cfct(r, file3, 3),omega)/1000 #puissance file3

print('Puissance', (p2+p3)/2, 'kW')  #puissance moyenne du file1 et du file2


#variable
rho=1.225 #masse volumique de l air
#largeur=3 #largeur de la pale en metre
omega=np.pi/2 #vitesse de rotation en rad/s
r=50 #longueur de la pale en metre
phi=0 #angle d'écoulement
u=10 #vitesse du vent


#definissons un profil de pale d 'éolienne, on souhaite le rapport l/r = 0.06 (valeur trouvé sur internet)
#avec r = 50, donc l (au max) vaut 2.98
#on modélise la pale par un ovale avec 2 polynomes de degrés 2 comme courbure
#voir le graph si dessous
x=np.linspace(0,50,1000)
#fig, axs = plt.subplots(3, 1)
plt.ylim((-50,50))
plt.plot(x, -(x+50)*(x-50)/1680)
plt.plot(x, (x+50)*(x-50)/1680)
plt.title("profil d'une pale d'éolienne")
plt.show()



def Valeur(file,nb):
  alpha=[]
  Cd=[]
  Cl=[]

  a=0
  for row in file:
      if a==0:    #la premiere ligne des documents ne nous interessent pas
          a=1
      else:
          x=row.split(',')         #on crée 3 listes, une par colonne
          alpha.append(float(x[0]))
          Cd.append(float(x[1]))
          Cl.append(float(x[2]))


  degre = 10
  polynome1=np.polyfit(alpha, Cd, degre) #polynome obtenu avec la regression polynomiale de numpy
  polynome2=np.polyfit(alpha, Cl, degre) #polynome obtenu avec la regression polynomiale de numpy
  Y1=[]
  Y2=[]
  X=[]
  x=-15
  n=len(alpha)
  step=35/n

  for k in range(0,n):
    y1=0
    y2=0
    for i in range(0,degre+1):       #calcul de la valeur de cl ou cd avec les regression
      y1=y1+polynome1[i]*x**(degre-i)
      y2=y2+polynome2[i]*x**(degre-i)
    Y1.append(y1)                    #création des listes de cd ou cl pour les tracer avec matplotlib
    Y2.append(y2)
    X.append(x)                      #création de la liste des abscisses
    x=x+step

  return(Y1,Y2,X)

def finesse(file, nb):
  file.seek(0)                       #remet la lecture des documents a la ligen 0
  Cd,Cl,alpha=Valeur(file, nb)
  f=[]
  for k in range(0,len(Cd)):
    f.append(Cl[k]/Cd[k])            #création de la liste du module de finesse

  n=len(alpha)
  max=0
  pos=5
  for k in range(5,len(f)):          #on ne prend pas en compte les premieres valeurs (car les regressions sont moches en ces points)
    if max<f[k]:
      max=f[k]                       #pour la valeur amax de f, on note la valeur de alpha
      pos=k

  return((pos*35/n)-15)

def dFlfct(r,dr,rho,omega,alpha,file):
  file.seek(0)
  Alpha=[]
  Cl=[]
  largeur=-2*(r+50)*(r-50)/1680      #largeur de la pale en r
  dS=largeur*dr                      #élément de surface de dS

  a=0
  for row in file:
      if a==0:
        a=1
      else:
        x=row.split(',')
        Alpha.append(float(x[0]))
        Cl.append(float(x[2]))

  degre=10
  polynome=np.polyfit(Alpha, Cl, degre)
  Cl=0
  for k in range(0,degre+1):
    Cl=Cl+alpha**(degre-k)*polynome[k]    #on determien cl en alpha
  return((1/2)*rho*((u**2)+(omega*r)**2)*dS*Cl)  #on calcule la valeur de la force en r sur la surface dS



def dFdfct(r,dr,rho,omega,alpha,file):
  file.seek(0)
  Alpha=[]
  Cd=[]
  largeur=-2*(r+50)*(r-50)/1680
  dS=largeur*dr

  a=0
  for row in file:
      if a==0:
        a=1
      else:
        x=row.split(',')
        Alpha.append(float(x[0]))
        Cd.append(float(x[1]))

  degre=10
  polynome=np.polyfit(Alpha, Cd, degre)
  Cd=0
  for k in range(0,degre+1):
    Cd=Cd+alpha**(degre-k)*polynome[k]    #on determien cd en alpha
  return(((1/2)*rho*(u**2+(omega*r)**2)*dS*Cd))  #on calcule la valeur de la force en r sur la surface dS




def dCfct(r,dFl,dFd,beta): #alpha = beta car phi = 0
  return(r*(dFl*np.cos(beta) + dFd*np.sin(beta)))   #force projeté sur les axes er et eteta



def Cfct(r, file, nb):
  C=0
  precision=1000   #on définit la précision de notre méthode d'intégration numérique
  step=r/precision
  alpha = finesse(file, nb)
  alpha = alpha*2*np.pi/360   #on met alpha en radiant
  for k in range(0,precision + 1):
    dFl = dFlfct(k*step,step,rho,omega,alpha,file)
    dFd = dFdfct(k*step,step,rho,omega,alpha,file)
    C = C + dCfct(k*step,dFl,dFd,alpha)  #on somme les valeurs de dC sur toute la longueur de la pale pour obtenir le couple total
  return(C)



def puissance(C,omega):
  return(C*omega)    #calcul de la puissance

print('Puissance', puissance(Cfct(r, file2, 2),omega)/1000, 'kW')

def Valeur(file,nb):
  alpha=[]
  Cd=[]
  Cl=[]

  a=0
  for row in file:
      if a==0:    #la premiere ligne des documents ne nous interessent pas
          a=1
      else:
          x=row.split(',')         #on crée 3 listes, une par colonne
          alpha.append(float(x[0]))
          Cd.append(float(x[1]))
          Cl.append(float(x[2]))


  degre = 10
  polynome1=np.polyfit(alpha, Cd, degre) #polynome obtenu avec la regression polynomiale de numpy
  polynome2=np.polyfit(alpha, Cl, degre) #polynome obtenu avec la regression polynomiale de numpy
  Y1=[]
  Y2=[]
  X=[]
  x=-15
  n=len(alpha)
  step=35/n

  for k in range(0,n):
    y1=0
    y2=0
    for i in range(0,degre+1):       #calcul de la valeur de cl ou cd avec les regression
      y1=y1+polynome1[i]*x**(degre-i)
      y2=y2+polynome2[i]*x**(degre-i)
    Y1.append(y1)                    #création des listes de cd ou cl pour les tracer avec matplotlib
    Y2.append(y2)
    X.append(x)                      #création de la liste des abscisses
    x=x+step

  return(Y1,Y2,X)

def finesse(file, nb):
  file.seek(0)                       #remet la lecture des documents a la ligen 0
  Cd,Cl,alpha=Valeur(file, nb)
  f=[]
  for k in range(0,len(Cd)):
    f.append(Cl[k]/Cd[k])            #création de la liste du module de finesse

  n=len(alpha)
  max=0
  pos=5
  for k in range(5,len(f)):          #on ne prend pas en compte les premieres valeurs (car les regressions sont moches en ces points)
    if max<f[k]:
      max=f[k]                       #pour la valeur amax de f, on note la valeur de alpha
      pos=k

  return((pos*35/n)-15)

def dFlfct(r,dr,rho,omega,alpha,file):
  file.seek(0)
  Alpha=[]
  Cl=[]
  largeur=-2*(r+50)*(r-50)/1680      #largeur de la pale en r
  dS=largeur*dr                      #élément de surface de dS

  a=0
  for row in file:
      if a==0:
        a=1
      else:
        x=row.split(',')
        Alpha.append(float(x[0]))
        Cl.append(float(x[2]))

  degre=10
  polynome=np.polyfit(Alpha, Cl, degre)
  Cl=0
  for k in range(0,degre+1):
    Cl=Cl+alpha**(degre-k)*polynome[k]    #on determien cl en alpha
  return((1/2)*rho*((u**2)+(omega*r)**2)*dS*Cl)  #on calcule la valeur de la force en r sur la surface dS



def dFdfct(r,dr,rho,omega,alpha,file):
  file.seek(0)
  Alpha=[]
  Cd=[]
  largeur=-2*(r+50)*(r-50)/1680
  dS=largeur*dr

  a=0
  for row in file:
      if a==0:
        a=1
      else:
        x=row.split(',')
        Alpha.append(float(x[0]))
        Cd.append(float(x[1]))

  degre=10
  polynome=np.polyfit(Alpha, Cd, degre)
  Cd=0
  for k in range(0,degre+1):
    Cd=Cd+alpha**(degre-k)*polynome[k]    #on determien cd en alpha
  return(((1/2)*rho*(u**2+(omega*r)**2)*dS*Cd))  #on calcule la valeur de la force en r sur la surface dS




def dCfct(r,dFl,dFd,beta): #alpha = beta car phi = 0
  return(r*(dFl*np.cos(beta) + dFd*np.sin(beta)))   #force projeté sur les axes er et eteta



def Cfct(r, file, nb):
  C=0
  precision=100   #on définit la précision de notre méthode d'intégration numérique
  step=r/precision
  alpha = finesse(file, nb)
  alpha = alpha*2*np.pi/360   #on met alpha en radiant
  for k in range(0,precision + 1):
    dFl = dFlfct(k*step,step,rho,omega,alpha,file)
    dFd = dFdfct(k*step,step,rho,omega,alpha,file)
    C = C + dCfct(k*step,dFl,dFd,alpha)  #on somme les valeurs de dC sur toute la longueur de la pale pour obtenir le couple total
  return(C)



def puissance(C,omega):
  return(C*omega)    #calcul de la puissance

U=[]
for k in range(0,100):
  U.append(k/4)

P=[]
for k in range(0,100):
  u=U[k]
  P.append(puissance(Cfct(r, file2, 2),omega)/1000)

plt.plot(U, P)
plt.grid()
plt.title("Puissance de l'éolienne en fonction de la vitesse du vent")
plt.xlabel('Vitesse du vent (m/s)')
plt.ylabel('Puissance (kW)')
plt.show()

V=[5.45, 7.36, 8.54, 9.78, 10.49]
alt=[10, 50, 100, 150, 200]


def logvent(z):
  z0=0.003           #coefficient de rugosité
  v0=0.7571          
  return(v0*np.log(z/z0))



degre = 2
polynome=np.polyfit(alt, V, degre)
X=[]
Y1=[]
Y2=[]
x=1
for k in range(0,1000):
    y=0
    for i in range(0,degre + 1):
      y=y+polynome[i]*x**(degre-i)
    Y1.append(y)
    Y2.append(logvent(x))
    X.append(x)
    x=x+500/1000




plt.plot(V, alt, label="courbe d'après les valeurs du site Global Wind Atlas")
plt.plot(Y1, X, label="profil quadratique extrapolé jusqu'à 500m")
plt.plot(Y2, X, label="profil logarithmique extrapolé jusqu'à 500m")
plt.legend()
plt.title("vitesse du vent en fonction de l'altitude")
plt.ylabel('altitude (en m)')
plt.xlabel('vitesse du vent (en m/s)')
plt.show()


import pandas as pd

with open('WindTurbin/windSpeed.csv', 'r') as f:
  windSpeed = pd.read_csv(f, usecols=[0])

  firstline = 0
  a = 0
  u = 0
  for k in range(0, windSpeed.size):
    a = a + 1
    u = u + float(windSpeed.loc[k]['val'])

  u = u / a
  #print(u)


with open('WindTurbin/annualData.csv', 'r') as f:
  annualData = pd.read_csv(f, usecols=[1])

  firstline = 0
  a = 0
  uannual = 0
  for k in range(0, annualData.size):
    a = a + 1
    uannual = uannual + float(annualData.loc[k]['value']) * u

  uannual = uannual / a
  #print(uannual)

with open('WindTurbin/interAnnualData.csv', 'r') as f:
  interAnnualData = pd.read_csv(f, usecols=[1])

  firstline = 0
  a = 0
  uinterannual = 0
  for k in range(0, interAnnualData.size):
    a = a + 1
    uinterannual = uinterannual + float(interAnnualData.loc[k]['value']) * u

  uinterannual = uinterannual / a
  #print(uinterannual)


#variable
rho=1.225 #masse volumique de l air
rayon=1.25 #rayon de la pâle en mètre
omega=np.pi/2 #vitesse de rotation en rad/s
r=20 #longueur de la pale en metre
phi=0 #angle d'écoulement
u=uinterannual #vitesse du vent


def Valeur(file,nb):
  alpha=[]
  Cd=[]
  Cl=[]

  a=0
  for row in file:
      if a==0:    #la premiere ligne des documents ne nous interessent pas
          a=1
      else:
          x=row.split(',')         #on crée 3 listes, une par colonne
          alpha.append(float(x[0]))
          Cd.append(float(x[1]))
          Cl.append(float(x[2]))


  degre = 10
  polynome1=np.polyfit(alpha, Cd, degre) #polynome obtenu avec la regression polynomiale de numpy
  polynome2=np.polyfit(alpha, Cl, degre) #polynome obtenu avec la regression polynomiale de numpy
  Y1=[]
  Y2=[]
  X=[]
  x=-15
  n=len(alpha)
  step=35/n

  for k in range(0,n):
    y1=0
    y2=0
    for i in range(0,degre+1):       #calcul de la valeur de cl ou cd avec les regression
      y1=y1+polynome1[i]*x**(degre-i)
      y2=y2+polynome2[i]*x**(degre-i)
    Y1.append(y1)                    #création des listes de cd ou cl pour les tracer avec matplotlib
    Y2.append(y2)
    X.append(x)                      #création de la liste des abscisses
    x=x+step

  return(Y1,Y2,X)

def finesse(file, nb):
  file.seek(0)                       #remet la lecture des documents a la ligen 0
  Cd,Cl,alpha=Valeur(file, nb)
  f=[]
  for k in range(0,len(Cd)):
    f.append(Cl[k]/Cd[k])            #création de la liste du module de finesse

  n=len(alpha)
  max=0
  pos=5
  for k in range(5,len(f)):          #on ne prend pas en compte les premieres valeurs (car les regressions sont moches en ces points)
    if max<f[k]:
      max=f[k]                       #pour la valeur amax de f, on note la valeur de alpha
      pos=k

  return((pos*35/n)-15)

def dFlfct(r,dr,rho,omega,alpha,file):
  file.seek(0)
  Alpha=[]
  Cl=[]
  dS=rayon*dr                      #élément de surface de dS (pale rectangulaire)

  a=0
  for row in file:
      if a==0:
        a=1
      else:
        x=row.split(',')
        Alpha.append(float(x[0]))
        Cl.append(float(x[2]))

  degre=10
  polynome=np.polyfit(Alpha, Cl, degre)
  Cl=0
  for k in range(0,degre+1):
    Cl=Cl+alpha**(degre-k)*polynome[k]    #on determine cl en alpha
  return((1/2)*rho*((u**2)+(omega*r)**2)*dS*Cl)  #on calcule la valeur de la force en r sur la surface dS



def dFdfct(r,dr,rho,omega,alpha,file):
  file.seek(0)
  Alpha=[]
  Cd=[]
  dS=rayon*dr

  a=0
  for row in file:
      if a==0:
        a=1
      else:
        x=row.split(',')
        Alpha.append(float(x[0]))
        Cd.append(float(x[1]))

  degre=10
  polynome=np.polyfit(Alpha, Cd, degre)
  Cd=0
  for k in range(0,degre+1):
    Cd=Cd+alpha**(degre-k)*polynome[k]    #on determien cd en alpha
  return(((1/2)*rho*(u**2+(omega*r)**2)*dS*Cd))  #on calcule la valeur de la force en r sur la surface dS




def dCfct(r,dFl,dFd,beta): #alpha = beta car phi = 0
  return(r*(dFl*np.cos(beta) + dFd*np.sin(beta)))   #force projeté sur les axes er et eteta



def Cfct(r, file, nb):
  C=0
  precision=1000   #on définit la précision de notre méthode d'intégration numérique
  step=r/precision
  alpha = finesse(file, nb)
  alpha = alpha*2*np.pi/360   #on met alpha en radiant
  for k in range(0,precision + 1):
    dFl = dFlfct(k*step,step,rho,omega,alpha,file)
    dFd = dFdfct(k*step,step,rho,omega,alpha,file)
    C = C + dCfct(k*step,dFl,dFd,alpha)  #on somme les valeurs de dC sur toute la longueur de la pale pour obtenir le couple total
  return(C)



def puissance(C,omega):
  return(C*omega)    #calcul de la puissance

p2=puissance(Cfct(r, file2, 2),omega)/1000 #puissance file2
p3=puissance(Cfct(r, file3, 3),omega)/1000 #puissance file3

print('Puissance moyenne annuelle', (p2+p3)/2, 'kW')  #puissance moyenne du file1 et du file2


with open('WindTurbin/annualData.csv', 'r') as f:
  annualData = pd.read_csv(f, usecols=[1])

  firstline = 0
  Pmonth = []
  for k in range (0, annualData.size):
    u=uinterannual*float(annualData.loc[k]['value'])
    p2=puissance(Cfct(r, file2, 2),omega)/1000 #puissance file2
    p3=puissance(Cfct(r, file3, 3),omega)/1000 #puissance file3
    Pmonth.append((p2+p3)/2)

plt.plot(['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'décembre'], Pmonth)
plt.title("Puissance du vent en fonction du mois")
plt.ylabel('puissance (en kW)')
plt.xlabel("mois de l'année")
plt.xticks(rotation = 60)
plt.show()

import random
import turtle as tl

tl.ht()
tl.speed(0)
tl.tracer(100)

D = 13  #diametre eolienne 130 m
k = 0.1
v0 = 10 #vitesse du vent 10 m.s-1
L = 150 #longueur du coté de la parcelle carrée 1500 m (surface = 2250000 m2)



def vw(x, D, k, v0):
    return (v0 * (1 - 1 / 3) / (1 + (2 * k * x / D) ** 2))


def Dwake(x):
    global D
    global k
    global L

    return (np.sqrt(2) * D + 2 * k * x)


def eolienne(L, D):
    Pos = []
    echec = 0
    while echec < 100:
        echec = echec + 1
        x, y = random.randrange(0, L), random.randrange(0, L)
        xg, xd, yh, yb = x - 9/2 * D, x + 9/2 * D, y + 3/2 * D, y - 3/2 * D
        #xg, xd, yh, yb = x - 5 / 2 * D, x + 5 / 2 * D, y + 5 / 2 * D, y - 5 / 2 * D
        condition = True
        for i in range(0, len(Pos)):
            if xg <= Pos[i][0] <= xd and yb <= Pos[i][1] <= yh:
                condition = False

        if condition:
            Pos.append([x, y])
            echec = 0

    return (Pos)

def rectangle(l, L):
    global D
    global k

    tl.color('red')
    tl.begin_fill()
    for i in range(0, 2):
        tl.fd(L)
        tl.right(90)
        tl.fd(l)
        tl.right(90)
    tl.end_fill()
    tl.color('black')

def cone(Lpos):
    global D
    global k
    global L

    ylim = -10
    for i in range(0, len(Lpos)):
        tl.color('blue')
        tl.up()
        tl.goto(Lpos[i][0]-D/2-L/2, Lpos[i][1]-L/2)
        tl.down()
        tl.goto(Lpos[i][0]-Dwake(abs(Lpos[i][1]-ylim))/2-L/2, ylim-L/2)
        tl.goto(Lpos[i][0]+Dwake(abs(Lpos[i][1]-ylim))/2-L/2, ylim-L/2)
        tl.goto(Lpos[i][0]+D/2-L/2, Lpos[i][1]-L/2)
        tl.goto(Lpos[i][0]-D/2-L/2, Lpos[i][1]-L/2)




def champEol(Li):
    global D
    global L

    tl.up()
    tl.goto(-L/2, L/2)
    tl.down()
    for i in range(0, 4):
        tl.fd(L)
        tl.right(90)

    for i in Li:
        tl.up()
        tl.goto(i)
        x, y = tl.pos()
        tl.goto(x-L/2-9*D/4, y-L/2+3*D/4)
        tl.down()
        rectangle(3/2*D, 9/2*D)
        tl.up()
        tl.goto(x-L/2, y-L/2)
        tl.dot(6)
        tl.down()

def sillage(Liste):
    global D
    global k
    global L

    S = []
    for i in range(0,len(Liste)):
        s = []
        for j in range(0,len(Liste)):
            if j != i:
                if Dwake(abs(Liste[i][1]-Liste[j][1]))/2 > abs(Liste[i][0]-Liste[j][0]) and Liste[i][1] < Liste[j][1]:
                    s.append(j)
        S.append(s)
    return(S)



def vitesse(s):
    global k
    global D
    global S
    global V
    global P
    global index

    if s==[]:
        v = v0
        return(v)
    else:
        condition = True
        for i in range(0, len(s)):
            if V[s[i]] == 0:
                condition = False
        if condition:
            v = v0
            for i in range(0, len(s)):
                v = v - vw(abs(P[s[i]][1]-P[index][1]), D, k, v)
            return(v)
        else:
            return(0)


P=eolienne(L, D)
S=sillage(P)
V = []

for i in range(0, len(P)):
    V.append(0)

index = 0
while 0 in V:
    index = (index + 1) % len(V)
    if V[index] == 0:
        V[index] = vitesse(S[index])

print("La liste de la position de chaque éolienne : ", P)
print("La liste de la vitesse du vent pour chaque éolienne : ",V)


champEol(P)
cone(P)
tl.update()
tl.exitonclick()


#variable
rho=1.225 #masse volumique de l air
rayon=1.25 #rayon de la pâle en mètre
omega=np.pi/2 #vitesse de rotation en rad/s
r=65 #longueur de la pale en metre
phi=0 #angle d'écoulement
u=10 #vitesse du vent

def Valeur(file,nb):
  alpha=[]
  Cd=[]
  Cl=[]

  a=0
  for row in file:
      if a==0:    #la premiere ligne des documents ne nous interessent pas
          a=1
      else:
          x=row.split(',')         #on crée 3 listes, une par colonne
          alpha.append(float(x[0]))
          Cd.append(float(x[1]))
          Cl.append(float(x[2]))


  degre = 10
  polynome1=np.polyfit(alpha, Cd, degre) #polynome obtenu avec la regression polynomiale de numpy
  polynome2=np.polyfit(alpha, Cl, degre) #polynome obtenu avec la regression polynomiale de numpy
  Y1=[]
  Y2=[]
  X=[]
  x=-15
  n=len(alpha)
  step=35/n

  for k in range(0,n):
    y1=0
    y2=0
    for i in range(0,degre+1):       #calcul de la valeur de cl ou cd avec les regression
      y1=y1+polynome1[i]*x**(degre-i)
      y2=y2+polynome2[i]*x**(degre-i)
    Y1.append(y1)                    #création des listes de cd ou cl pour les tracer avec matplotlib
    Y2.append(y2)
    X.append(x)                      #création de la liste des abscisses
    x=x+step

  return(Y1,Y2,X)

def finesse(file, nb):
  file.seek(0)                       #remet la lecture des documents a la ligen 0
  Cd,Cl,alpha=Valeur(file, nb)
  f=[]
  for k in range(0,len(Cd)):
    f.append(Cl[k]/Cd[k])            #création de la liste du module de finesse

  n=len(alpha)
  max=0
  pos=5
  for k in range(5,len(f)):          #on ne prend pas en compte les premieres valeurs (car les regressions sont moches en ces points)
    if max<f[k]:
      max=f[k]                       #pour la valeur amax de f, on note la valeur de alpha
      pos=k

  return((pos*35/n)-15)

def dFlfct(r,dr,rho,omega,alpha,file):
  file.seek(0)
  Alpha=[]
  Cl=[]
  dS=rayon*dr                      #élément de surface de dS (pale rectangulaire)

  a=0
  for row in file:
      if a==0:
        a=1
      else:
        x=row.split(',')
        Alpha.append(float(x[0]))
        Cl.append(float(x[2]))

  degre=10
  polynome=np.polyfit(Alpha, Cl, degre)
  Cl=0
  for k in range(0,degre+1):
    Cl=Cl+alpha**(degre-k)*polynome[k]    #on determine cl en alpha
  return((1/2)*rho*((u**2)+(omega*r)**2)*dS*Cl)  #on calcule la valeur de la force en r sur la surface dS



def dFdfct(r,dr,rho,omega,alpha,file):
  file.seek(0)
  Alpha=[]
  Cd=[]
  dS=rayon*dr

  a=0
  for row in file:
      if a==0:
        a=1
      else:
        x=row.split(',')
        Alpha.append(float(x[0]))
        Cd.append(float(x[1]))

  degre=10
  polynome=np.polyfit(Alpha, Cd, degre)
  Cd=0
  for k in range(0,degre+1):
    Cd=Cd+alpha**(degre-k)*polynome[k]    #on determien cd en alpha
  return(((1/2)*rho*(u**2+(omega*r)**2)*dS*Cd))  #on calcule la valeur de la force en r sur la surface dS




def dCfct(r,dFl,dFd,beta): #alpha = beta car phi = 0
  return(r*(dFl*np.cos(beta) + dFd*np.sin(beta)))   #force projeté sur les axes er et eteta



def Cfct(r, file, nb):
  C=0
  precision=1000   #on définit la précision de notre méthode d'intégration numérique
  step=r/precision
  alpha = finesse(file, nb)
  alpha = alpha*2*np.pi/360   #on met alpha en radiant
  for k in range(0,precision + 1):
    dFl = dFlfct(k*step,step,rho,omega,alpha,file)
    dFd = dFdfct(k*step,step,rho,omega,alpha,file)
    C = C + dCfct(k*step,dFl,dFd,alpha)  #on somme les valeurs de dC sur toute la longueur de la pale pour obtenir le couple total
  return(C)



def puissance(C,omega):
  return(C*omega)    #calcul de la puissance


Puissance1 = 0
Puissance2 = 0
Puissance3 = 0
for k in range(len(V)):
  u = V[k]
  Puissance1 = Puissance1 + puissance(Cfct(r, file1, 1), omega)
  Puissance2 = Puissance2 + puissance(Cfct(r, file2, 2), omega)
  Puissance3 = Puissance3 + puissance(Cfct(r, file3, 3), omega)

print('Puissance =', (Puissance1+Puissance2+Puissance3)/3/1000000, 'MW')


