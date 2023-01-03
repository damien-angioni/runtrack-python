def calcule(var1,operator,var2):
    if(operator == "+"):
        return var1+var2
    elif(operator == "-"):
        return var1-var2
    elif(operator == "*"):
        return var1*var2
    elif(operator == "/"):
        return var1/var2
    elif(operator == "%"):
        return var1%var2
    else:
        return "Opérateur invalide"
print(calcule(2,"+",3))
print(calcule(5,"*",12))
print(calcule(60,"-",18))
print(calcule(42,"/",7))
print(calcule(6,"%",3))
print(calcule(0,"x",0))