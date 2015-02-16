

def fact_i(n):
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result
####
def fact_r(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact_r(n-1)
####
def fact_r_tail(n, result=1):
    if n == 1 or n == 0:
        return result
    else:
        return fact_r_tail(n-1, n*result)
####

import sys

class TailRecurseException(BaseException):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        if (f.f_back and f.f_back.f_back and
             f.f_back.f_back.f_code == f.f_code):
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs
    return func

# @tail_call_optimized
# def fact_tco(n, result=1):
    # if n == 1 or n == 0:
        # return result
    # else:
        # return fact_tco(n-1, n*result)
def fact_tco(n, result=1):
    if n == 1 or n == 0:
        return result
    else:
        return fact_tco(n-1, n*result)

fact_tco = tail_call_optimized(fact_tco)

for i in range(2, 50):
    x = fact_i(i)
    y = fact_r(i)
    z = fact_r_tail(i)
    w = fact_tco(i)
    if x == y == z == w:
        pass
    else:
        print('error')

# print(fact_i(980))
sys.setrecursionlimit(2000)
print(fact_r_tail(1000))
sys.setrecursionlimit(100)
print(fact_tco(1000))
for i in range(1000, 1050, 3):
    x = fact_i(i)
    w = fact_tco(i)
    if x == w:
        pass
    else:
        print('error')
