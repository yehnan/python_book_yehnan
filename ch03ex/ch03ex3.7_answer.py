

import math

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
def factorial_stirling(n):
    return math.sqrt(2 * math.pi * n) * pow(float(n) / math.e, n)
    
if __name__ == '__main__':
    # simple test
    for n in range(2, 30):
        nf = factorial(n)
        nfs = factorial_stirling(n)
        error = (nfs - nf) / nf
        tolerance = 0.1
        if error >= tolerance:
            print('%d! = %d, stirling: %f' % (n, nf, nfs))
            print('error: %f' % ((nfs - nf) / nf))
