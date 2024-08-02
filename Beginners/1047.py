startHour, startMinute, endHour, endMinute = map(int, input().split())

startTimeMinute = (startHour * 60) + startMinute
endTimeMinute = (endHour * 60) + endMinute

time = endTimeMinute - startTimeMinute

if time <= 0:
    time += 24 * 60

hour, minute = time // 60, time % 60


print(f'O JOGO DUROU {hour} HORA(S) E {minute} MINUTO(S)')
