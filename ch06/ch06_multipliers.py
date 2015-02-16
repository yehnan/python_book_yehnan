

def makeMultipliers():
    result = []
    for i in range(3):
        def m(x):
            return i * x
        result.append(m)
    return result
for m in makeMultipliers():
    print(m(5))
print('-' * 20)

def makeMultipliers():
    result = []
    for i in range(3):
        m = lambda x: i * x
        result.append(m)
    return result
for m in makeMultipliers():
    print(m(5))
print('-' * 20)

def makeMultipliers():
    return [lambda x: i*x for i in range(3)]
for m in makeMultipliers():
    print(m(5))
print('-' * 20)

def makeMultipliers():
    result = []
    for i in range(3):
        m = lambda x, y=i: y * x
        result.append(m)
    return result
for m in makeMultipliers():
    print(m(5))
print('-' * 20)
for m in [lambda x, n=n: n*x for n in range(3)]:
    print(m(5))
print('-' * 20)
