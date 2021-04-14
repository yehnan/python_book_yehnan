

def is_leap_year(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False

def year_days(year):
    return 365 + (1 if is_leap_year(year) else 0)

# argument month is 1, 2, 3, ..., 11, 12
def month_days(month, year):
    md = [31, 28, 31, 30, 31, 30,
          31, 31, 30, 31, 30, 31]
    return md[month-1] + (1 if month == 2 and is_leap_year(year) else 0)

# assume epoch is [1970, 1, 1]
def days_since_epoch(date):
    year, month, day = date
    
    days = day
    for y in range(1970, year):
        days += year_days(y)
    for m in range(1, month):
        days += month_days(m, year)
        
    return days
    
def days_diff(date1, date2):
    return days_since_epoch(date2) - days_since_epoch(date1)

        
##

date1 = [2014, 11, 12]
date2 = [2015, 2, 15]

print(days_diff(date1, date2), "days")


# from datetime import date
# print(date(*date2) - date(*date1))


# for y in range(1970, 2020):
    # for m in range(5, 11+1):
        # for d in range(5, 27):
            # date1 = [y, m, d]
            # date2 = [y+1, m-2, d-3]
            # if days_diff(date1, date2) != (date(*date2) - date(*date1)).days:
                # print("Failed")

