def calcule(num1, operateur, num2):
    if(operateur == "+"):
        return num1 + num2
    elif(operateur == "-"):
        return num1 - num2
    elif(operateur == "*"):
        return num1 * num2
    elif (operateur == "/"):
        return num1 / num2
    elif (operateur == "%"):
        return num1 % num2
    else:
        print("Le symbole suivant n'est pas reconnu:",operateur)
        return None

print(calcule(5,"+",9))
print(calcule(5,"-",9))
print(calcule(5,"*",9))
print(calcule(5,"/",9))
print(calcule(5,"%",9))
print(calcule(5,"e",9))