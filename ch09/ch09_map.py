

def sq(n): return n**2
def even(n): return n % 2 == 0
def sum_sq_even(n):
    result = 0
    for i in range(1, n):
        if even(i):
            result += sq(i)
    return result

print(sum_sq_even(10))

#### 

def sum_sq_even(n):
    return sum(map(sq, filter(even, range(1, n))))

print(sum_sq_even(10))

#### 

def dec_memo(func):
    cache = func.cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@dec_memo
def fib_r(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r(n-1) + fib_r(n-2)
fib = fib_r

def odd(n):
    return n % 2 != 0
    
def odd_fibs(n):
    result = []
    i = 0
    while i < n:
        temp = fib(i)
        if odd(temp):
            result.append(temp)
        i += 1
    return result

print(odd_fibs(10))

####

def odd_fibs(n):
    return list(filter(odd, map(fib, range(n))))

print(odd_fibs(10))

#### 

def my_map(func, iterable):
    result = []
    for e in iterable:
        result.append(func(e))
    return result
def my_filter(func, iterable):
    result = []
    for e in iterable:
        if func(e):
            result.append(e)
    return result

def sum_sq_even(n):
    return sum(my_map(sq, my_filter(even, range(1, n))))

print(sum_sq_even(10))

def odd_fibs(n):
    return list(my_filter(odd, my_map(fib, range(n))))

print(odd_fibs(10))

#### 

def sum_sq_even(n):
    return sum(my_map(sq, 
                      my_filter(even, 
                                range(1, n))))

def odd_fibs(n):
    return list(my_filter(odd, 
                          my_map(fib, 
                                 range(n))))

#### 
print('-' * 20)
from operator import add
def sum_sq_even(n):
    return reduce(add, 
                  map(sq, 
                      filter(even, 
                             range(1, n))))

def odd_fibs(n):
    return reduce(lambda x, y: x+[y], 
                  filter(odd, 
                         map(fib, 
                             range(n))),
                  [])


print(sum_sq_even(10))
print(odd_fibs(10))
