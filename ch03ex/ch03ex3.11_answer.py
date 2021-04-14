

from math import log2, ceil

def f(a, b):
    bit_n = ceil(log2(max(a, b)))
    count = 0
    for i in range(bit_n):
        if (a ^ b) & (0x1 << i):
            count += 1
    return count


if __name__ == "__main__":
    if f(31, 14) != 2:
        print('Failed: f(31, 14) should be 2')

    if f(0b11110000, 0b00001111) != 8:
        print('Failed: f(0b11110000, 0b00001111) should be 8')

