

# examples:
# leap year: 1600, 1992, 1996, 2000, 2060, 2400
# not leap year: 1800, 1900, 2100
# not leap year: 1997, 2057

year = 1996

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(year)
    print(' is leap year')
else:
    print(year)
    print(' is not leap year')

year = 2100

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print(year)
    print(' is leap year')
else:
    print(year)
    print(' is not leap year')

