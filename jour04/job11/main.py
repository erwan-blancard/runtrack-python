def add_1():
    L = [7, 11, 42, 39, 2]
    i = 0
    while i < len(L):
        L[i] = L[i] + 1
        i += 1

    print(L)

add_1()