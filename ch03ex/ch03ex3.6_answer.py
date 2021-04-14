

def is_1089(n):
    nabc = n
    ncba = int(str(nabc)[::-1])
    ndef = abs(nabc - ncba)
    nfed = int(str(ndef)[::-1])
    return (ndef + nfed) == 1089
    
if __name__ == '__main__':
    # simple test
    if is_1089(732) != True:
        print('Failed: 732')
    if is_1089(654) != True:
        print('Failed: 654')
    if is_1089(123) != True:
        print('Failed: 123')
        
    # test all 3-digit numbers
    for x in range(1, 9+1):
        for y in range(0, 9+1):
            for z in range(0, 9+1):
                n = x*100 + y*10 + z
                if is_1089(n) != (abs(x - z) >= 2):
                    print('Failed: %d' % n);

