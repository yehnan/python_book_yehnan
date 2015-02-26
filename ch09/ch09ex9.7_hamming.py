

def hamming(a, b):
    return sum(x != y for x, y in map(None, a, b))



