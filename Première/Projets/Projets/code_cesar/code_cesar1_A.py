import doctest


def lettre(lettre, decal):
    """
    Docstring :
        Fonction qui chiffre une lettre en utilisant le "code césar".

    Pré-conditions :
        Une lettre au format "str"
        Une valeur de décalage au format "int"
    Post-conditions :
        La lettre chiffré au format "str"

    Tests unitaires :
    >>> lettre("!", 2)
    "!"
    >>> caesar("Z", 6)
    "F"
    >>> caesar("a", 3)
    "d"
    """
    pass

def caesar(phrase, decal):
    """
    Docstring :
        Fonction qui chiffre une phrase en utilisant le "code césar".

    Pré-conditions :
        Une phrase au format "str"
        Une valeur de décalage au format "int"
    Post-conditions :
        Le message chiffré au format "str"

    Tests unitaires :
    >>> caesar("Hello World !", 2)
    'Jgnnq Yqtnf !'
    >>> caesar("ZazA", 6)
    "FgfG"
    """
    # corps de la fonction
    pass


# Programme principal
doctest.testmod()	# exécution des test unitaires
