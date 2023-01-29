def recherche_occurrence(liste, valeur):
    occurences = 0
    for element in liste:
        if element == valeur:
            occurences += 1
    return occurences


def extreme_moyenne(liste):
    minimum = max(liste)
    maximum = min(liste)
    somme = 0
    for element in liste:
        somme += element
    moyenne = somme / len(liste)
    return (minimum, maximum, moyenne)




T = [2,3,5,8,9,4,5,0]

print(recherche_occurrence(T,10))
print(recherche_occurrence(T,5))
print(extreme_moyenne(T))