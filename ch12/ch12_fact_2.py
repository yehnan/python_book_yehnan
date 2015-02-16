

def fact(n):
    if type(n) is not int or n < 0:
        return None
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result

while True:
    s = input('input n: ')
    f = fact(int(s))
    if f is not None:
        print('%s! = %d' % (s, f))
    else:
        print('n must be a non-negative integer')


