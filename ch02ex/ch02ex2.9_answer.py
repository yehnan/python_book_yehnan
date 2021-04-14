

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def f(n):
    fact = factorial(n)
    result = 0
    while fact > 0:
        result += fact % 10
        fact //= 10
    
    return result

if __name__ == '__main__':
    # simple tests
    n_fn = ((1, 1), (2, 2), (3, 6), (4, 6), (5, 3),
            (6, 9), (7, 9), (8, 9), (9, 27), (10, 27))

    for n, fn in n_fn:
        if fn != f(n):
            print('Failed:')
            print('summation of digits of %d! should be %d, not %d' % (n, fn, f(n)))

