#Exercice 1:

def recherche(tab,n):
    indice = len(tab)
    i = 0
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i
    return indice
    










#Exercice 2:

from math import sqrt

def distance(point1, point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def plus_courte_distance(tab, depart):
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist :
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point