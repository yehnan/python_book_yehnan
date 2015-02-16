

from math import sqrt
from random import randint

def estimate_pi(n):
    N = 10**100
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    def montecarlo(n, experiment):
        passed = 0
        for i in range(n):
            if experiment():
                passed += 1
        return float(passed) / n
    def cesaro():
        return gcd(randint(1, N), randint(1, N)) == 1
    return sqrt(6.0 / montecarlo(n, cesaro))

if __name__ == '__main__':
    for i in range(10, 101, 10):
        print(estimate_pi(i))




