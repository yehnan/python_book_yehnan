

def product(iterable, start=1):
    result = start
    for x in iterable:
        result *= x
    return result

def my_factorial(n):
    return product(range(2, n+1))

from math import factorial
print('6! is ' + str(my_factorial(6)))
print('math.factorial: ' + str(factorial(6)))
print('10! is ' + str(my_factorial(10)))
print('math.factorial: ' + str(factorial(10)))
print('15! is ' + str(my_factorial(15)))
print('math.factorial: ' + str(factorial(15)))
