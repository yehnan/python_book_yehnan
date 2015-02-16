
# -*- coding: utf-8 -*-

from __future__ import print_function
from io import open
import struct

with open ('test.bin', 'rb') as fin:
    a = struct.unpack('<cxxx', fin.read(4))
    print(a)
    b = struct.unpack('<L', fin.read(4))
    print(hex(b[0]))
    c, d = struct.unpack('<if', fin.read(8))
    print(c)
    print(d)
    e, f = struct.unpack('<cxxxxxxxd', fin.read(16))
    print(e)
    print(f)
