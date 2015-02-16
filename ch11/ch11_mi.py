
class S():
    def foo(self): pass
class A(S):
    def foo(self): print('A foo')
class B(S):
    def foo(self): print('B foo')
class C(A, B):
    pass
C().foo()



