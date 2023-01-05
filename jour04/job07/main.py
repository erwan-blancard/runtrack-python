def multiples_3():
    n = 0
    L = [8, 24, 48, 2, 16]
    for i in L:
        if i % 3 == 0:
            n += 1
    print("Il y a", n, "multiple(s) de 3 dans L.")

multiples_3()