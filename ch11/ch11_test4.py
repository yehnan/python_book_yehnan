

class MyC():
    def __init__(self):
        self.x = 3
        self.y = 4
    def __hash__(self):
        return 100
a = MyC()
b = MyC()
print(hash(a))
print(hash(b))

from collections import Hashable

print(issubclass(MyC, Hashable))


