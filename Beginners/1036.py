import math 

A, B, C = map(float, input().split())

try:
    delta = B ** 2 - (4 * A * C)
    x1 = (-B + math.sqrt(delta)) / (2 * A)
    x2 = (-B - math.sqrt(delta)) / (2 * A)

    print(f"R1 = {x1:.5f}\nR2 = {x2:.5f}")
except:
    print('Impossivel calcular')