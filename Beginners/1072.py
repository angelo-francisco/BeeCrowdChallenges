N = int(input())
values = [int(input()) for _ in range(N)]

countIn = countOut = 0

for value in values:
    if 10 <= value <= 20:
        countIn += 1
    else:
        countOut += 1

print(f'{countIn} in\n{countOut} out')