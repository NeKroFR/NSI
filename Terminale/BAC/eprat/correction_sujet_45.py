#Exercice 1:

def rangement_valeurs(notes_eval):
    tab = [0]*11
    for n in notes_eval:
        tab[n] = tab[n] + 1
    return tab

def notes_triees(effectifs_notes):
    tab = []
    for i in range(len(effectifs_notes)):
        for _ in range(effectifs_notes[i]):
            tab.append(i)
    return tab




#Exercice 2:

def dec_to_bin (nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if nb_bin == '0':
        return 0
    elif nb_bin == '1':
        return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

