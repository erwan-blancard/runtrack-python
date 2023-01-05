def liste_nombres():
    L = [5, 8, 95, 69, 41]
    print(L[1])
    L = somme_3(L)
    print(len(L))

def somme_3(list):
    list[3] = list[2] + list[4]
    print("Somme de L[2] et L[4] dans L[3]:", list[3])
    return list

liste_nombres()