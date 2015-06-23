

def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return collatz(n // 2)
    else:
        return 3 * collatz(n) + 1

def collatz_i(n):
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return n

if __name__ == '__main__':
    for i in range(1, 10000+1):
        if collatz_i(i) != 1:
            print('collatz_i(' + str(i) + ') failed');
            break
    else:
        print('All passed')
        
        