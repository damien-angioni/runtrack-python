def incrémente_valeur():
    L=[7,11,42,39,2]
    i=0
    while (i <= len(L)-1):
        L[i]+=1
        i += 1
    return L
print(incrémente_valeur())