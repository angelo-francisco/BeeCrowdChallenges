I: float = 0.0
J: float = 1.0

while I <= 2:
    I = round(I, 2)
    J = round(J, 2)
    
    if float(I).is_integer():
        I = int(I)
    
    if float(J).is_integer():
        J = int(J)

    print(f'I={I} J={J}')
    print(f'I={I} J={J+1}')
    print(f'I={I} J={J+2}')
    
    J += 0.2
    I += 0.2
    