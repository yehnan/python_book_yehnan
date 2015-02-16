
def range_g(start, end=None, inc=None):
    if end is None:
        end = start
        start = 0
    if inc is None:
        inc = 1
    while True:
        if inc > 0 and start >= end:
            break
        elif inc < 0 and start <= end:
            break
        yield start
        start += inc

def range2x(start, end=None, inc=None):
    if end is None:
        end = start
        start = 0
    if inc is None:
        inc = 1
    result = []
    while True:
        if inc > 0 and start >= end:
            break
        elif inc < 0 and start <= end:
            break
        result.append(start)
        start += inc
    return result

# not work
def range3x(start, end=None, inc=None):
    if end is None:
        end = start
        start = 0
    if inc is None:
        inc = 1
    s = [start]
    def sub():
        while s[0] < end:
            if inc > 0 and s[0] >= end:
                break
            elif inc < 0 and s[0] <= end:
                break
            s[0] += inc
            return (s[0] - inc)
    return sub

if __name__ == '__main__':
    tests = (0, 10, 30, -100, 1, 2)
    for a in tests:
        x0 = list(range(a))
        x1 = range2x(a)
        x2 = list(range_g(a))
        if x0 != x1 or x0 != x2:
            print('error')
    tests = ((0, 10), (10, 30), (-100, 20), (1, 2))
    for a,b in tests:
        x0 = list(range(a, b))
        x1 = range2x(a, b)
        x2 = list(range_g(a, b))
        if x0 != x1 or x0 != x2:
            print('error')
    tests = ((0, 10, 1), (10, 30, 2), (-10, -20, -1), (0, -31, -3))
    for a,b,c in tests:
        x0 = list(range(a, b, c))
        x1 = range2x(a, b, c)
        x2 = list(range_g(a, b, c))
        if x0 != x1 or x0 != x2:
            print('error %s %s' % (x0, x1))
    # xx = range3x(10, -3, -1)
    # for i in range(20):
        # print(xx())


