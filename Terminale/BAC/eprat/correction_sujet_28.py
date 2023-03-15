#Exercice 1:

def moyenne(tab):
    s = 0
    for v in tab :
        s = s + v
    return s/len(tab)


assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5

#Exercice 2:

def dichotomie(tab, x):
    if len(tab) == 0:
        return False, 1
    if (x < tab[0]) or (x > tab[len(tab)-1]):
        return False, 2
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3
