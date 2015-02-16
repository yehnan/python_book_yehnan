#import mymath
#from mymath import pi, gcd, factorial
import mymath as m

print('Hello Python')
print('pi is ' + str(m.pi))
print('gcd of 24 and 16 is ' + str(m.gcd(24, 16)))
print('factorial of 6 is ' + str(m.factorial(6)))
print('Bye Python')

if __name__ == '__main__':
    print('myhello as main program')
else:
    print('myhello as module')

