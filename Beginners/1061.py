dayStart = int(input().split()[1])
hourStar, minuteStart, secondStart = map(int, input().split(' : '))

dayEnd = int(input().split()[1])
hourEnd, minuteEnd, secondEnd = map(int, input().split(' : '))

secondsStart = dayStart * (24 * 3600) + hourStar * 3600 + minuteStart * 60 + secondStart
secondsEnd = dayEnd * (24 * 3600) + hourEnd * 3600 + minuteEnd* 60 + secondEnd
seconds = secondsEnd - secondsStart

days = seconds // (24 * 3600)
seconds %= (24 * 3600)

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
_seconds = seconds % 60

print(f"{int(days)} dia(s)\n{int(hours)} hora(s)\n{int(minutes)} minuto(s)\n{int(_seconds)} segundo(s)")