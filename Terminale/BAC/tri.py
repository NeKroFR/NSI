def tri_selection(liste):
    n = len(liste)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

def tri_insertion(liste):
    n = len(liste)
    for i in range(1, n):
        courant = liste[i]
        j = i
        while j > 0 and liste[j - 1] > courant:
            liste[j] = liste[j - 1]
            j -= 1
        liste[j] = courant
    return liste


T = [4,5,6,87,0,23,5,6,4]
print(tri_selection(T))
T = [4,5,6,87,0,23,5,6,4]
print(tri_insertion(T))
