def triangle_strategy(a,b,c):
    if(a+b < c) or (a+c < b) or (b+c < a):
        return "ça ne peut pas être un triangle :("
    elif(a*a == b*b+c*c) or (b*b == a*a+c*c) or(c*c == a*a+b*b):
        if(a == b) or (a == c) or (b == c):
            return "triangle isocèle et rectangele"
        else:
            return "triangle rectangle"
    elif(a == b == c):
        return "triangle equilateral"
    elif(a == b) or (a == c) or (b == c):
        return "triangle isocèle"
    elif(a+b == c) or (a+c == b) or (b+c == a):
        return "triangle plat"
    else:
        return "triangle quelconque"
print(triangle_strategy(10,4,4))
print(triangle_strategy(3,4,5))
print(triangle_strategy(6,6,6))
print(triangle_strategy(5,7,7))
print(triangle_strategy(10,5,5))
print(triangle_strategy(5,6,8))