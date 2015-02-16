

# Raymond Hettingers
# http://code.activestate.com/recipes/576647/
from itertools import permutations

def queen_gf(n):
    cols = range(n)
    for ans in permutations(cols):
        if (n == len(set(ans[i]+i for i in cols)) ==
                len(set(ans[i]-i for i in cols))):
            yield ans
