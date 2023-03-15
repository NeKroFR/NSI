#Exercice 1:

def convertir(tab):
    n = len(tab)
    s = 0
    for i in range(n):
        s = s + tab[i]*2**(n-i-1)
    return s
        


#Exercice 2:

liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        j = i
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j - 1
        tab[j] = valeur_insertion