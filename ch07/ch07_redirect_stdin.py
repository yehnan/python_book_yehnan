
# -*- coding: utf-8 -*-
from __future__ import print_function
from io import open
import sys

with open('stdin_test.txt', 'r', encoding='utf8') as fin:
    stdin_backup = sys.stdin
    sys.stdin = fin
    while True:
        try:
            name = input()     # 2.xª©¶·¨Ï¥Îraw_input()
            print('Hello ' + name)
        except:
            break
    sys.stdin = stdin_backup




