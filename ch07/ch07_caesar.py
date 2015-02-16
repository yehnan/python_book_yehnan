
# -*- coding: utf-8 -*-
from io import open
import string

# 回傳轉換表，shift是偏移量，可正可負，encrypt代表要加密還是解密
def caesar_table(shift, encrypt=True):
    lowers = string.ascii_lowercase    # 小寫英文字母
    uppers = string.ascii_uppercase    # 大寫英文字母
    lowers_new = lowers[shift:] + lowers[:shift]
    uppers_new = uppers[shift:] + uppers[:shift]
    # 若是2.x版，請把str.maketrans改成string.maketrans
    # maketrans的功能是製作轉換表，供str.translate使用
    if encrypt:
        return str.maketrans(lowers+uppers, lowers_new+uppers_new)
    else:
        return str.maketrans(lowers_new+uppers_new, lowers+uppers)
# 凱撒密碼，shift是偏移量，encrypt代表要加密還是解密
def caesar(file_in, file_out, shift, encrypt=True):
    table = caesar_table(shift, encrypt)
    with open(file_in, mode='r', encoding='ascii') as fin:
        with open(file_out, mode='w', encoding='ascii') as fout:
            for line in fin:
                # 呼叫translate，傳入轉換表
                fout.write(line.translate(table))
                
caesar('test.txt', 'encrypt.txt', 3, True)
caesar('encrypt.txt', 'decrypt.txt', 3, False)

