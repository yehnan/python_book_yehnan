

class Animal():
    def shout(self): print('Animal shout')
class Dog(Animal):
    def shout(self): print('Dog shout')
class Cat(Animal):
    def shout(self): print('Cat shout')
    def __str__(self): return 'I am a cat'
        
d = Dog(); d.shout()
c = Cat(); c.shout()
print(c)

class MyClass():
    def __str__(self): return 'a MyClass instance'
mc = MyClass()
print(str(mc))
print(mc)
   

