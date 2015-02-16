
# -*- coding: utf-8 -*-
# 你好
from __future__ import print_function
from io import open

print('你好Python')
with open('ch07_print_self_utf8.py', encoding='utf8') as fin:
    for line in fin:
        print(line, end='')
print('再見Python')
