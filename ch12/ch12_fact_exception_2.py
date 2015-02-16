
# -*- coding: utf-8 -*-
def fact(n):
    if type(n) is not int:
        raise TypeError('Argument must be type int')
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
    except (EOFError, KeyboardInterrupt) as e:
        print('Bye')
        break
    except TypeError as e:
        print('Error: ' + str(e))
    except ValueError as e:
        print('Error: ' + str(e))
    except Exception:
        print('Error: unknown error')
    else:
        print('%s! = %d' % (s, f))

