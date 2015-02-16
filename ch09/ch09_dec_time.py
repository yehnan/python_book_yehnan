

def dec_time(func):
    def wrapper(*args, **kwargs):
        import time
        t_start = time.clock()
        res = func(*args, **kwargs)
        t_end = time.clock()
        print(func.__name__, t_end-t_start)
        return res
    return wrapper

def fact_i(n):
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result

@dec_time
def foo(n):
    for i in range(n):
        fact_i(i)
foo(1000)
