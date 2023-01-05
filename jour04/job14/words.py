def get_words_greater_than_n(n, sentence):
    words = []
    chars = ""
    for i in sentence:
        if i != " ":
            chars += i
        else:
            words += [chars]
            chars = ""

    for word in words:
        if get_lenght(word) > n:
            print(word, end=" ")

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

get_words_greater_than_n(3, "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance")