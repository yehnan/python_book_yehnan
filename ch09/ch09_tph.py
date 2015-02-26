

# Problem 45: Triangular, pentagonal, and hexagonal
# https://projecteuler.net/problem=45

from itertools import count
from itertools import imap as map

def filter_equal(ita, itb):
    a = next(ita)
    b = next(itb)
    while True:
        if a < b:
            a = next(ita)
        elif a > b:
            b = next(itb)
        else:
            yield a
            a = next(ita)

def tph_gf():
    t = map(lambda n: n * (n+1) // 2, count(1))
    p = map(lambda n: n * (3*n - 1) // 2, count(1))
    h = map(lambda n: n * (2*n - 1), count(1))
    filter_tph = filter_equal(filter_equal(t, p), h)
    while True:
        yield next(filter_tph)

tph = tph_gf()
print(next(tph))  # 1
print(next(tph))  # 40755
print(next(tph))  # 1533776805
