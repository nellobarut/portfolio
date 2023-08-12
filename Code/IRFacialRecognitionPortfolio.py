#Module nécessaire pour le programme
import cv2                      #pour le traitement vidéo
import os                       #pour importer les fichiers
import matplotlib.pyplot as plt #pour tracer les courbes
import numpy as np              #FFT et opération sur les Matrice/liste
import csv                      #pour lire les fichiers CSV
from PIL import Image           #pour le traitements des images

##
def Data(): #importe tous les fichiers (photo,CSV et nom) des individus composants la base de donnée
    #création de listes pour les fichiers (DATA) et pour les noms (Name)
    DATA=[]
    Name=[]

    #ajoute tous les noms des individus de la base de donnée dans la liste Name en allant les chercher dans le repertoire de l'ordinateur
    for filename in os.listdir("C:/Users/Siena PAGE/Desktop/TIPE_BDD"):
        Name.append(filename)

    #ajoute une liste vide a DATA pour chaque nom dans Name
    for k in range(0,len(Name)):
        DATA.append([])

    #pour chaque nom dans Name créer le chemin pour accéder aux fichiers (photos et CSV)
    count1=0
    for i in Name:
        path="C:/Users/Siena PAGE/Desktop/TIPE_BDD"
        path=('/'.join(("C:/Users/Siena PAGE/Desktop/TIPE_BDD",'%s')) % i)

        #pour chaque individu compte les nombre de photos (et donc de CSV car ils vont par paire)
        count2=0
        for filename in os.listdir(path):
            type=filename.split('.')
            if type[1]=='jpg':
                count2=count2+1

        #crée une liste composée d'une photo et du fichier CSV correspondant puis l'ajoute a la Liste DATA dans la liste correspondant à celle de l'individu (dans l'ordre alphabétique)
        #repète l'opération jusqu'à avoir ajouter toutes les photos sauf la dernière qui servira de photo test
        for k in range(1,count2):   #count2 et non count2+1 car on ne veut pas de la dernière dans la BDD puisque cest celle quon va comparer
            print(k)
            PhotoCsv=[]
            PhotoCsv.append(Image.open('/'.join((path, ''.join(('%s','%d.jpg')) % (i,k)))))
            PhotoCsv.append(open('/'.join((path, ''.join(('%s','%d.csv')) % (i,k)))))
            DATA[count1].append(PhotoCsv)

        #ajoute finalement le nom de l'individu pour pouvoir le citer en cas de reconnaissance par le programme
        DATA[count1].append(Name[count1])
        count1=count1+1
    return(DATA)

#-------------------------------------------------------------------------------
def Test(): #création de la liste des photos qu'on compare à la base de données

    #meme principe que la fonction DATA mais on ne garde que la dernière photo de chaque individu (ici la 5eme ou la 6eme pour certains
    Test=[]
    Name=[]

    for filename in os.listdir("C:/Users/Siena PAGE/Desktop/TIPE_BDD"):
        Name.append(filename)

    for k in range(0,len(Name)):
        Test.append([])

    count1=0
    for i in Name:
        path="C:/Users/Siena PAGE/Desktop/TIPE_BDD"
        path=('/'.join(("C:/Users/Siena PAGE/Desktop/TIPE_BDD",'%s')) % i)

        count2=0
        for filename in os.listdir(path):
            type=filename.split('.')
            if type[1]=='jpg':
                count2=count2+1

        PhotoCsv=[]
        PhotoCsv.append(Image.open('/'.join((path, ''.join(('%s','%d.jpg')) % (i,count2)))))
        PhotoCsv.append(open('/'.join((path, ''.join(('%s','%d.csv')) % (i,count2)))))
        Test[count1].append(PhotoCsv)

        Test[count1].append(Name[count1])
        count1=count1+1
    return(Test)

