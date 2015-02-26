

def is_anagram(s1, s2):
    s1 = ''.join(s1.lower().split())
    s2 = ''.join(s2.lower().split())
    return sorted(s1) == sorted(s2)

# True
print(is_anagram('heart', 'earth'))
print(is_anagram('Torchwood', 'Doctor Who'))
print(is_anagram('spot', 'stop'))
print(is_anagram('silent', 'listen'))
print(is_anagram('William Shakespeare', 'I am a weakish speller'))
print(is_anagram('computer', 'cuter mop'))
print(is_anagram('a b c  \t\n 1 2 3 \t\n ', '123abc\t\n'))
print('')
# False
print(is_anagram('abc', 'abd'))
print(is_anagram('play', 'pray'))
print(is_anagram('string', 'sting'))

