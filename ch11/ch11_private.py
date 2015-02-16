

class A():
    def bar(self): return 4
    def foo(self): return 3 + self.bar()
class B(A):
    def bar(self): return 104

b = B()
print(b.foo())

class A():
    def __bar(self): return 4
    def foo(self): return 3 + self.__bar()
class B(A):
    def bar(self): return 104
    def bm(self): return self.bar() + 1000

b = B()
print(b.foo())
print(b.bm())
print(b._A__bar())


