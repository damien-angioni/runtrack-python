def agronomie(type,saison):
    if(type == "fruit"):
        if(saison == "été"):
            return "Poire, fraise et cassis"
        elif(saison == "hiver"):
            return "orange, mandarine, kiwi"
        else:
            return "saison invalide"
    elif(type == "légume"):
        if(saison == "été"):
            return "artichaut, aubergine, navet"
        elif(saison == "hiver"):
            return "carotte, topinambour, endive"
        else:
            return "saison invalide"
    else:
        return "type invalide"
print(agronomie("légume","été"))
print(agronomie("fruit","hiver"))
print(agronomie("croissant","été"))