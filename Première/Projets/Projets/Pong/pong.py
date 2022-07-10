from tkinter import *

def efface():

    '''' effacement complet du canevas'''

    can.delete('all')

def affiche():
    '''affichage à la position [ligne][colonne]'''
    for i in range(25):
        for j in range(40):
            if grille[i][j] == 1:
                can.create_rectangle(j*32, i*32, j*32+32, i*32+16, fill = 'blue')
            elif grille[i][j] == 2:
                can.create_oval(j*32, i*32, j*32+32, i*32+32, fill='red' )


#######################
# PROGRAMME PRINCIPAL #
#######################

"""création de la grille"""
grille = [[0 for i in range(40)] for j in range(25)]
grille[12][2] = 2
balleX = 2
balleY = 12
balleUP = True
balleDROITE = True

def anim():
    '''
        BOUCLE D'ANIMATION PRINCIPALE
    '''
    efface()
    affiche()
    fen.after(30, anim)



def haut(event):
    '''
        Procédure éxécutée lors de l'appui sur la flèche ↥
    '''




def bas(event):
    '''
        Procédure éxécutée lors de l'appui sur la touche ↧
    '''





##############################
# FIN DU PROGRAMME PRINCIPAL #
##############################
fen = Tk()
fen.title('Pong')


can = Canvas(fen, width = 1280, height = 800, background='black')
can.pack()

fen.bind("<Up>", haut)
fen.bind("<Down>", bas)

anim()

fen.mainloop()