

def dec_notfunc(n):
    def wrapper(func):
        return [func(i) for i in range(n)]
    return wrapper
    
@dec_notfunc(5)
def foo(n):
    return n**2

print(foo)
