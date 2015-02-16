
import pickle
def dec_memo_limit(func, limit=None):
    if isinstance(func, int):
        def wrapper(f):
            return dec_memo_limit(f, func)
        return wrapper

    d = {}
    li = []
    def wrapper(*args, **kwargs):
        key = pickle.dumps((args, kwargs))
        try:
            li.append(li.pop(li.index(key)))
        except ValueError:
            d[key] = func(*args, **kwargs)
            li.append(key)
            if limit is not None and len(li) > limit:
                del d[li.pop(0)]
        return d[key]

    wrapper._memoize_dict = d
    wrapper._memoize_list = li
    wrapper._memoize_limit = limit
    wrapper._memoize_origfunc = func
    wrapper.__name__ = func.__name__
    return wrapper

@dec_memo_limit(200)
def fib_r(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r(n-1) + fib_r(n-2)
print(fib_r._memoize_limit)

@dec_memo_limit(100)
def fib_r2(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r2(n-1) + fib_r2(n-2)
print(fib_r2._memoize_limit)

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
    for i in range(1000):
        fib_r(i)
@dec_time
def foo2():
    for i in range(1000):
        fib_r2(i)

foo1()
foo2()

import functools
@functools.lru_cache(maxsize=100)
def fib_r3(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r3(n-1) + fib_r3(n-2)

@dec_time
def foo3():
    for i in range(1000):
        fib_r3(i)
foo3()

# @functools.lru_cache(maxsize=300)
# def bar(li):
    # return sum(li)

# print(bar([1,2,3]))
# print(bar([22,22,22]))

@dec_memo_limit
def fib_r4(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r4(n-1) + fib_r4(n-2)
print(fib_r4)


