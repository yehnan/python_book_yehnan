

a = 26
b = 16

import mymath

def main():
    print('Hello Python')
    print('pi is ' + str(mymath.pi))
    print('gcd(%d, %d) is %d' % (a, b, mymath.gcd(a, b)))
    print('factorial(%d) is %d' % (6, mymath.factorial(6)))
    print('Bye Python')

if __name__ == '__main__':
    print('%s as main program' % __name__)
    print('mymath.__name__ is %s ' % mymath.__name__)
    main()


    