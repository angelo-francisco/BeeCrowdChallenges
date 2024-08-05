values = [float(input()) for _ in range(5)]

count = 0

for value in values:
    if value % 2 == 0:
        count += 1

print(count, 'valores pares')