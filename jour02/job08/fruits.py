def végétaux_de_saison(type, saison):
    if (type == "fruit") and (saison == "hiver"):
        print("orange, mandarine et kiwi")

    if (type == "fruit") and (saison == "ete"):
        print("Poire, fraise, cassis")

    if (type == "legume") and (saison == "hiver"):
        print("carotte, topinambour, endive")

    if (type == "legume") and (saison == "ete"):
        print("artichaut, aubergine,navet")

végétaux_de_saison("fruit","hiver")
végétaux_de_saison("fruit","ete")
végétaux_de_saison("legume","hiver")
végétaux_de_saison("legume","ete")