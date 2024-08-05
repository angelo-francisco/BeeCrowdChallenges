values = [float(input()) for _ in range(6)]

count = 0

for value in values:
    if value > 0:
        count += 1


print(count, 'valores positivos')