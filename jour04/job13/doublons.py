def remove_duplicates(list):
    singles_list = []
    empty_flag = False

    while not empty_flag:
        index_list = []
        ref_num = list[0]
        i = 0
        while i < get_lenght(list):
            if list[i] == ref_num:
                index_list += [i]
            i += 1

        j = 0
        while j < get_lenght(index_list):
            list = suppr_item(list, index_list[j] - j)
            j += 1

        singles_list += [ref_num]

        if get_lenght(list) == 0:
            empty_flag = True

    return singles_list

def get_lenght(list):
    l = 0
    for i in list:
        l += 1
    return l
def suppr_item(list, index):
    newlist = []
    i = 0
    while i < get_lenght(list):
        if i != index:
            newlist += [list[i]]
        i += 1
    return newlist

print(remove_duplicates([10,20,30,20,10,50,60,40,80,50,40]))