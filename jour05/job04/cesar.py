alphabet = "abcdefghijklmnopqrstuvwxyz"

def cesar_encode(message, offset):
    message = message.lower()
    encoded_message = ""
    offset %= 26
    i = 0
    while i < len(message):
        if is_char_valid(message[i]):
            char_index = get_index_in_alphabet(message[i])
            if char_index + offset > 25:
                encoded_message += alphabet[char_index + offset - 26]
            else:
                encoded_message += alphabet[char_index + offset]
        else:
            encoded_message += message[i]
        i += 1

    print(encoded_message)

def get_index_in_alphabet(c):
    i = 0
    while i < len(alphabet):
        if c == alphabet[i]:
            return i
        i += 1
    return None
def is_char_valid(c):
    for char in alphabet:
        if c == char:
            return True
    return False


print("Entrez la phrase: ", end=" ")
message = input()
print("Entrez le décalage: ", end=" ")
offset = input()
cesar_encode(str(message), int(offset))