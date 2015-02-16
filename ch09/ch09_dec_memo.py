

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

def fib_r2(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r2(n-1) + fib_r2(n-2)

def dec_time(func):
    def wrapper(*args, **kwargs):
        import time
        t_start = time.clock()   
        res = func(*args, **kwargs)
        t_end = time.clock()  
        print(func.__name__, t_end-t_start)
        return res
    return wrapper
@dec_time
def foo1():
    for i in range(6000):
        fib_r(i)
@dec_time
def foo2():
    for i in range(33):
        fib_r2(i)
        
foo1()
foo2()
