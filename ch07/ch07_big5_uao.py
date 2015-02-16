
# -*- coding: utf-8 -*-
from __future__ import print_function
import codecs
# import big5uao
import big5uao_3

# a煊b喆c凜凛
test = b'a\x95\x4Fb\x95\xEDc\xBB\xFE\x81\x60'

dec = codecs.getdecoder('big5uao')
enc = codecs.getencoder('big5uao')

d0, d1 = dec(test)
print(d0, d1)

test = b'\x95\x4F\x80\x80'
d0, d1 = dec(test, errors='replace')
print(d0, d1)

# 應是Big5+UAO的 0xa7 0x41 0xa6 0x6e
s = '你好'       # 2.x u'你好'      3.x '你好'

e = enc(s)
for b in e[0]:
    print('%x ' % b, end='')
print(e[1])

s = '\uEEEE\uDDDD'
e = enc(s, errors='strict')
for b in e[0]:
    print('%x ' % b, end='')
print(e[1])
