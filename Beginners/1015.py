X1, Y1 = map(float, input().split())
X2, Y2 = map(float, input().split())

distancia = (((X2 - X1) ** 2) + ((Y2 - Y1) ** 2)) ** (1 / 2)

print(f"{distancia:.4f}")
