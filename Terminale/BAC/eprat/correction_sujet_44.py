#Exercice 1:

def renverse(mot):
    chaine = ''
    for c in mot:
        chaine = c + chaine
    return chaine

#Exercice 2:

def crible(n):
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(2, n):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2 * i, n, i):
                tab[multiple] = False
    return premiers


assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]