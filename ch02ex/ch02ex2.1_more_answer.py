

from __future__ import print_function

# examples:
# leap year: 1600, 1992, 1996, 2000, 2060, 2400
# not leap year: 1800, 1900, 2100
# not leap year: 1997, 2057

def leapyear_a(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
        
def leapyear_b(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False
        
def leapyear_c(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def leapyear_d(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

if __name__ == '__main__':
    funcs = [leapyear_a, leapyear_b, leapyear_c, leapyear_d]
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
    
    