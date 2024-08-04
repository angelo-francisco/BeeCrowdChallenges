wage =  float(input())

wageList = [
    (0, 400, 15),
    (400.01, 800, 12),
    (800.01, 1200, 10),
    (1200.01, 2000, 7), 
]

wagePercentual, wageEarned = 0, 0

if wage > 2000:
    wagePercentual = 4
    wageEarned = wage * (wagePercentual / 100)
    wage += wageEarned

else:
    for _wage in wageList:
        if _wage[0] <= wage <= _wage[1]:
            wagePercentual = _wage[2]
            wageEarned = wage * (wagePercentual / 100)
            wage += wageEarned

            break


print(f'Novo salario: {wage:.2f}')
print(f'Reajuste ganho: {wageEarned:.2f}')
print(f'Em percentual: {wagePercentual} %')
