value = float(input())

intervals = ([0, 25], [25, 50], [50, 75], [75, 100])

if value < 0 or value > 100:
    print('Fora de intervalo')

else:
    for interval in intervals:
        if interval[0] <= value <= interval[1]:
            print(f"Intervalo {'(' if 25 <= interval[0] <= 75 else '['}{interval[0]},{interval[1]}]")
            break
        