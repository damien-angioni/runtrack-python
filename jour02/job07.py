def pronostic(langage):
    if(langage == "javascript"):
        return "tu es un developpeur web"
    elif(langage == "python"):
        return "tu es un développeur IA"
    elif(langage == "java"):
        return "tu es un développeur logiciel"
    elif(langage == "reactjs"):
        return "tu es un développeur mobile"
    else:
        return "un jour je serai le meilleur développeur... je coderai sans répit"
print(pronostic("javascript"))
print(pronostic("python"))
print(pronostic("java"))
print(pronostic("reactjs"))
print(pronostic("lua"))