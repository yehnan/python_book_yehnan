
# -*- coding: utf-8 -*-
from io import open
import os
import os.path

# 計算文字檔有幾行
def line_count(filepath, enc='utf8'):
    count = 0
    with open(filepath, mode='r', encoding=enc) as fin:
        for line in fin:
            if line.strip():       # 空白行不算
                count += 1
    return count
# 判斷文字編碼系統，從檔案開頭的前幾個位元組
def what_encoding_by_head(filepath):
    enc = None
    with open(filepath, 'rb') as fin:
        data = fin.read(3)
        if len(data) == 3:       # Windows會在UTF-8檔案開頭加上BOM
            if data[0] == 0xEF and data[1] == 0xBB and data[2] == 0xBF:
                enc = 'utf8'
        if len(data) >= 2:       # UTF-16 BE與LE
            if data[0] == 0xFE and data[1] == 0xFF:
                enc = 'UTF-16BE'
            elif data[0] == 0xFF and data[1] == 0xFE:
                enc = 'UTF-16LE'
    return enc
# 判斷文字編碼系統，從第一行或第二行，若含有'coding'字樣的話
def what_encoding_by_mark(filepath):
    enc = 'ascii'            # 預設為ASCII
    mark = 'coding'          # 編碼標記字樣
    def extract_enc(line):
        chars = ' :=-*'      # 編碼標記字樣周圍無用的字元
        return line.strip().lstrip(chars).rstrip(chars)
    with open(filepath, mode='r', encoding=enc, errors='ignore') as fin:
        for i in range(2):         # 只讀兩行
            line = fin.readline()
            idx = line.find(mark)  # 若含有編碼標記字樣
            if idx != -1:
                enc = extract_enc(line[idx+len(mark):])
                break
    return enc
# 判斷文字編碼系統
def what_encoding(filepath):
    return what_encoding_by_head(filepath) or what_encoding_by_mark(filepath)

lc_total = 0         # 總行數
file_count = 0       # 被計算行數的檔案個數
for p in os.listdir('.'):      # 2.x版應使用u'.'
    if os.path.isfile(p) and p[-3:] == '.py':
        try:
            enc = what_encoding(p)
            lc = line_count(p, enc)
            lc_total += lc
            file_count += 1
            print(p, enc, lc)
        except:
            print(p, "can't count lines")

print('%d .py files totally have %d lines ' % (file_count, lc_total))

