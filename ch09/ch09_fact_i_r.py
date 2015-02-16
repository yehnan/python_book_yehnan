

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

print(fact_i(999))
print(fact_r(999))


