def round_numbers_list(list):
    i = 0
    while i < get_lenght(list):
        if list[i] % 1 >= 0.5:
            list[i] = (list[i] + 1) // 1
        else:
            list[i] = list[i] // 1

        i += 1

    return sort_list(list)


def sort_list(list):
    list_len = get_lenght(list)
    output_list = []
    while get_lenght(output_list) != list_len:
        i = 0
        last_num = None
        last_num_index = None
        while i < get_lenght(list):
            if last_num == None or list[i] < last_num:
                last_num = list[i]
                last_num_index = i
            i += 1
        output_list += [last_num]
        list = suppr_item(list, last_num_index)

    return output_list

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
            newlist = newlist + [list[i]]
        i += 1
    return newlist

print(round_numbers_list([22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]))