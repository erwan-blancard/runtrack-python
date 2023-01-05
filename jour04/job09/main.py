def liste_max_min():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    last_min_value = None
    last_max_value = None
    for i in L:
        if last_min_value == None:
            last_min_value = i
        elif i < last_min_value:
            last_min_value = i

    for i in L:
        if last_max_value == None:
            last_max_value = i
        elif i > last_max_value:
            last_max_value = i

    print(last_min_value)
    print(last_max_value)

def liste_max_min_court():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    print(min(L))
    print(max(L))

liste_max_min()

liste_max_min_court()