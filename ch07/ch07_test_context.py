

from __future__ import print_function
from io import open

with open('test.txt') as fin:
    for line in fin:
        print(line, end='')

####
with open('test.txt', 'r') as fin:
    with open('testw.txt', 'w') as fout:
        for line in fin:
            print(line, end='')
            fout.write(line)

####
with open('test.txt', 'r') as fin, open('testw.txt', 'w') as fout:
    for line in fin:
        print(line, end='')
        fout.write(line)



