#Exercice 1:

def moyenne(liste_notes):
    s_n = 0
    s_c = 0
    for v in liste_notes:
        s_n = s_n + v[0]*v[1]
        s_c = s_c + v[1]
    return s_n / s_c



#Exercice 2:

def pascal(n):
    triangle= [[1]]
    for k in range(1, n+1):
        ligne_k = [1]
        for i in range(1,k):
            ligne_k.append(triangle[k-1][i-1]+triangle[k-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle

