#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import doctest
import random
import os

# <INSTRUCTIONS>
# 1) compléter les fonctions
# 2) le corps principal du programme est fait en bas de fichier : étudier son fonctionnement et le corriger si besoin
# Remarque : ce fichier correspond à la première étape à faire quand on veut réaliser un programme
# </INSTRUCTIONS>

def lecture_fichier (nom_fichier) :
    """
    lit les mots contenus dans le fichier nom_fichier,
    choix alétoire d'un mot qui est renvoyé

    Pré-conditions :
    *) nom_fichier est le nom du fichier contenant les mots pour le jeu
    Post-conditions :
    *) le mot choisi aléatoirement dans le fichier

    Tests unitaires :
    >>> lecture_fichier("pendu_mots_test_unitaire.txt")
    "toto"

    Remarques :
    *) pour écrire cette fonction, il faut apprendre à utiliser les fichiers 
       (nsivaugelas.free.fr, rubriques Outils, page d'aide sur l'utilisation des fichiers)
    *) string.strip('') enlève le caractère \n correspondant à un retour à la ligne dans le fichier

    """
    word = random.choice(open(nom_fichier,"r").readlines()).strip('\n')
    return word 


def affiche_mot_a_deviner (mot, lettres) :
    """
    cette fonction renvoie le mot à deviner en version codée
    si on doit trouver 'travail' et qu'on a déjà testé la lettre 'a': renvoie '--a-a--'

    Pré-conditions :
    *) mot est le mot à trouver (non codé par des tirets -)
    *) lettres est une chaîne de caractères contenant les lettres déjà testées
    Post-conditions :
    *) renvoie le mot codé par des tirets et les lettres contenues dans la string lettres

    Tests unitaires :
    >>> affiche_mot_a_deviner ('travail', '')
    "-------"
    >>> affiche_mot_a_deviner ('travail', 'a')
    "--a-a--"
    >>> affiche_mot_a_deviner ('travail', 'va')
    "--ava--"
    >>> affiche_mot_a_deviner ('travail', 'travail')
    "travail"

    """
    chiffré = ''
    for i in mot:
        if i in lettres:
            chiffré += i
        else:
            chiffré += '-'
    return chiffré



def choix_lettre_par_joueur () :
    """
    affiche un message invitant le joueur à taper une lettre au clavier qui sera renvoyée
    si le joueur tape plusieurs lettres, on ne prend que la première

    Pré-conditions :
    *) aucune
    Post-conditions :
    *) renvoie la lettre choisi au clavier par le joueur

    Tests unitaires : on ne peut pas les faire dans ce cas
    """
    while True:
        char = input('Choisissez une lettre: ')
        if char not in 'azertyuiopqsdfghjklmwxcvbnéèçàùAZERTYUIOPMLKJHGFDSQWXCVBN':
            print("Erreur! Vous devez choisir une lettre.")
        else:
            break
    return char[0]

def message_erreur_deja_jouer (lettres, lettre) :
    """
    affiche un message d'erreur si la lettre a déjà été jouée
    le message d'erreur doit contenir la lettre déjà jouée et la liste des autres lettres déjà jouées

    Pré-conditions :
    *) lettres est une chaine de caractres contenant les lettres déjà joueés
    *) lettre est la lettre jouée pendant ce tour du jeu
    Post-conditions :
    *) affiche le message d'erreur
    *) renvoie True si la lettre a déjà été jouée, sinon False

    Tests unitaires : 
    >>> message_erreur_deja_jouer ('aeiou', 'e')
    True
    >>> message_erreur_deja_jouer ('aeiou', 'f')
    False
    """
    if lettre in lettres:
        print("\nErreur! vous ne pouvez pas jouer la lettre '" + lettre + "' car vous l'avez déjà utilisée.\n\nLettres déjà jouées:\n-------------------\n"+lettres)
        return False
    else:
        return True
        
def nombre_de_tours_restants (n) :
    """
    affiche un message indiquant le nombre de tours restants

    Pré-conditions :
    *) entier n correspondant au nombre de tours restants
    Post-conditions :
    *) affiche le message
    *) renvoie True si le joueur peut continuer à jouer, False sinon

    Tests unitaires : 
    >>> nombre_de_tours_restants (2)
    True
    >>> nombre_de_tours_restants (0)
    False
    >>> nombre_de_tours_restants (-1)
    False
    """
    print(" ____________________\n/ Vies restantes: "+ str(n) + " /\n____________________\n")
    if n < 1:
        return False
    else:
        return True

# Programme principal
doctest.testmod()	# exécution des test unitaires
os.system("clear")
mot_choisi = lecture_fichier ("pendu_mots.txt")
nb_tours = len(set(mot_choisi)) + 3
lettres_deja_jouees = ""
while nombre_de_tours_restants (nb_tours) :
    os.system("clear")
    nombre_de_tours_restants(nb_tours)
    print(affiche_mot_a_deviner(mot_choisi, lettres_deja_jouees))
    lettre = choix_lettre_par_joueur()
    print(lettre)
    if not lettre in mot_choisi:
        nb_tours -= 1
    if not  message_erreur_deja_jouer(lettres_deja_jouees, lettre):
        input()
    else:
        lettres_deja_jouees += lettre
    if affiche_mot_a_deviner (mot_choisi, lettres_deja_jouees) == mot_choisi :
        break
    
os.system("clear")
if affiche_mot_a_deviner (mot_choisi, lettres_deja_jouees) == mot_choisi :
    print("Gagné, le mot était: "+ mot_choisi)
else :
    print("Perdu")



