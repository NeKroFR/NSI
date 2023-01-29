def recherche_dichotomique(liste, cible):
    gauche, droite = 0, len(liste) - 1
    while gauche <= droite:
        milieu = gauche + (droite - gauche) // 2
        if liste[milieu] == cible:
            return milieu
        elif liste[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return None


T = [0, 4, 4, 5, 5, 6, 6, 23, 87]

print(recherche_dichotomique(T,1))
print(recherche_dichotomique(T,23))