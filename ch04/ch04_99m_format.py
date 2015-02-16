
def p99(li):
    for y in range(1, 9+1):
        result = []
        for x in li:
            s = '%2d x%2d = %2d' % (x, y, x*y)
            result.append(s)
        print('  '.join(result))

p99([2, 3, 4, 5])
print('')
p99([6, 7, 8, 9])

