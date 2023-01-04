def nombres_premiers(number):
    n = [True] * (number + 1)
    n[1] = False    # 1 n'est pas premier
    last_n = 2      # initialise le dernier nombre premier trouvé à 2
    check_index = 2
    while check_index <= number:
        # change en False les entrées de la liste correspondant au nombre associé
        for i in range(check_index + 1, number + 1):
            # vérifie si le nombre est divisible par le dernier nombre premier trouvé
            if i % check_index == 0:
                n[i] = False

        # cherche le prochain nombre entier
        check_index += 1
        while check_index < number and n[check_index] != True:
            check_index += 1

    for i in range(2, number +1):
        if n[i] == True:
            print(i)

nombres_premiers(1000)