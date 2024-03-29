#Exercice 1:

def tri_selection(tab):
    n = len(tab)
    for i in range(n-1):
        min_i = i
        for j in range(i+1, n):
            if tab[j] < tab[min_i]:
                min_i = j
        tab[i], tab[min_i] = tab[min_i], tab[i]
    return tab

#Exercice 2:

from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre etait ", nb_mystere)