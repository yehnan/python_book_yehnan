

def caesar_dict(n):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    result = {}
    for i, e in enumerate(alphabet_lower):
        i = (i + n) % len(alphabet_lower)
        result[e] = alphabet_lower[i]
        
    for i, e in enumerate(alphabet_upper):
        i = (i + n) % len(alphabet_upper)
        result[e] = alphabet_upper[i]
    
    return result
    

if __name__ == '__main__':
    print(caesar_dict(13))
