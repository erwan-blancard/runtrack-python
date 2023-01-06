def round_grades(list):
    rounded_list = []
    i = 0
    while i < len(list):
        if list[i] > 40:
            if list[i] % 10 > 5:
                if list[i] % 10 > 7:
                    rounded_list += [list[i] - list[i] % 10 + 10]
                else:
                    rounded_list += [list[i]]
            else:
                if list[i] % 10 > 2:
                    rounded_list += [list[i] - list[i] % 10 + 5]
                else:
                    rounded_list += [list[i]]
        else:
            rounded_list += [list[i]]
        i += 1

    print(rounded_list)

round_grades([55, 54, 40, 39, 42, 43, 100, 99])
