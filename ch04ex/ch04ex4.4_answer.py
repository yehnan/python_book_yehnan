

s = 'abcde'
print(s)

sr0 = ''.join(reversed(s))
print(sr0)         # edcba, ok

sr1 = s[::-1]
print(sr1)         # edcba, ok

sr2 = s[-1:0:-1]
print(sr2)         # edcb, not ok

sr3 = s[-1::-1]
print(sr3)         # edcba, ok


        