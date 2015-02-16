

class MyClass():
    x, y = 3, 4
    def foo(self):
        print(x + y)
    def bar(self):
        print(self.x + self.y)
MyClass().foo()
MyClass().bar()
