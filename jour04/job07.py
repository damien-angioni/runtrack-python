L=[8,24,48,2,16]
def check_multiple_3(liste):
    i=0
    occurence=0
    while (i <= len(liste)-1):
        if (liste[i]%3==0):
            occurence += 1
        i += 1
    return occurence
print(check_multiple_3(L))