

from abc import ABCMeta, abstractmethod

class S(metaclass=ABCMeta):
    # __metaclass__ = ABCMeta
    @abstractmethod
    def method_1(self, arg1): pass
    def method_2(self, arg1, arg2): pass

# s = S()

class Sub(S):
    def method_1(self, arg1):
        print(arg1)
    def method_2(self, arg1, arg2):
        print(arg1, arg2)

s = Sub()
s.method_1(3)
s.method_2(3, 4)

