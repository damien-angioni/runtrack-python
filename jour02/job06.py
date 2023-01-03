def relatif(nombre):
    if(nombre > 0):
        return "positif"
    elif(nombre < 0):
        return "négatif"
    else:
        return "nul"
print(relatif(4))
print(relatif(-12))
print(relatif(0))