#-------------------------------------------------------------------------------
def Taille(ImageColor): #recadre la photo pour que l'individu soit centré et rogne les bords pour ne concerver que son visage (le fond ne nous interesse pas)

    #LES PHOTOS FONT 320 APAR 240 AVANT TRAITEMENTS

    r=90     #valeur de ref r=90
    g=140    #valeur de ref g=140
    b=80     #valeur de ref b=80


    #on cherche a situer l'individu par au centre (selon l'horizontal) et pour cela on balaye l'écran de haut en bas à différentes valeurs de x
    ky=130 #valeur de départ pour déterminer si l'individu se situe par rapport au centre (160)
    YHaut=[]
    YBas=[]
    for m in range(0,13,5): #boucle de 12 de long allant de 5 en 5 (donc balaye 60 pour aller de 130 à 190)
        yh=0
        yb=0
        for j in range(0,240): #d'abord de haut en bas
            if ImageColor.getpixel((ky+m,j))[0]>r and ImageColor.getpixel((ky+m,j))[1]<g and ImageColor.getpixel((ky+m,j))[2]<b: #on cherche le premier pixel assez "rouge", pour cela on compare les valeurs RGB des pixels a des valeurs de référence obtenu empiriquement
                if yh==0:
                    yh=j
        YHaut.append(yh)
        h=240
        for i in range(0,240): #puis de bas en haut
            h=h-1
            if ImageColor.getpixel((ky+m,h))[0]>r and ImageColor.getpixel((ky+m,h))[1]<g and ImageColor.getpixel((ky+m,h))[2]<b: #meme methode de recherche du "rouge" =(chaud)
                if yb==0:
                    yb=h
        YBas.append(yb)

    #on garde seulement la valeur la plus basse de Yhaut et la plus haute de Ybas
    yh=YHaut[0]
    yb=YBas[0]
    for i in range(1,len(YHaut)):
        if yh>YHaut[i]:
            yh=YHaut[i]
        if yb<YBas[i]:
            yb=YBas[i]

    #on s'assure que la distance yb-yh soit paire car on souhaite prendre la moitie ensuite
    if (yb-yh)%2==1:
        yb=yb+1


    #meme principe qu'avant mais le centrage verticale cette fois
    kx=90 #le centre de la photo est a y=120
    Xdroite=[]
    Xgauche=[]
    for m in range(0,13,5):
        xd=0
        xg=0
        for j in range(0,320):
            if ImageColor.getpixel((j,kx+m))[0]>r and ImageColor.getpixel((j,kx+m))[1]<g and ImageColor.getpixel((j,kx+m))[2]<b:
                if xg==0:
                    xg=j
        Xgauche.append(xg)
        h=290               #pour eviter l'echelle de temperature on se décale sur la gauche
        for i in range(0,290):
            h=h-1
            if ImageColor.getpixel((h,kx+m))[0]>r and ImageColor.getpixel((h,kx+m))[1]<g and ImageColor.getpixel((h,kx+m))[2]<b:
                if xd==0:
                    xd=h
        Xdroite.append(xd)

    xd=Xgauche[0]
    xg=Xdroite[0]
    for i in range(1,len(Xdroite)):
        if xd>Xgauche[i]:
            xd=Xgauche[i]
        if xg<Xdroite[i]:
            xg=Xdroite[i]

    if (xd-xg)%2==1:
        xd=xd+1

    #on calcule la position verticale pour lequel l'individu est centré
    centre=160-(xg+(xd-xg)//2)
    return(yh,yb,centre)

#-------------------------------------------------------------------------------
def crop(Image): #on recadre la photo avec les valeurs obtenues avec la fonction Taille
    yh,yb,decalage=Taille(Image)
    box=(160-decalage-(yb-yh)//2,yh,160-decalage+(yb-yh)//2,yb) #la fonction crop prend en arguments 4 postions correspondant a la valeur la plus a gauche, la plus haute, la plus a droite et la plus basse puis conserve le rectangle formé
    ImageCropped=Image.crop(box)
    return(ImageCropped)

#-------------------------------------------------------------------------------
def Fourier(Tableau):   #faire le cas ou y a des entiers au debut
    #crée une matrice rectangulaire avec la valeur de la température de chaque pixel de la photo initiale en lisant le hichier csv
    #plusieurs problèmes:
    #le séparateur partie entière/partie réelle est le point virgule (;) donc il aut le remplacer par un point (.)
    #les valeurs dans le fichier CSV sont des strings (chaines de caracteres), il faut les transformer en nombres réels (float)
    #Pour une raison inconnue lorsqu'on importe un fichier CSV sur python la partie entièrs et la partie réelle d'un meme nombre ne sont pas dans la meme case
    #on se retrouve donc avec plusieurs situations particulières en fonction de la valeur de la case (entier ou flottant, debut et fin du tableau)
    #je sais pas si ca a un interet que je documente point par point cette fonction car elle n'éxiste que parce que le CSV ne s'importe pas "correctement"
    #print(Tableau)

    T=[]
    a=0
    for row in Tableau:
        #print(a)
        a=a+1
        F=[]
        if len(row[0].split(';'))==1:
            PartieEntiereRelou=row[0]
        else:
            for k in range(0,len(row[0].split(';'))-1):
                F.append(float(row[0].split(';')[k]))
        PartieFractionnaireRelou=(row[1].split(';'))[0]
        F.append(float('.'.join((PartieEntiereRelou,PartieFractionnaireRelou))))
        k=0
        while len(F)<320-len(row[-1].split(';')):
            k=k+1
            PartieEntiereEntier=[]
            if len(row[k].split(';'))==2:
                PartieEntiere=(row[k].split(';'))[1]
            else:
                PartieEntiere=(row[k].split(';'))[-1]
                entier=0
                while len(row[k].split(';'))-entier>2:
                    entier=entier+1
                    PartieEntiereEntier.append((row[k].split(';'))[entier])

            PartieFractionnaire=(row[k+1].split(';'))[0]

            if len(PartieEntiereEntier)!=0:
                for i in range(0,len(PartieEntiereEntier)):
                    F.append(float(PartieEntiereEntier[i]))

            F.append(float('.'.join((PartieEntiere,PartieFractionnaire))))

        PartieEntiereRelou2=(row[-2].split(';'))[-1]
        if len(row[-1].split(';'))!=1:
            F.append(float('.'.join((PartieEntiereRelou2,row[-1].split(';')[0]))))
            for i in range(1,len(row[-1].split(';'))):
                F.append(float(row[-1].split(';')[i]))
        else:
            PartieFractionnaireRelou2=row[-1]
        F.append(float('.'.join((PartieEntiereRelou2,PartieFractionnaireRelou2))))
        T.append(F)


    #on se retrove finalement avec une matrice avec les températures (taille: 240x320)
    return(T)
#-------------------------------------------------------------------------------
def CSVcrop(T,Image): #réduit la taille du tableau des températures pour le transformer en une matrice carrée de meme dimension que l'image réduite

    #print(len(T))
    Tcrop=[]

    #comme ppur la réducion de la photo
    yh,yb,decalage=Taille(Image)
    box=(160-decalage-(yb-yh)//2,yh,160-decalage+(yb-yh)//2,yb)
    #print(box)

    for i in range(box[1],box[3]):
        TcropTempo=[]
        for k in range(box[0],box[2]):
            #print(i,k)
            TcropTempo.append(T[i][k])
        Tcrop.append(TcropTempo)
    return(Tcrop)

#-------------------------------------------------------------------------------
def Moyenne(Matrice): #soustrait la valeur moyenne de la température car on ne s'intéresse qu'aux variations

    somme=0 #variable correspodnant a la somme de toutes les valeurs de températures
    for i in range(0,len(Matrice)):
        for k in range(0,len(Matrice[i])):
            somme=somme+Matrice[i][k]

    #on divise la somme par le nombre de valeurs (nombre de coéfficients de la matrice)
    moy=somme/(len(Matrice)*len(Matrice[0]))

    #on soustrait a chaque valeur de la mateice la valeur moyenne
    for i in range(0,len(Matrice)):
        for k in range(0,len(Matrice[i])):
            Matrice[i][k]=Matrice[i][k]-moy

#-------------------------------------------------------------------------------
def MoyenneFFT(Liste): #creer une Matrice avec les valeurs moyennes des FFT d'un individu

    #création d'une Matrice de meme taille que les FFT avec des 0 partouts
    SommeFFT=[]
    for k in range(0,len(Liste[0])):
        SommeFFT.append([0])
        for i in range(0,len(Liste[0][0])-1):
            SommeFFT[k].append(0)

    #Somme chaque valeur de chaque FFT a la position correspondante dans la Matrice SommeFFT
    for k in range(0,len(Liste[0])):
        for i in range(0,len(Liste[0][0])):
            for j in range(0,len(Liste)):
                SommeFFT[k][i]=SommeFFT[k][i]+Liste[j][k][i]

    #divise chaque valeur de la Matrice SommeFFT par le nombre de Matrice FFT (pour obtenir la moyenne)
    for k in range(0,len(SommeFFT)):
        for i in range(0,len(SommeFFT[0])):
            SommeFFT[k][i]=SommeFFT[k][i]/len(Liste)
    return(SommeFFT)

#-------------------------------------------------------------------------------
def ReduceFFT(FFT): #Effectue une FFT a la Matrice temperature puis reduit la Matrice FFT a une matrice composée seulement des valeurs dans les angles (taille finale 10x10)

    #FFT a 2 dimensions (sur une matrice carrée)
    FFT=np.fft.fft2(FFT)

    #création d'une liste vide complétée par la suite par 4 matrices 5x5 correspondants aux valeurs dans les angles
    FFTreduce=[]

    #haut gauche
    FFT1=FFT[0:5]
    for k in range(0,len(FFT1)):
        FFTreduce.append((FFT[k])[:5])


    #haut droite
    FFT2=FFT[0:5]
    for k in range(0,len(FFT2)):
        FFTreduce[k]=np.concatenate((FFTreduce[k],FFT[k][len(FFT)-5:len(FFT)]))


    #bas gauche
    FFT3=FFT[len(FFT)-5:]
    for k in range(0,len(FFT3)):
        FFTreduce.append((FFT[k])[:5])


    #bas droite
    FFT4=FFT[len(FFT)-5:]
    for k in range(5,5+len(FFT4)):
        FFTreduce[k]=np.concatenate((FFTreduce[k],FFT[k][len(FFT)-5:len(FFT)]))

    #on transforme la liste de liste en array numpy pour appliquer la fonction abs qui prend le module de chaque coefficiant
    FFT=np.array(FFTreduce)
    FFT=abs(FFT)
    return(FFT)

#-------------------------------------------------------------------------------
def Comparaison(FFT1,FFT2): #2 méthodes de comparaison valeur par valeur
    #premiere méthode: comparaison selon un intervalle determiner en pourcentage de la valeur
    confiance1=0.3  #0.3
    taux1=0
    for k in range(0,min(len(FFT1),len(FFT2))):
        for i in range(0,min(len(FFT1[k]),len(FFT2[k]))):
            if (FFT1[i][k]*(1-confiance1))<(FFT2[i][k])<=(FFT1[i][k]*(1+confiance1)) or (FFT2[i][k]*(1-confiance1))<=(FFT1[i][k])<=(FFT2[i][k]*(1+confiance1)):
                taux1=taux1+1

    #deuxieme méthode: comparaison selon un intervalle de longueur fixe (2xconfiancec2) centré en la valeur
    confiance2=100 #100 (méthode pas utlisé car inéfficace)
    taux2=0
    for k in range(0,min(len(FFT1),len(FFT2))):
        for i in range(0,min(len(FFT1[k]),len(FFT2[k]))):
            if FFT1[i][k]-confiance2<FFT2[i][k]<FFT1[i][k]+confiance2 or FFT2[i][k]-confiance2<FFT1[i][k]<FFT2[i][k]+confiance2:
                taux2=taux2+1

    #on transfrome les valeurs en pourcentage
    taux1=(taux1*100)/(min(len(FFT1),len(FFT2))*min(len(FFT1[0]),len(FFT2[0])))
    taux2=(taux2*100)/(min(len(FFT1),len(FFT2))*min(len(FFT1[0]),len(FFT2[0])))
    return(taux1,taux2)

#-------------------------------------------------------------------------------
def Axes(FFT): #crée les listes utilisées comme axes des abscisses et des ordonnées
    #création de listes vides
    X=[]
    Y=[]
    XX=[]
    YY=[]

    #exemple: pour une matrice 4x4, on obtient XX=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
    #                                       et YY=[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
    count=0
    for row in FFT:
        count=count+1
        for k in range(0,len(row)):
            X.append(count)
            Y.append(k)
        XX=np.concatenate((XX,X))
        YY=np.concatenate((YY,Y))
        X=[]
        Y=[]
    return(XX,YY)

#-------------------------------------------------------------------------------
def graph(courbe): #trace chaque valeur de la Matrice (température ou FFT) en fonction de sa position dans la matrice (x,y)
    #projection 3D
    ax = plt.axes(projection='3d')

    #création des listes pour les axes des abscisses et des ordonnées
    x,y=Axes(courbe)
    ax.scatter(x, y, courbe, c='blue')

    #légende des axes, cadrillages et titre
    plt.xlabel('x - axe des abscisses ')
    plt.ylabel('y - axe des ordonnées')
    plt.grid()
    ax.set_title('FFT')
    plt.show()

#-------------------------------------------------------------------------------
def CréationListe(Image,Fichier): #compile l'enchainement des fonctions pour passer des fichiers bruts a la Matrice FFT
    Tableau=csv.reader(Fichier)
    ImageCropped=crop(Image)
    CSV=Fourier(Tableau)
    FFT=CSVcrop(CSV,Image)
    Moyenne(FFT)
    FFT=ReduceFFT(FFT)
    return(FFT)

#-------------------------------------------------------------------------------
def BaseDeDonnée(Photo): #crée une liste de matrice correspondant a la base de donnée de tous les individus de la liste Photo (Photo=Data()) en faisant la moyenne des FFT de chaque photo de chaque individu

    BDD=[]
    for k in range(0,len(Photo)):
        MoyenneK=[]
        for i in range(0,len(Photo[k])-1):
            MoyenneK.append(CréationListe(Photo[k][i][0],Photo[k][i][1])) #ajoute chaque FFT d'un individu dans la liste MoyenneK
        MoyenneK=MoyenneFFT(MoyenneK) #calcule la moyenne de toutes les FFT de moyenneK
        BDD.append([Photo[k][-1],MoyenneK]) #ajoute cette moyenne a la BDD pour chaque individu ainsi que son nom

    print('OK')
    return(BDD)

##
#compare chaque photo de la liste PhotoTest a la BDD puis affiche le résultat, c'est a dire la personne ressemblant le plus et le resultat qui etait le bon, ainsi que la personne qui est arrivé 2eme et leur pourcenatge de ressemblance relative
PhotoTest=Test()
Photo=Data()
BDD=BaseDeDonnée(Photo)

count=0
for i in range(0,len(PhotoTest)): #parcourt la liste PhotoTest
    TAUX=[]
    FFTtest=CréationListe(PhotoTest[i][0][0],PhotoTest[i][0][1]) #crée la FFT correspondant a la photo
    for k in range(0,len(BDD)):
        TAUX.append([Comparaison(BDD[k][1],FFTtest)[0],BDD[k][0]]) #pour chaque FFT dans la BDD calcule le taux de ressemblance
    ressemblance=0
    gagnant=0

    #conserve seulement le taux de ressemblance le plus élévé et le 2eme plus élévé
    for k in range(0,len(TAUX)):
        if TAUX[k][0]>=ressemblance:
            ressemblance=TAUX[k][0]
            gagnant=k

    difference=ressemblance
    for k in range(0,len(TAUX)):
        if k!=gagnant:
            if ressemblance-TAUX[k][0]<difference:
                difference=ressemblance-TAUX[k][0]
                posdiff=k

    #affiche le résultat
    print('Le gagnant est',TAUX[gagnant][1],'avec',TAUX[gagnant][0],'%')
    print('La photo etait celle de',PhotoTest[i][1])
    print('La difference avec le 2eme est de',difference,'%','( c est',TAUX[posdiff][1],')')
    if TAUX[gagnant][1]==PhotoTest[i][1]:
        print('CEST BON')
        count=count+1
    else:
        print('NON')
    print('')

print('le nombre de bonne reconnaissance =',count)
##
for k in range(0,5):
    PhotoTest=x[k][1]
    Photo=x[k][0]
    BDD=BaseDeDonnée(Photo)


    count=0
    for i in range(0,len(PhotoTest)): #parcourt la liste PhotoTest
        TAUX=[]
        FFTtest=CréationListe(PhotoTest[i][0][0],PhotoTest[i][0][1]) #crée la FFT correspondant a la photo
        for k in range(0,len(BDD)):
            TAUX.append([Comparaison(BDD[k][1],FFTtest)[0],BDD[k][0]]) #pour chaque FFT dans la BDD calcule le taux de ressemblance
        ressemblance=0
        gagnant=0

        #conserve seulement le taux de ressemblance le plus élévé et le 2eme plus élévé
        for k in range(0,len(TAUX)):
            if TAUX[k][0]>=ressemblance:
                ressemblance=TAUX[k][0]
                gagnant=k

        difference=ressemblance
        for k in range(0,len(TAUX)):
            if k!=gagnant:
                if ressemblance-TAUX[k][0]<difference:
                    difference=ressemblance-TAUX[k][0]
                    posdiff=k

        #affiche le résultat
        print('Le gagnant est',TAUX[gagnant][1],'avec',TAUX[gagnant][0],'%')
        print('La photo etait celle de',PhotoTest[i][1])
        print('La difference avec le 2eme est de',difference,'%','( c est',TAUX[posdiff][1],')')
        if TAUX[gagnant][1]==PhotoTest[i][1]:
            print('CEST BON')
            count=count+1
        else:
            print('NON')
        print('')

    print('le nombre de bonne reconnaissance =',count)
    print('')
    print('')
    print('')
    print('')
    print('')

##
Photo=[[[Image.open("Desktop/TIPE_BDD/Nello/Nello5.jpg"),open(r"C:\Users\Siena PAGE\Desktop/TIPE_BDD/Nello/Nello5.csv")],'Nello']]

FFTtest=CréationListe(Photo[0][0][0],Photo[0][0][1])
BDD=BaseDeDonnée(Data())

##
#print(len(BaseDeDonnée(Photo)))
TAUX=[]
for k in range(0,len(BDD)):
    TAUX.append([Comparaison(BDD[k][1],FFTtest)[0],BDD[k][0]])

print(TAUX)




##
##
##
def CSVManuel(Image): #cette fonction a pour objectif de créer un tableau avec la température correspondant a chaque pixel avec un traitement de l'image (en comparant la valeur RGB de chaque pixel a l'échelle des températures fournie avec la photo)

    #Image=Image.open("Desktop/TIPE_ems_Nell/Nello/nello5.jpg")
    #Tmax=33.3
    #Tmin=13.0
    #cela implique de connaitre la valeur de la température min et max de la photo (en la lisant nous meme)


    Tmax=33.3
    Tmin=13.0

    #on rogne l'image pour enlever le texte
    Image=Image.crop((15,25,Image.size[0],Image.size[1]-27))

    #on calcule la variation de température par pixel (supposée linéaire sur l'échelle) grace aux températures max et min et au nombre de pixels
    GradT=(Tmax-Tmin)/180

    #création de la Matrice température
    T=[]

    #valeur min et max en ordonnée et en abscisse a parcourir (on pourrait restreindre car les bords ne nous interessent)
    startx=0
    endx=Image.size[0]
    starty=0
    endy=Image.size[1]

    #la valeur RGB des pixels de l'échelle pour une meme ordonnée n'étant pas constant on calcule la moyenne
    #l'échelle des températures s'étend de y=5 a y=183 et fait 7 pixels de large (centrée en 295)
    echelle=[]
    for y in range(5,183):
        echelleK=[0,0,0]
        for x in range(292,298):
            for k in range(0,3):
                echelleK[k]=echelleK[k]+Image.getpixel((x,y))[k]
        for k in range(0,3):
            echelleK[k]=int(echelleK[k]//5)
        echelle.append(tuple(echelleK))

    #on crée une liste croix contenant la position de chaque pixel qui constitue le réticule au centre de la photo car la valeur RGB de ces pixels n'a pas de lien avec la température
    Croix=[]
    for k in range(130,140):
        for i in range(94,97):
            Croix.append((k,i))

    for k in range(151,160):
        for i in range(94,97):
            Croix.append((k,i))

    for k in range(144,147):
        for i in range(101,110):
            Croix.append((k,i))

    for k in range(144,147):
        for i in range(80,90):
            Croix.append((k,i))

    for k in range(142,149):
        for i in range(90,92):
            Croix.append((k,i))

    for k in range(142,149):
        for i in range(99,101):
            Croix.append((k,i))

    for k in range(149,151):
        for i in range(92,99):
            Croix.append((k,i))

    for k in range(140,142):
        for i in range(92,99):
            Croix.append((k,i))

    Croix.append((141,91))
    Croix.append((149,91))
    Croix.append((142,92))
    Croix.append((148,92))
    Croix.append((142,98))
    Croix.append((148,98))
    Croix.append((141,99))
    Croix.append((149,99))

    #calcule de la valeur de la température correspondant a chaque pixel
    for y in range(starty,endy):
        Tx=[] #liste des températures pour la lignes x
        for x in range(startx,endx):
            if (x,y) not in Croix: #on vérifie que le pixel n'est pas un de ceux composant la croix, dans ce cas on doit extrapoler et donc on ajoute la valeur de température du pixel précédent (voir le else suivant)
                value=True
                value2=True
                f=0
                while value2:
                    f=f+10
                    for i in range(0,178): #on compare ensuite une par une les valeurs RGB du pixel a chaque valeur RGB des pixels de l'échelle de température jusqu'à trouver celui qui correspond le mieux (les valeurs RGB sont en 8 bits chacune donc il y a plus de 16 millions de possibilités alors que l'échelle ne fait que 180 pixels, il y a donc un facteur de précision f, il augmente de 10 si le pixel ne correspond à aucun de ceux présents dans l'échelle jusuq'à ce qu'il y ai un résultat positif
                        if (echelle[i][0]-f)<Image.getpixel((x,y))[0]<(echelle[i][0]+f) and (echelle[i][1]-f)<Image.getpixel((x,y))[1]<(echelle[i][1]+f) and (echelle[i][2]-f)<Image.getpixel((x,y))[2]<(echelle[i][2]+f) and value:
                            Tx.append(Tmin+(180-i)*GradT) #on ajoute la valeur de la température calculé grace a sa position selon y (i dans la boucle)
                            Image.putpixel((x,y),echelle[i])
                            value=False
                            value2=False
            else:
                Tx.append(Tx[-1])
                Image.putpixel((x,y),Image.getpixel((x-1,y)))

        T.append(Tx)
    return(T)

##
def DataALL():
    DATA_ALL=[]
    for m in range(0,5):
        DATA_ALL.append([[],[]])

        Name=[]
        for filename in os.listdir("C:/Users/Siena PAGE/Desktop/TIPE_BDD"):
            Name.append(filename)

        for k in range(0,len(Name)):
            DATA_ALL[m][0].append([])
            DATA_ALL[m][1].append([])

        count1=0
        for i in Name:
            path="C:/Users/Siena PAGE/Desktop/TIPE_BDD"
            path=('/'.join(("C:/Users/Siena PAGE/Desktop/TIPE_BDD",'%s')) % i)

            count2=0
            for filename in os.listdir(path):
                type=filename.split('.')
                if type[1]=='jpg':
                    count2=count2+1

            for k in range(1,count2+1):
                PhotoCsv=[]
                PhotoCsv.append(Image.open('/'.join((path, ''.join(('%s','%d.jpg')) % (i,k)))))
                PhotoCsv.append(open('/'.join((path, ''.join(('%s','%d.csv')) % (i,k)))))
                if k-1!=m:
                    DATA_ALL[m][0][count1].append(PhotoCsv)
                else:
                    DATA_ALL[m][1][count1].append(PhotoCsv)

            DATA_ALL[m][0][count1].append(Name[count1])
            DATA_ALL[m][1][count1].append(Name[count1])
            count1=count1+1


    return(DATA_ALL)

x=DataALL()


##
for k in range(0,3):
    d={}
    d['%d' % k]=[]
    print(d)
    print(type(d))


##
Data()




