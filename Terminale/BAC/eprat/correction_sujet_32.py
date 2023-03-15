#Exercice 1:

def min_et_max(tab):
    mini = tab[0]
    maxi = tab[0]
    for v in tab:
        if v > maxi:
            maxi = v
        if v < mini:
            mini = v
    return {'min':mini, 'max': maxi}


#Exercice 2:

class Carte:
    def __init__(self, c, v):
        self.couleur = c
        self.valeur = v

    def get_valeur(self):
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def get_couleur(self):
        couleurs = ['pique', 'coeur', 'carreau', 'trÃ¨fle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        self.paquet=[]
        for c in range (1,5):
            for v in range(1,14):
                self.paquet.append(Carte(c,v))
            

    def get_carte(self, pos):
        assert pos < 52 and pos > -1, "paramÃ¨tre pos invalide"
        return self.paquet[pos]
    
