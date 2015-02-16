

def fact_i(n):
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result
####
def fact_r(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact_r(n-1)
####
def fact_r_tail(n, result=1):
    if n == 1 or n == 0:
        return result
    else:
        return fact_r_tail(n-1, n*result)

for i in range(2, 50):
    x = fact_i(i)
    y = fact_r(i)
    z = fact_r_tail(i)
    if x == y == z:
        pass
    else:
        print('error')

