

def isAnagram(s1, s2):
    s1 = ''.join(s1.lower().split())
    s2 = ''.join(s2.lower().split())
    return sorted(s1) == sorted(s2)

# True
print(isAnagram('heart', 'earth'))
print(isAnagram('Torchwood', 'Doctor Who'))
print(isAnagram('spot', 'stop'))
print(isAnagram('silent', 'listen'))
print(isAnagram('William Shakespeare', 'I am a weakish speller'))
print(isAnagram('computer', 'cuter mop'))
print(isAnagram('a b c  \t\n 1 2 3 \t\n ', '123abc\t\n'))
print('')
# False
print(isAnagram('abc', 'abd'))
print(isAnagram('play', 'pray'))
print(isAnagram('string', 'sting'))

