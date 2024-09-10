values = [int(input()) for _ in range(100)]

big = max(values)
big_pos = values.index(big) + 1

print(big)
print(big_pos)
