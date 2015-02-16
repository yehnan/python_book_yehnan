

def fib_gf():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
fib_g = fib_gf()

def fib_memo():
    memo = {0: 0, 1: 1}
    def sub(n):
        if n not in memo: 
            memo[n] = sub(n-1) + sub(n-2) 
        return memo[n]
    return sub
fib_m = fib_memo()

for x in range(40):
    fg = next(fib_g)
    fm = fib_m(x)
    if fg != fm:
        print('error: fib(%d) %d %d' % (x, fg, fm))

