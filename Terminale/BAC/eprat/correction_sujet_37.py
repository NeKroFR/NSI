#Exercice 1:

def recherche(elt, tab):
    indice = -1
    for i in range(len(tab)):
        if tab[i] == elt:
            indice = i
    return indice

#Exercice 2:

class AdresseIP:

    def __init__(self, adresse):
        self.adresse = adresse
   
    def liste_octet(self):
        return [int(i) for i in self.adresse.split(".")] 
        
    def est_reservee(self):
        return self.adresse == '192.168.0.0' or self.adresse == '192.168.0.255'
             
    def adresse_suivante(self):
        if self.liste_octet()[3] < 254:
            octet_nouveau = self.liste_octet()[3] + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False

adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')
