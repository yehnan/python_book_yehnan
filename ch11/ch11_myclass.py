

class Person():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

# p1 = Person()
p2 = Person('John', 22, 170, 60)
p3 = Person('Amy', 17, 160, 42)


class Book():
    def __init__(self, title, cover_price, discount=1.0):
        self.title = title
        self.cover_price = cover_price
        self.discount = discount
    def get_title(self): return self.title
    def get_cover_price(self): return self.cover_price
    def get_discount(self): return self.discount
    def set_discount(self, discount): self.discount = discount
    def get_price(self): return int(self.cover_price * self.discount)
    
b1 = Book('Make Wishes', 300)
b2 = Book('Fun of cooking', 500, 0.79)
print(b2.get_price())
print('-' * 20)

class MyClass():
    x, y, z = 3, 4, 5
    def sfoo(): 
        # print(z)
        print(MyClass.z)
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def foo(self): print(self.x + self.z)
    def bar(self): 
        # print(self.y - z)
        print(self.y - MyClass.z)

c0 = MyClass(33, 44)
MyClass.sfoo()   # 5
# c0.sfoo()
c0.foo() # 38
c0.bar() # 39


