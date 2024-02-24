A, B, C = map(float, input().split())

PI = 3.14159
triangulo = (A*C) / 2
circulo = (C**2) * PI
trapezio = (A+B) * C / 2
quadrado = B**2
reactangulo = A * B

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {reactangulo:.3f}')

