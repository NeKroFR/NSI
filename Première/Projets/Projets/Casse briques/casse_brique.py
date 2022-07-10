from tkinter import *
#######################
#      FONCTIONS      #
#######################
def efface():
    '''' effacement de tous les éléments du canevas'''
    can.delete('all')

def affiche():
    '''balaie la matrice et affiche les éléments dans le canevas'''
    for i in range(25):
        for j in range(40):
            if grille[i][j] == 1:
                can.create_rectangle(j*32, i*32, j*32+32, i*32+16, fill = '#925af9')
            elif grille[i][j] == 2:
                can.create_oval(j*32, i*32, j*32+32, i*32+32, fill='#ffb8f6' )
            elif grille[i][j] == 3:
                can.create_image(j*32,i*32, image = brique, anchor ='nw')

def anim():
    '''
    BOUCLE D'ANIMATION PRINCIPALE
    '''
    efface()
    affiche()
    balle()
    WINorLOOSE()
    fen.after(1, anim)

def gauche(event):
    '''
    Procédure éxécutée lors de l'appui sur la touche 'fleche gauche'
    '''
    if grille[24][0] == 1:
        return False
    #décale toutes les valeurs de grille[24] vers la gauche
    right = grille[24][1::]
    left = grille[24][:1:]
    modif = right+left 
    grille[24] = modif

def droite(event):
    '''
    Procédure éxécutée lors de l'appui sur la touche 'fleche droite'
    '''
    if grille[24][39] == 1:
        return False
    #décale toutes les valeurs de grille[24] vers la droite
    right = grille[24][-1::]
    left = grille[24][:-1:]
    modif = right + left 
    grille[24] = modif

def WINorLOOSE():
    """
    Fonction qui gère la victoire ou la defaite et change ainsi l'affichage
    """
    #si l'on perd
    if 2 in grille[24]:
        text = Label(fen, text="Game Over!", font=("Courrier", 16), bg="#B0FFDB", fg="black")
        text.pack(expand=YES)
    #si on gagne
    if not 3 in grille[0]:
        text = Label(fen, text="You Win!", font=("Courrier", 16), bg="#B0FFDB", fg="black")
        text.pack(expand=YES)

def balle():
    """
    fonction qui gère le déplacement de la balle
    """
    global balleY,balleUP,balleDROITE,balleX, score
    #si la balle est sur la raquette
    if grille[balleY+1][balleX] == 1:
        balleUP = True
    #si la balle est sous une brique ou contre un mur
    if 2 in grille[0]:#plafond
        balleUP = False
    elif grille[balleY-1][balleX]==3:#brique
        grille[balleY-1][balleX]= 0
        score +=1
        balleUP = False
    if balleX == 0 or balleX == 39:#mur côté
        balleDROITE = not balleDROITE
    grille[balleY][balleX]=0

    #déplacement balle axe Y
    if balleUP:
        balleY -= 1
    else:    
        balleY +=1
    #déplacement balle axe X
    if balleDROITE:
        balleX += 1
    else:
        balleX -= 1
    grille[balleY][balleX]=2

def diff():
    """
    fonction qui détermine la difficultée
    """
    print("1) Easy\n2) Medium\n3) Hard\n4) Hell")
    a = int(input("Choisissez une difficulté:"))
    if a == 1:
        return [5,35]
    if a == 2:
        return [10,30]
    if a == 3:
        return [10,24]
    if a == 4:
        return [10,24]
    else:
        print("Vous devez chosir un chiffre compris entre 1 et 4")
        exit()
#######################
# PROGRAMME PRINCIPAL #
#######################
"""création de la grille"""
dif = diff()
score = 0
grille = [[3 for i in range(40)] for j in range(5)]
grille += [[0 for i in range(40)] for j in range(19)]
#création de la raquette+ ajout de la raquette dans la grille
raquette = [[0 for i in range(40)]]
for i in range(dif[0],dif[1]):
    raquette[0][i] = 1
grille += raquette
#création de la balle
grille[23][20] = 2
balleX = 20
balleY = 23
balleUP = True
balleDROITE = True


##############################
# FIN DU PROGRAMME PRINCIPAL #
##############################


fen = Tk()
fen.title('Casse-briques')
can = Canvas(fen, width = 1280, height = 800, background='#bae6ff')
brique = BitmapImage(file ='brique.xbm', foreground='#e400ff')
can.pack()
fen.bind("<Left>", gauche)
fen.bind("<Right>", droite)

anim()

fen.mainloop()