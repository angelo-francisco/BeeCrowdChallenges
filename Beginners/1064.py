values = [float(input()) for _ in range(6)]

count, _sum = 0, 0

for value in values:
    if value > 0:
        _sum += value
        count += 1

avarage = _sum / count

print(count, 'valores positivos')
print(f'{avarage:.1f}')