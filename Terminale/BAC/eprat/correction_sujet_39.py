#Exercice 1:

def fibonacci(n):
    tab = [None]*(n+1)
    tab[1] = 1
    tab[2] = 1
    for i in range(3, n+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[n]
        

#Exercice 2:

def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves =  []

    for i in range(len(eleves)) :
        if notes[i] == note_maxi :
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi,meilleurs_eleves)



eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]