

from __future__ import print_function
from io import open 
from collections import namedtuple
import csv

with open('csv.txt', 'r', encoding='ascii') as fin:
    csvreader = csv.reader(fin, delimiter=',')
    header = next(csvreader)
    Data = namedtuple('Header', ','.join(header))
    for row in csvreader:
        d = Data._make(row)
        print(d.name, d.eng, d.history, d.math)


