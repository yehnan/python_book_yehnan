

def fib_i(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
####
def fib_memo():
    memo = {0: 0, 1: 1}
    def sub(n):
        if n not in memo: 
            memo[n] = sub(n-1) + sub(n-2) 
        return memo[n]
    return sub
fib_m = fib_memo()

for x in range(30):
    fi = fib_i(x)
    fm = fib_m(x)
    if fi != fm:
        print('error: fib(%d) %d %d' % (x, fi, fm))

