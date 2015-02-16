

def foo():
    x = 3
    def bar():
        print(x)
    bar()
foo()

class MyClass():
    x = 3
    def foo():
        print(x)
    def bar(self):
        # print(x)
        print(self.x)
# MyClass.foo()
MyClass().bar()
