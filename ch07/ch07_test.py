
fin = open('test.txt')
print(fin.readline())
for line in fin:
    print(line)
fin.close()

####
fin = open('test.txt')
fout = open('testw.txt', 'w')
for line in fin:
    print(line)
    fout.write(line)
fin.close()
fout.close()

####



