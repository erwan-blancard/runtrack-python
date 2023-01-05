def produit():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    nombres_valides = []
    for i in L:
        if i >= 25 and i <= 90:
            nombres_valides.append(i)

    resultat = 1
    for i in nombres_valides:
        resultat = resultat * i

    print(resultat)

produit()