width=input("Largeur:")
height=input("Hauteur:")
i=0
segment=int(width)*"-"
espace=int(width)*" "
print("|",segment,"|")
while(i+3<=int(height)):
    print("|",espace,"|")
    i+=1
print("|",segment,"|")