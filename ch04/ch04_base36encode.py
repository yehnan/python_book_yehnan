

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def base36encode(number, alphabet=alphabet):
    result = []
    base = len(alphabet)
    sign = ''
    if number < 0:
        sign = '-'
        number = -number
        
    while number >= base:
        number, i = divmod(number, base)
        result.append(alphabet[i])
    result.append(alphabet[number])
    if sign == '-':
        result.append(sign)
        
    return ''.join(reversed(result))

print(base36encode(int('0', 36)))
print(base36encode(int('ZZ', 36)))
print(base36encode(int('ZYXW', 36)))
print(base36encode(int('-ABCDEF', 36)))
print(base36encode(int('-GHIJKLMNOPQ', 36)))


