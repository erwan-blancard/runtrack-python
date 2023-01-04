def reverse_string():
    print("Entrez une chaîne: ")
    str_input = input()
    str_reverse = ""
    i = len(str_input)
    while i > 0:
        str_reverse = str_reverse + str_input[i-1]
        i -= 1
    print(str_reverse)

reverse_string()