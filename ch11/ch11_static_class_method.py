

class MyClass():
    @staticmethod
    def foo(arg1, arg2): print(arg1, arg2)
    @classmethod
    def bar(cls, arg1): print(cls, arg1)
MyClass.foo(3, 4)
MyClass.bar(5)







