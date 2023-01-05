def somme_paires():
    somme = 0
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    for i in L:
        if i % 2 == 0:
            somme = somme + i
    print(somme)

somme_paires()