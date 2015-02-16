

def powerset(s):
    li = list(s)
    ps = set()
    for n in range(0, 2**len(s)):
        sub = set()
        x = n
        for i in range(len(s)):
            if x & 0x1:
                sub.add(li[i])
            x >>= 1
        ps.add(frozenset(sub))
    return ps
####

def powerset_r(iterable):
    def set_add(ps, item):
        if len(ps) == 0:
            return []
        else:
            return [ps[0] + [item]] + set_add(ps[1:], item)
    def sub(s):
        if len(s) == 1:
            return [s, []]
        else:
            ps = sub(s[1:])
            return ps + set_add(ps, s[0])
    return sub(list(iterable))

test = [1,2,3,4]
print(powerset(test))
print(sorted(powerset_r(test), key=lambda x: len(x)))

