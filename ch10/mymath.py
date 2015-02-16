

pi = 3.14

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

if __name__ == '__main__':
    print('%s as main program' % __name__)


