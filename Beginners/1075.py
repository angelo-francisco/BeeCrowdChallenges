N = int(input())

start, end = 1, 10000
for num in range(start, end+1):
    if num % N == 2:
        print(num)