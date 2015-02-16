

def product(iterable, start=1):
    result = start
    for x in iterable:
        result *= x
    return result

a = range(1, 10+1)
b = [2, 3, 4, 5]
c = [1.1, 3.5, 5.6]
print(product(a, 0.1))
print(product(b))
print(product(c))
