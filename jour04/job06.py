cardinaux=[0,1,2,3,4,5,6,7,8,9]
def swap(liste):
    a=liste[0]
    liste[0]=liste[len(liste)-1]
    liste[len(liste)-1]=a
    print(liste)
swap(cardinaux)