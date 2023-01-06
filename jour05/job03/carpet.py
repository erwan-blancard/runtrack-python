def draw_carpet(n):
    for h in range(n+2):
        char_line = ""
        for w in range(n+2):
            if h == 0 or h == n+1:
                if w == 0 or w == n+1:
                    char_line += "+"
                else:
                    char_line += "-"
            else:
                if w == 0 or w == n+1:
                    char_line += "|"
                elif w == (n+1) - h:
                    char_line += " "
                else:
                    char_line += "#"
        print(char_line)
        # jump to next line
        print("", end="")

print("Entrez la taille du tapis: ", end=" ")
n = input()
draw_carpet(int(n))