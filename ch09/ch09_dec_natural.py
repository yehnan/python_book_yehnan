

def dec_natural(func):
    def wrapper(n):
        if type(n) == int and n >= 0:
            return func(n)
        else:
            raise TypeError('Argument is not a natural number')
    return wrapper
    
@dec_natural
def fact_i(n):
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result

print(fact_i(3))
# print(fact_i(-1))
