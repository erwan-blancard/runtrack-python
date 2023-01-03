def signe(nombre):
    if(nombre > 0):
        print(nombre, "est positif.")
    elif (nombre < 0):
        print(nombre, "est négatif.")
    else:
        print("Le nombre est zéro, donc nul.")

signe(5)
signe(-8)
signe(999)
signe(-1)
signe(0)