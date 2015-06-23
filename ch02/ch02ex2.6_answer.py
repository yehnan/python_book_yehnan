

# greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# least common multiple
def lcm(a, b):
    x = gcd(a, b)
    return (a // x) * b
    
if __name__ == '__main__':
    # simple tests
    if lcm(7, 13) != 91:
        print('Failed')
    if lcm(100, 25) != 100:
        print('Failed')
    if lcm(16, 24) != 48:
        print('Failed')

