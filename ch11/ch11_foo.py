

class Foo(object):
    pass

Foo.pi = 3.14
print(Foo.pi)

def gcd(a, b): # Greatest Common Divisor
    while b:
        a, b = b, a%b
    return a

Foo.gcd = gcd
print(Foo.gcd)


class Bar():
    def __init__(self):
        self.x = 3
    def xxx():
        print('hello')
    def yyy(aa):
        print('hello', aa.x)
Bar.xxx()
b = Bar()
# b.xxx()
b.yyy()
