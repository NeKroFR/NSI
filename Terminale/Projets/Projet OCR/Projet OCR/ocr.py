from images import *


def pré_traitement(matrice,seuil):
    """
    Fonction qui transforme une images en niveaux de gris en une image en noir et blanc.
    ---
    IN:
        la matrice d'une image en niveau de gris, le seuil(int)
    OUT:
        la matrice d'une image en niveau de noir
    """
    m = []
    for l in matrice:
        a = []
        for i in l:
            if i < seuil:
                a.append(0)
            else:
                a.append(255)
        m.append(a)    
    return m

def seuil(data: list)->int:
    """
    Fonction qui détermine le seuil d'une image
    ---
    IN:
        tableau de tableaux des valeurs de pixels d'une image
    OUT:
        un entier, valeur moyenne des pixels de l'image.
    """
    i = 0
    e = 0
    for l in data:
        for m in l:
            e += 1
            i += m
    return int(i/e)
    
def noir_blanc(data: list)->list:
    """
    Fonction qui renvoie un tableau de tableaux des valeurs modifiées des pixels pour une conversion en noir et blanc
    ---
    IN:
        le tableau de tableaux des valeurs des pixels d'une image
    OUT:
        tableau de tableaux des valeurs modifiées des pixels pour une conversion en noir et blanc
    """
    s = seuil(data)
    return pré_traitement(data,s)

def traitement(data1: list, data2: list)->list:
    """
    Fonction qui traite deux matrices
    ---
    IN:
        deux tableaux de tableaux : le premier correspondant à un caractère à identifier, le deuxième à un caractère témoin
    OUT:
        tableau de tableaux après les opérations logiques décrites au premier paragraphe
    """


test = get_data_from_image("1.png")
"""
print(test[0], test[5])
print(test[7][2])
print("lignes:",len(test[0]))
print("colonnes:",len(test))
"""
