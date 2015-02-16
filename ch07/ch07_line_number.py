
# -*- coding: utf-8 -*-
from io import open

# 計算文字檔有幾行
def line_count(filepath, enc='utf8'):
    count = 0
    with open(filepath, mode='r', encoding=enc) as fin:
        for line in fin:
            count += 1
    return count

# 計算文字檔有幾行，另一種作法
def line_count_2(filepath, enc='utf8'):
    return sum(1 for line in open(filepath, mode='r', encoding=enc))

# 為文字檔加上行號，參數：輸入檔路徑、輸出檔路徑、編碼
def line_number(fin_path, fout_path, enc='utf8'):
    lc = line_count(fin_path)      # 知道行數才能對齊
    lcw = len(str(lc))             # 該佔幾格
    with open(fin_path, mode='r', encoding=enc) as fin:
        with open(fout_path, mode='w', encoding=enc) as fout:
            for i, line in enumerate(fin):
                fout.write(u'{:0{width}d} {}'.format(i+1, line, width=lcw))

