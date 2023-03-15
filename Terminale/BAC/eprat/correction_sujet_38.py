#Exercice 1:

def correspond(mot, mot_a_trous):
    n1 = len(mot)
    n2 = len(mot_a_trous)
    if n1 != n2:
        return False
    for i in range(n1):
        if mot[i] != mot_a_trous[i] and mot_a_trous[i] != '*':
            return False
    return True

#Exercice 2:

def est_cyclique(plan):
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinaires = 1
    
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinaires += 1

    return nb_destinaires == len(plan)