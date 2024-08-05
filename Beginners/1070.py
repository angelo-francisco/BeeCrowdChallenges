x = int(input())

if x % 2 == 0:
    x += 1

for i in range(x, x + (6 * 2), 2):
    print(i)