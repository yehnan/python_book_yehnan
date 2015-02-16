

from __future__ import print_function
from collections import Counter
from io import open

with open('i_have_a_dream.txt', 'r', encoding='ascii') as fin:
    c = Counter()
    for line in fin:
        if line[0] == '#':
            continue
        c.update(line.split())
    print(sorted(c.items(), key=lambda x: x[1]))
    
