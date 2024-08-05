values = [int(input()) for _ in range(5)]

countPA, countI, countPO, countN = 0, 0, 0, 0

for value in values:
    if value > 0:
        countPO += 1
    if value < 0:
        countN += 1
    if value % 2 == 0:
        countPA += 1
    if value % 2 != 0:
        countI += 1


print(countPA, 'valor(es) par(es)')
print(countI, 'valor(es) impar(es)')
print(countPO, 'valor(es) positivo(s)')
print(countN, 'valor(es) negativo(s)')