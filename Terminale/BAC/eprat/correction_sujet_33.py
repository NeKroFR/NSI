#Exercice 1:

def taille(arbre, lettre):
    if lettre == '':
        return 0
    return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])


#Exercice 2:

def tri_selection(tab):
    N = len(tab)
    for k in range(N-1):
        imin = k
        for i in range(k+1 , N):
            if tab[i] < tab[imin] :
                imin = i
        tab[k] , tab[imin] = tab[imin] , tab[k]
