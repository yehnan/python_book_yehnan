

def fg(n):
    for i in range(1, n):
        yield i
    for i in range(-1, -n, -1):
        yield i

print(list(fg(5)))

def sub_fg(n):
    i = 1 if n > 0 else -1
    inc = i
    while i != n:
        yield i
        i += inc
def fg(n):
    yield from sub_fg(n)
    yield from sub_fg(-n)

print(list(fg(5)))

def fg(n):
    yield from range(1, n)
    yield from range(-1, -n, -1)

print(list(fg(5)))
