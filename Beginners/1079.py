N = int(input())

for _ in range(N):
    g1, g2, g3 = map(float, input().split())
    avarage = ((g1 * 2) + (g2 * 3) + (g3 * 5)) / 10

    print(f'{avarage:.1f}')