def retourner(chaine):
    rendu=""
    i = len(chaine) - 1 
    while i >= 0:
        rendu += chaine[i]
        i -= 1
    return rendu
print(retourner("nikana"))