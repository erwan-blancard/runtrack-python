import math as maths
def triangle(a, b, c):
    # vérifie si le triangle est possible
    if ((a + b > c) and (a + c > b) and (b + c > a)) == False:
        return "Le triangle ABC n'est pas valide"

    # vérifie si le triangle est équilatéral
    if a == b and b == c:
        return "Le triangle ABC est équilatéral"

    # vérifie si le triangle est isocèle: si oui, vérifie s'il est rectangle isocèle, sinon , vérifie s'il est rectangle
    if a == b or a == c or b == c:

        # vérifie si le triangle est rectangle
        if pythagore(a, b, c):
            return "Le triangle ABC est isocèle rectangle"
        else:
            return "Le triangle ABC est isocèle"

    # vérifie si le triangle est rectangle
    elif pythagore(a, b, c):
        return "Le triangle ABC est rectangle"
    else:
        return "Le triangle ABC est quelconque"

def pythagore(a, b, c):
    longueurs = [a, b, c]
    # print("Initial:", longueurs)
    # tri des longueurs de la plus grande à la plus petite pour appliquer ensuite le théorème de Pythagore
    while longueurs[0] < longueurs[1] or longueurs[1] < longueurs[2]:
        if longueurs[0] < longueurs[1]:
            longueurs = [longueurs[1], longueurs[0], longueurs[2]]

        if longueurs[1] < longueurs[2]:
            longueurs = [longueurs[0], longueurs[2], longueurs[1]]

        # print("In loop:", longueurs)

    if pow(longueurs[0], 2) == pow(longueurs[1], 2) + pow(longueurs[2], 2):
        return True
    else:
        return False

# invalide
print(triangle(1,1,3))
# quelconque
print(triangle(5,6,7))
# équilatéral
print(triangle(3,3,3))
# isocèle
print(triangle(3,4,4))
# rectangle
print(triangle(3,4,5))
# isocèle rectangle (impossible à cause des floats)
print(triangle(3,3,maths.sqrt((pow(3, 2)) + (pow(3, 2)))))