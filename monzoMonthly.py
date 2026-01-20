january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31
year = [january, february, march, april, may, june, july, august, september, october, november, december]

def getAllMonthlyDeposits(): 
    x, y = 1, 32
    for month in year:
        yield getMonthlyDeposit(x, y)
        x = y + 1
        y = x + month +1

def getMonthlyDeposit(currentDay: int, lastDay: int) -> float:
    monthlyDeposit = 0
    for i in range(currentDay, lastDay):
        monthlyDeposit = round(monthlyDeposit + round((currentDay * 0.01), 2), 2)
    return monthlyDeposit

x = getAllMonthlyDeposits()
for i in x:
    print(i)
"""
loop through each month in year
for month in year:
x, y = 1, len(month)
    getMonthlyDeposit(x, y)
    x = y + 1
    y = x + len(month)

loop through each day in month from current day to last day of month
daily deposit = current day * 0.01
"""