import csv
"""
Partie I
"""
def dicoPlusMoins(nomDeFichier:str)->dict:
    '''
    A partir du nom de fichier csv contenant des avis positifs (1) ou négatifs (-1)
    La fonction construit le dictionnaire des mots en ajoutant à la valeur de chaque mot 1 si l'avis est positif et enlevant 1 si l'avis est négatif
    La fonction renvoie le dictionnaire ainsi construit
    '''
    with open(nomDeFichier,'r',encoding='utf-8') as fichier:
        T = []
        lecteur=csv.reader(fichier,delimiter=';')
        for row in lecteur:
           T.append(row)
        for element in T:
           element[0]=element[0].split()
    data = {}
    for i in T:
        for m in i[0]:
            if m in data.keys():
                data[m] = int(data.get(m)) + int(i[1])
            else:
                data[m] = i[1]
    return data

def AnalyseAvis(avis,dico):
    '''
    avis est une chaine de caractères à analyser
    dico est un dictionnaire. les clefs sont des mots, les valeurs sont les notes attribus à chaque mot par la fonction dicoPlusMoins
    la fonction renvoie une note entière attribuée à la chaine de caractères avis
    exemple :
    AnalysedeTexte("très mauvais restaurant")
    >>> -38
    Cet exemple ne peux servir de test unitaire, le dictionnaire dépendant lui même des données utilisées.
    '''
    note = 0
    wordlist = []
    for i in avis.split():
        if i in dico.keys():
           note += int(dico.get(i))
    return note


dico = dicoPlusMoins("avisposneg.csv")
note1 = AnalyseAvis("Très mauvais restaurant , nous sommes  déçus . Pas de goût, pas de textures", dico)        
note2 = AnalyseAvis("Très bonne crêperie nous sommes très contents de ce moment. très sympa. Les galettes sont bien garnies et très bonnes", dico)        

print(note1, note2)

"""
Partie II
"""
def dicoPlusMoinsV2(nomDeFichier:str)->dict:
    """
    Pour tous les commentaires du fichiers de données
	calculer le score du commentaire
		si le score est positif et que le commentaire est positif 
			alors ne rien faire
		si le score est négatif et que le commentaire est négatif 
			alors ne rien faire
		si le score est positif et que le commentaire est négatif
			alors décrémenter la valeur de tous les mots du commentaire
		si le score est négatif et que le commentaire est positif
			alors incrémenter la valeur de tous les mots du commentaire 
    """
    with open(nomDeFichier,'r',encoding='utf-8') as fichier:
        T = []
        lecteur=csv.reader(fichier,delimiter=';')
        for row in lecteur:
           T.append(row)
        for m in T:
            m[0]=m[0].split()
    data = {}
    for i in T:
        val_avis=0
        for m in i[0]:
            if m in data:
                val_avis=val_avis+data[m]
            else:
                data[m]=0
                if i[1]=='1' and val_avis<=0:
                    for m in i[0]:
                        if m in data:
                            data[m]=data[m]+1
                        else:
                            data[m]=1
                if i[1]=='-1' and val_avis>0:
                    for m in i[0]:
                        if m in data:
                            data[m]=data[m]-1
                        else:
                            data[m]=-1                
    return data
    

dico = dicoPlusMoinsV2("avisposnegtest.csv")
print(dico)