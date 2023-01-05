def pyramide():
    alphabet = "abcdefghijklmnopqrstuvwxyz" * 10
    i = 0
    total_chars = 0
    str_to_print = ""
    while i <= (len(alphabet) - total_chars):
        for j in range(total_chars, total_chars + i +1):
            str_to_print = str_to_print + alphabet[j]
        print(str_to_print)

        i += 1
        total_chars = total_chars + i
        str_to_print = ""


pyramide()