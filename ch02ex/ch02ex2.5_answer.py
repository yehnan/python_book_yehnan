

def f(x, y, z):
    if x >= y:
        if y >= z:     # x y z
            return x**2 + y**2
        else:          # x z y
            return x**2 + z**2
    else:
        if x >= z:     # y x z
            return y**2 + x**2
        else:          # y z x
            return y**2 + z**2


if __name__ == '__main__':
    # simple tests
    if f(1, 2, 3) != (2**2 + 3**2):
        print('Failed')
    if f(5, 3, 4) != (5**2 + 4**2):
        print('Failed')
    if f(9, 11, 10) != (11**2 + 10**2):
        print('Failed')

