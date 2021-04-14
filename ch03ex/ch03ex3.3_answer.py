

def f(n):
    if n < 10:
        if n == 9 or n == 6 or n == 3:
            return True
        else:
            return False
    else:
        result = 0
        while n > 0:
            result += n % 10
            n //= 10
        return f(result)


if __name__ == '__main__':
    # simple tests
    if f(9) != True:
        print('Failed')
    if f(37524) != True:
        print('Failed')
    if f(21) != True:
        print('Failed')
    if f(18) != True:
        print('Failed')
    if f(4) != False:
        print('Failed')
