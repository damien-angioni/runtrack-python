import random
def modifier(liste):
    liste[3]=liste[2]+liste[4]
def numberlist():
    L=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    print(L[1])
    modifier(L)
    print(L[4])
    return L
print(numberlist())