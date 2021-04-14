

def main(words):
    d = {}
    for w in words:
        ws = ''.join(sorted(w)) ## not use set or hash
        if ws not in d:
            d[ws] = [w]
        else:
            d[ws].append(w)
    return list(d.values())

data = ['eat', 'ate', 'done', 'tea', 
        'opus', 'soup', 'node', 'quick']
print(main(data))

# [['eat', 'ate', 'tea'], ['done', 'node'], ['opus', 'soup'], ['quick']]

