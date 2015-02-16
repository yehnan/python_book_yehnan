

class A():
    x, y = 3, 4
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def foo(self):
        print(self.a + self.b + self.x + self.y)
class B(A):
    ww = 1000
    x = 1003
    def bar(self):
        self.foo()
        print(self.x + self.ww)

a0 = A(13, 14)
a0.foo()
b0 = B(103, 104)
b0.foo()
b0.bar()

