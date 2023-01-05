def switch_F_L_terms(list):
    if list == None or list == 0:
        return None
    if len(list) == 1:
        return list

    value_F = list[0]
    value_L = list[len(list)-1]
    list[0] = value_L
    list[len(list)-1] = value_F
    return list

print(switch_F_L_terms([8496, 541, 44, 54544556, 484848488]))