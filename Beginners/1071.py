x = int(input())
y = int(input())

_sum = 0

if x > y:
    for i in range(x-1, y, -1):
        if i % 2 != 0:
            _sum += i

else:
    for i in range(x+1, y):
        print(i)
        if i % 2 != 0:
            _sum += i

print(_sum)
