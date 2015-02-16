
import functools

def dec(func):
    @functools.wraps(func)
    def wrapper():
        return func()
    return wrapper
    
@dec
def foo():
    pass

print(foo.__name__)

