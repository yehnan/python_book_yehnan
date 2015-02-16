

class FromNtoM():
    def __init__(self, n, m):
        self.n = n
        self.m = m
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.m:
            tmp, self.n = self.n, self.n+1
            return tmp
        else:
            raise StopIteration

print(sum(FromNtoM(1, 100+1)))
print(sum(range(1, 100+1)))


