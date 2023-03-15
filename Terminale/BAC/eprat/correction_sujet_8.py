#Exercice 1:

def max_dico(dico):
    maxi_v = 0
    maxi_n = ""
    for nom, val in dico.items():
        if val > maxi_v:
            maxi_v = val
            maxi_n = nom
    return maxi_n, maxi_v



#Exercice 2:

class Pile:

    def __init__(self):
        self.contenu = []

    def est_vide(self):
        return self.contenu == []

    def empiler(self, v):
        self.contenu.append(v)

    def depiler(self):
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()