

class Frange():
    def __init__(self, start, stop=None, step=None):
        self.start = start + 0.0
        self.stop = stop
        self.step = step
        if self.stop is None:
            self.stop = self.start + 0.0
            self.start = 0.0
        if self.step is None:
            self.step = 1.0
    def __iter__(self):
        return self
    def __next__(self):
        next = self.start
        self.start += self.step
        if abs(next) < abs(self.stop):
            return next
        else:
            raise StopIteration

for x in Frange(3):
    print(x)
print([i for i in Frange(2.55, 3.7, 0.1)])
print([i for i in Frange(0, 1, 0.1)])
