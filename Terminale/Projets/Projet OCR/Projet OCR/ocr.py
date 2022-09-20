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
    identifier = noir_blanc(data1)
    temoin = noir_blanc(data2)
    T= []
    for i in range(len(identifier)):
        a = []
        for u in range(len(identifier[i])):
            x = identifier[i][u] ^ temoin[i][u]
            a.append(x & temoin[i][u])
        T.append(a)
    return T


def ocr(lettre: list)->str:
    '''Reconnaissance d'une lettre manuscrite par comparaison avec les lettres témoins de l'alphabet.
    ENTREEE :
        lettre : tableau des pixels de la lettre manuscrite
    SORTIE :
        lettre_identifiee : le caractère ( str ) identifié.
    '''
    dico = {} 
    lettre = noir_blanc(get_data_from_image(lettre))
    alphabet = [chr(i) for i in range(65,91)]
    for temoin in alphabet:
        lettre_temoin = noir_blanc(get_data_from_image(temoin + '.png')) # récupération du tableau des pixels du caractère témoin correspondant à 'temoin'
        resultat = traitement(lettre, lettre_temoin) # opérations logiques entre les pixels des deux caractères
        # calcul du pourcentage de pixels blancs ayant disparu après traitement
        i = 0
        e = 0
        for l in resultat:
            for m in l:
                e += 1
                if m == 0:
                    i += 1
        a  = i/e*100
        # placement de ce pourcentage dans le dictionnaire comme valeur associée à la lettre courante
        dico[temoin] = a
    
    # recherche du maximum dans les valeurs du dictionnaire
    lettre_identifiee = max(dico, key=dico.get)
    # renvoi du caractère identifié
    return lettre_identifiee			

			
    

test = noir_blanc(get_data_from_image("1.png"))
v = noir_blanc(get_data_from_image("V.png"))
#print(test)
#print(v)
a = traitement(test, v)
save_image_from_data("test.png", a)

for i in range(1,9):
    print(ocr(str(i)+".png"), end="")
print()
"""
print(test[0], test[5])
print(test[7][2])
print("lignes:",len(test[0]))
print("colonnes:",len(test))
"""
