

# A B C D... Z  AA AB   AZ BA
# 1          26 27 28   52 53
# note: there is no  zero

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
base = len(alphabet)

# from int to str, number must >= 1
def base26encode(number): 
    result = []
    while number-1 >= base:
        number, i = divmod(number-1, base)
        result.append(alphabet[i])
    result.append(alphabet[number-1])
    
    return ''.join(reversed(result))

# from str to int, 'A', 'B', ...'Z', 'AA', ...'AZ', ...
def base26decode(s): 
    s = s.upper()
    number = 0
    for n in s:
        number *= base
        number += alphabet.index(n) + 1
    return number

print('a ', base26decode('a'))
print(base26encode(base26decode('a') + 1))
print('b ', base26decode('b'))
print(base26encode(base26decode('b') + 1))
print('aa ', base26decode('aa'))
print(base26encode(base26decode('aa') + 1))
print('ab ', base26decode('ab'))
print(base26encode(base26decode('ab') + 1))
print('z ', base26decode('z'))
print(base26encode(base26decode('z') + 1))
print('az ', base26decode('az'))
print(base26encode(base26decode('az') + 1))
print('ba ', base26decode('ba'))
print(base26encode(base26decode('ba') + 1))
print('bz ', base26decode('bz'))
print(base26encode(base26decode('bz') + 1))
print('zz ', base26decode('zz'))
print(base26encode(base26decode('zz') + 1))
print('bzz ', base26decode('bzz'))
print(base26encode(base26decode('bzz') + 1))
print('------')
print('-' * 40)


