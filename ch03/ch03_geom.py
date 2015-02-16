
def geomean(numbers):
    product = 1
    for n in numbers:
        product *= n
    return product ** (1.0 / len(numbers))

if __name__ == '__main__':
    a = list(range(1, 10+1))
    gm = geomean(a)
    print(gm)

