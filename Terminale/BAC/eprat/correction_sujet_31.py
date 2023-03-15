#Exercice 1:

def nb_repetitions(elt, tab):
    c = 0
    for v in tab:
        if v == elt:
            c = c + 1
    return c


#Exercice 2:

def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a > 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a

