import calendar

def getMonthName(b: int = 1):
    months = list(calendar.month_name)
    return months[b]


mothNumber = int(input())

print(getMonthName(mothNumber))
