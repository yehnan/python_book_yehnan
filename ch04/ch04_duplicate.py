

def duplicate(iterable):
    fst = []
    snd = []
    for x in iterable:
        if x not in fst:
            fst.append(x)
        elif x not in snd:
            snd.append(x)
        else:
            pass
    return snd
        
print(duplicate([1, 2, 6, 1, 3, 2, 5]))
print(duplicate(range(10)))
print(duplicate([1, 1, 3, 1, 3, 3, 1, 2, 1, 5, 2]))



