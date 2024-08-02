A, B, C = sorted(list(map(float, input().split())), reverse=True)

if A >= B + C:
    print('NAO FORMA TRIANGULO')

else:
    if pow(A, 2) == pow(B, 2) + pow(C, 2):
        print('TRIANGULO RETANGULO')
    
    elif pow(A, 2) > pow(B, 2) + pow(C, 2):
        print('TRIANGULO OBTUSANGULO')
    
    elif pow(A, 2) < pow(B, 2) + pow(C, 2):
        print('TRIANGULO ACUTANGULO')
    
    if A == B == C:
        print('TRIANGULO EQUILATERO')
        
    else:
        if A == B or B == C or A == C:
            print('TRIANGULO ISOSCELES')