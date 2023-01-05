L=[8,24,27,48,2,16,9,102,7,84,91]
minimum=25
maximum=90
def Produit_intervalle(intlow,inthigh,liste):
    i=0
    produit=1
    while (i <= len(liste)-1):
        if (intlow<=liste[i]<=inthigh):
            produit=produit*liste[i]
        i += 1
    return produit
print(Produit_intervalle(minimum,maximum,L))