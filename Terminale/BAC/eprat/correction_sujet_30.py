#Exercice 1:

def moyenne (tab):
    s = 0
    for v in tab:
        s = s + v
    return s / len(tab)



#Exercice 2:

def binaire(a):
    bin_a = str(a % 2)
    a = a // 2
    while a > 0 :
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

