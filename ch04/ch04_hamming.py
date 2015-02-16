

def hamming(s1, s2):
    lens = (len(s1), len(s2))
    minlen = min(lens)
    maxlen = max(lens)
    h = maxlen - minlen

    for i in range(minlen):
        if(s1[i] != s2[i]):
            h += 1
    
    return h

print(hamming('abcde', 'edcba')) # 4
print(hamming('abc', 'abcde')) # 2
print(hamming('1011101', '1001001')) # 2
print(hamming('karolin', 'kathrin')) # 3

