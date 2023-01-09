taille=input("choisir taille:")
def tapis(n):
    n+=1
    segment=int(n)*"-"
    print("+"+segment+"+")
    i=0
    while(i<n):
        j=1
        k=0
        print("|",end="")
        while(j<n-i):
            print("#",end="")
            j+=1
        print(" ",end="")
        while(k<i):
            print("#",end="")
            k+=1
        print("|")
        i+=1
    print("+"+segment+"+")
tapis(int(taille))