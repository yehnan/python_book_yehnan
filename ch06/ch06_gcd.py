

def gcd_i(a, b): 
    while b:
        a, b = b, a%b
    return a
####
def gcd_r(a, b):
    if b == 0:
        return a
    else:
        return gcd_r(b, a%b)

if __name__ == '__main__':
    for a in range(1, 100):
        for b in range(1, 100):
            x = gcd_i(a, b)
            y = gcd_r(a, b)
            if x != y:
                print('error: gcd(%d,%d), %d, %d' % (a, b, x, y))