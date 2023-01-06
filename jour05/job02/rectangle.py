def draw_rect(width, height):
    for h in range(height):
        char_line = ""
        for w in range(width):
            if w == 0 or w == width-1:
                char_line += "|"
            elif h != 0 and h != height-1:
                char_line += " "
            else:
                char_line += "-"
        print(char_line)
        # jump to next line
        print("", end="")

print("Entrez la largeur du rectangle: ", end=" ")
width = input()
print("Entrez la hauteur du rectangle: ", end=" ")
height = input()
draw_rect(int(width), int(height))