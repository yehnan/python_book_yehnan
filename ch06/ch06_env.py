


def fact(n):
    if n <= 1:
        return n
    else:
        return n * fact(n-1)

print(fact(3))

def counter(n):
    li = [n]
    def bar(x):
        li[0] += x
        return li[0]
    return bar

c0 = counter(0)
c100 = counter(100)
print(c0(1))
print(c100(10))
print(c0(1))
print(c0(3))
print(c100(20))


