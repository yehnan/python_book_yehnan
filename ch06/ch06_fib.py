

def fib_r(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r(n-1) + fib_r(n-2)
####
def fib_i(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
####
memo = {0: 0, 1: 1}
def fib_m(n):
    if n not in memo: 
        memo[n] = fib_m(n-1) + fib_m(n-2) 
    return memo[n]

for x in range(20):
    fr = fib_r(x)
    fi = fib_i(x)
    fm = fib_m(x)
    if fr != fi or fi != fm:
        print('error: fib(%d) %d %d %d' % (x, fr, fi, fm))


