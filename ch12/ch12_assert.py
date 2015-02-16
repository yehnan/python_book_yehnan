


def fact(n):
    assert type(n) is int
    assert n < 0
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result



