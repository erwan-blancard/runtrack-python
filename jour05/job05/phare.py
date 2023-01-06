def pedometer(x, y):
    print("Pour", x, "marches de", y, "cm, le gardien parcours", ((((x * y)*2)*5)*7) / 100, "m par semaine.")

print("Entrez le nombre de marches: ", end=" ")
x = input()
print("Entrez la taille des marches (cm): ", end=" ")
y = input()
pedometer(int(x), float(y))