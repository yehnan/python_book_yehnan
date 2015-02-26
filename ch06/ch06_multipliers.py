

def make_multipliers():
    result = []
    for i in range(3):
        def m(x):
            return i * x
        result.append(m)
    return result
for m in make_multipliers():
    print(m(5))
print('-' * 20)

def make_multipliers():
    result = []
    for i in range(3):
        m = lambda x: i * x
        result.append(m)
    return result
for m in make_multipliers():
    print(m(5))
print('-' * 20)

def make_multipliers():
    return [lambda x: i*x for i in range(3)]
for m in make_multipliers():
    print(m(5))
print('-' * 20)

def make_multipliers():
    result = []
    for i in range(3):
        m = lambda x, y=i: y * x
        result.append(m)
    return result
for m in make_multipliers():
    print(m(5))
print('-' * 20)
for m in [lambda x, n=n: n*x for n in range(3)]:
    print(m(5))
print('-' * 20)
