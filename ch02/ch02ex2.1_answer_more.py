

from __future__ import print_function

# Generally, if a year is (evenly) divisible by 4, then it is a leap year. 
# However, there are a couple of exceptions. 
# If the year is divisible by 4 but is also divisible by 100, 
# then it is not a leap year - unless, it is also divisible by 400, then it is.

# examples:
# leap year: 1600, 1992, 1996, 2000, 2060, 2400
# not leap year: 1800, 1900, 2100
# not leap year: 1997, 2057

def leapyear_0(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
        
def leapyear_1(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False
        
def leapyear_2(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def leapyear_3(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

if __name__ == '__main__':
    funcs = [leapyear_0, leapyear_1, leapyear_2, leapyear_3]
    leapyears = [1600, 1992, 1996, 2000, 2060, 2400]
    not_leapyears = [1800, 1900, 2100, 1997, 2057]
    allpass = True
    for f in funcs:
        print('Testing function: %s' % f.__name__)
        for y in leapyears:
            if f(y) != True:
                print('Failed: %d is leap year' % y)
                allpass = False
        for y in not_leapyears:
            if f(y) != False:
                print('Failed: %d is not leap year' % y)
                allpass = False
    if allpass:
        print('All passed')
    else:
        print('Not all passed')
    
    