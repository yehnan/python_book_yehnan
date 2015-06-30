

import math

def is_cardano(a, b, c):
    return (8*a*a*a + 15*a*a + 6*a - 1) == 27*b*b*c
    
def main():
    count = 0
    for a in range(1, 1000-1-1 + 1):
        for b in range(1, 1000-a-1 + 1):
            for c in range(1, 1000-a-b + 1):
                if is_cardano(a, b, c):
                    count += 1
                    print(a, b, c)
    print('Total: %d' % count)
    return count
                
if __name__ == '__main__':
    # simple test
    if is_cardano(2, 1, 5) == False:
        print('Failed: (2, 1, 5) should be a Cardano Triple')
    if main() != 149:
        print('Failed: should be 149')
    