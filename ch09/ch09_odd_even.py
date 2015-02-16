

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)



if __name__ == '__main__':
    for i in range(0, 100):
        if is_odd(i) != (i%2 == 1):
            print('error odd', i)
        if is_even(i) != (i%2 == 0):
            print('error even', i)


