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
    '!'
    >>> caesar("Z", 6)
    'F'
    >>> caesar("a", 3)
    'd'
    """
    x = ord(lettre)
    # on vérifie si la lettre est une majuscule, puis on applique le décallage
    if x > 64 and x < 91:
        x += decal
        if x > 90:
            x -= 26
    # on vérifie si la lettre est une minuscule, puis on applique le décallage
    elif x > 96 and x < 123:
        x += decal
        if x > 122:
            x -= 26
    # si le charactère n'est pas une lettre on ne fait rien
    return chr(x)

def caesar(msg, key):
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
    'FgfG'
    """
    message = ''
    for i in msg: 
        x = lettre(i, key)
        message = message + x
    return message

fichier = input("Entrez le fichier contenant la phrase à déchiffrer: ")
clean = open(fichier,"r").read()

for i in range(1, 27):
    print("pas: ",i," message: ",caesar(clean,i))

"""
TRAVAIL SUPLEMENTAIRE: détectiojn du mot  "le"
"""
for i in range(1, 27):
    if " le " in caesar(clean,i):
        print("pas: ",i," message: ",caesar(clean,i))