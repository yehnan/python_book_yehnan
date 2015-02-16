
# -*- coding: utf-8 -*-
from __future__ import print_function
import codecs
import big5ext
import big5uao

def getregentry(codec_name):
    if codec_name == 'big5ext':
        return codecs.CodecInfo(
        name='big5ext',
        encode=big5ext.Codec().encode,
        decode=big5ext.Codec().decode,
        incrementalencoder=big5ext.IncrementalEncoder,
        incrementaldecoder=big5ext.IncrementalDecoder,
        streamreader=big5ext.StreamReader,
        streamwriter=big5ext.StreamWriter,
        )
    elif codec_name == 'big5uao':
        return codecs.CodecInfo(
        name='big5uao',
        encode=big5uao.Codec().encode,
        decode=big5uao.Codec().decode,
        incrementalencoder=big5uao.IncrementalEncoder,
        incrementaldecoder=big5uao.IncrementalDecoder,
        streamreader=big5uao.StreamReader,
        streamwriter=big5uao.StreamWriter,
        )

codecs.register(getregentry) 	

#################
print(codecs.lookup('big5uao'))
print(codecs.lookup('big5ext'))


test = b'a\x95\x4Fb\x95\xEDc\xBB\xFE\x81\x60'
print(len(test))
dec1 = codecs.getdecoder('big5ext')
dec2 = codecs.getdecoder('big5uao')

d1 = dec1(test)
d2 = dec2(test)
print(d1[0], d1[1])
print(d2[0], d2[1])

for b1 in range(0x81, 0xFE+1):
    for b2 in range(0x40, 0x7E+1):
        big5 = chr(b1) + chr(b2)
        d1 = dec1(big5)
        d2 = dec2(big5)
        if d1[0] != d2[0]:
            print(d1, d2)
    for b2 in range(0xA1, 0xFE+1):
        big5 = chr(b1) + chr(b2)
        d1 = dec1(big5)
        d2 = dec2(big5)
        if d1[0] != d2[0]:
            print(d1, d2)

ss = u'你好'       # a7 41   a6 6e
enc2 = codecs.getencoder('big5uao')
e2 = enc2(ss)
for b in e2[0]:
    print('%x ' % ord(b), end='')
print(e2[1])

