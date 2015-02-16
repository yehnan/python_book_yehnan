

class A():
    x = 3
    def __init__(self):
        self.x = 33

    
class B(A):
    x = 4
    def __init__(self):
        super().__init__()
        self.z = 1000
b = B()
print(b.x)
