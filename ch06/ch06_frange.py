

def frange_g(start, end=None, inc=None):
    if end is None:
        end = start
        start = 0.0
    if inc is None:
        inc = 0.1
    while True:
        if inc > 0 and start >= end:
            break
        elif inc < 0 and start <= end:
            break
        yield start
        start += inc

for i in frange_g(0, -1, -0.1):
    print(i)



