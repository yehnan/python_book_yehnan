

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



