

def int_from(n, inc=1):
    while True:
        yield n
        n += inc

ix = int_from(1)
iy = int_from(100, -2)

for i in range(5):
    print(next(ix))
    print(next(iy))

