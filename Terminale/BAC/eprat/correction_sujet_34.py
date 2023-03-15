#Exercice 1:

def moyenne(tab):
    assert len(tab) != 0, "aucune note"
    s = 0
    for v in tab :
        s = s + v
    return s/len(tab)



#Exercice 2:

def tri(tab):
    i= 0
    j= len(tab) - 1
    while i != j :
        if tab[i] == 0:
            i= i + 1
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j= j - 1
    return tab