
# -*- coding: utf-8 -*-
def fact(n):
    if type(n) is not int:
        raise TypeError
    if n < 0:
        raise ValueError('Argument must be non-negative')
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result

while True:
    try:
        s = input('input n: ')     # 2.x版改用raw_input
        f = fact(int(s))
    except TypeError:
        print('%s is not an integer' % s)
        break
    except ValueError as e:
        print('%s can not be less than 0' % s)
        break
    print('%s! = %d' % (s, f))


