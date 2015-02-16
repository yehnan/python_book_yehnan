
# -*- coding: utf-8 -*-
from __future__ import print_function
from io import open
import sys

with open('test.txt', 'w', encoding='utf-8') as fout:
    stdout_backup = sys.stdout
    sys.stdout = fout
    print(u'Hello Python')
    sys.stdout = stdout_backup

