

#### powerset, all subsets of a set ####
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


