#Exercice 1:

def recherche_min(tab):
    indice_mini = 0
    mini = tab[0]
    for i in range(1, len(tab)):
        if tab[i] < mini:
            indice_mini = i
            mini = tab[i]
    return indice_mini

#Exercice 2:

def separe(tab):
    gauche = 0
    droite = len(tab) - 1
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche = gauche + 1
        else :
            tab[gauche], tab[droite] = tab[droite], tab[gauche]
            droite = droite - 1
    return tab