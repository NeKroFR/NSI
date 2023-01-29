def sac_a_dos(poids, valeur, capacite):
    n = len(poids)
    ratio = [(valeur[i] / poids[i], poids[i], valeur[i]) for i in range(n)]
    ratio.sort(reverse=True)
    poids_total = 0
    valeur_totale = 0
    for r, p, v in ratio:
        if poids_total + p <= capacite:
            poids_total += p
            valeur_totale += v
        else:
            fraction = (capacite - poids_total) / p
            valeur_totale += v * fraction
            break
    return valeur_totale

poids = [10, 20, 30]
valeur = [60, 100, 120]
capacite = 50
print(sac_a_dos(poids, valeur, capacite))