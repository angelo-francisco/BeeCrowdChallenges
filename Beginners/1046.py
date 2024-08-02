start, end = map(int, input().split())

duration = end - start

if start == end:
    print(f'O JOGO DUROU 24 HORA(S)')
else:
    if duration < 0:
        duration = 24 - abs(duration)

    print(f'O JOGO DUROU {duration} HORA(S)')