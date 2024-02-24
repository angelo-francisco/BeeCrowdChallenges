A, B, C = map(int, input().split())

maior_ab = (A+B + abs(A - B)) / 2
maior = (maior_ab+C + abs(maior_ab - C)) / 2

print(f'{int(maior)} eh o maior')

