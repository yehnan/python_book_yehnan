

def my_sum(iterable, start=0):
    result = start
    for x in iterable:
        result += x
    return result

a = ('a', 'b', 'c', 'd')
b = range(1, 10+1)
c = ['abc', 'def', 'gh', 'i']
print(my_sum(a, ''))
print(my_sum(b))
print(my_sum(c, ''))
