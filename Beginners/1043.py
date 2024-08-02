A, B, C = map(float, input().split())

perimeter = area = 0

def bol_triangle(a, b, c):
    if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b):
       return True
    else:
        return False

if bol_triangle(A, B, C):
    perimeter = A + B + C
    print(f'Perimetro = {perimeter:.1f}')

else:
    area = ((A + B) * C) / 2
    print(f'Area = {area:.1f}') 