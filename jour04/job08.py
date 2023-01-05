L=[8,24,7,48,2,16,9,7,84,91]
def Somme_de_Liste(liste):
    i=0
    somme=0
    while (i <= len(liste)-1):
        if (liste[i]%2==0):
            somme=somme+liste[i]
        i += 1
    return somme
print(Somme_de_Liste(L))