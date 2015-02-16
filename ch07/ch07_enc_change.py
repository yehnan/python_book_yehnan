
# -*- coding: utf-8 -*-
from io import open

def enc_change(file_in, enc_in, file_out, enc_out):
    with open(file_in, mode='r', encoding=enc_in) as fin:
        with open(file_out, mode='w', encoding=enc_out) as fout:
            for line in fin:
                fout.write(line)



enc_change('test_big5.txt', 'big5', 'test_utf8.txt', 'utf8')
