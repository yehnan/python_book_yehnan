
# -*- coding: utf-8 -*-
import big5uao
import codecs

enc_utf_16_be = codecs.getencoder('utf_16_be')
enc_big5uao = codecs.getencoder('big5uao')
enc_gbk = codecs.getencoder('gbk')

encs = (enc_utf_16_be, enc_big5uao, enc_gbk)

s = '煊喆凜凛遙遥阪坂齊斉齐齋斎榮荣栄富冨樫堅島嶋崎﨑邊边辺絕绝對对対涉澀渋瑠鹽塩盐汙污汚櫻桜鐮镰鎌高髙癡痴'

for c in s:
    fs = [c, ' ']
    for enc in encs:
        d, e = enc(c)
        x = '%02X%02X' % (d[0], d[1])
        fs.append(x)
        fs.append(' ')
    print(''.join(fs))
    

print(len(s))
