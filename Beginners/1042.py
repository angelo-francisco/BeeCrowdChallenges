values = list(map(int, input().split()))

for value in sorted(values, reverse=False):
    print(value)

print()

for value in values:
    print(value)