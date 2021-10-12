F = int(input())
S = int(input())
T = int(input())
if F + S + T == 180:
    
    if F != S and F != T and T != S:
        
        print("Scalene")
    
    if F == S and F == T and F == 60:
        print("Equilateral")
    
    if (F == S and S != T) or (F == T and T != S) or (T == S and S != F):
        print("Isosceles")
    
if F + S + T != 180:
    print("Error")
