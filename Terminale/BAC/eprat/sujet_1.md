# Sujet1



## EXERCICE 1 (4 points)

Programmer la fonction verifie qui prend en paramètre un tableau de valeurs
numériques non vide et qui renvoie True si ce tableau est trié dans l’ordre croissant,
False sinon.

Exemples :
```>>> verifie([0, 5, 8, 8, 9])
True
>>> verifie([8, 12, 4])
False
>>> verifie([-1, 4])
True
>>> verifie([5])
True
```

## EXERCICE 2 (4 points)
Les résultats d'un vote ayant trois issues possibles 'A', 'B' et 'C' sont stockés dans un
tableau.
Exemple :

```Urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']```

La fonction depouille doit permettre de compter le nombre de votes exprimés pour
chacune des issues. Elle prend en paramètre un tableau et renvoie le résultat dans un
dictionnaire dont les clés sont les noms des issues et les valeurs le nombre de votes en
leur faveur.
La fonction vainqueur doit désigner le nom du ou des gagnants. Elle prend en
paramètre un dictionnaire dont la structure est celle du dictionnaire renvoyé par la
fonction depouille et renvoie un tableau. Ce tableau peut donc contenir plusieurs
éléments s’il y a des ex-aequo.
Compléter les fonctions depouille et vainqueur fournies à la page suivante pour
qu’elles renvoient les résultats attendus.

```py
urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = ...
    for bulletin in urne:
        if ...:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            ...
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if ... > ... :
            nmax = ...
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == ...]
    return ...
```    

```
Exemples d’utilisation :
>>> election = depouille(urne)
>>> election
{'B': 4, 'A': 3, 'C': 3}
>>> vainqueur(election)
['B']
```
[Correction](correction_sujet_1.py)