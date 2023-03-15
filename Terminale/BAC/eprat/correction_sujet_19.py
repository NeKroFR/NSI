#Exercice 1:

def recherche (tab, n):
    deb = 0
    fin = len(tab)-1
    indice = -1
    while deb <= fin and indice == -1:
        mil = (deb+fin)//2
        if tab[mil] == n:
            indice = mil
        elif n > tab[mil]:
            deb = mil + 1
        else :
            fin = mil - 1
    return indice



#Exercice 2:

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def position_alphabet(lettre):
    return ord(lettre) - ord('A')
def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat

