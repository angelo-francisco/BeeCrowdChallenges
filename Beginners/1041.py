x, y = map(float, input().split())

if x == y == 0:
    print('Origem')

else:
    if  x > 0 and y > 0:
        print('Q1')
    
    elif x > 0 and y < 0:
        print('Q4')

    elif x < 0 and y < 0:
        print('Q3')
    
    elif x < 0 and y > 0:
        print('Q2')
    
    else:
        if (x == 0 and y != 0):
            print('Eixo Y')
        
        else:
            print('Eixo X')