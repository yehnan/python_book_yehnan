

def fact(n):
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result

while True:
    s = input('input n: ')
    f = fact(int(s))
    print('%s! = %d' % (s, f))

