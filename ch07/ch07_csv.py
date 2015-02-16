
# -*- coding: utf-8 -*-
# Python 3.x
import csv

with open('csv.txt', 'r', encoding='utf-8') as fin:
    with open('csv_out.txt', 'w', encoding='utf-8') as fout:
        csvreader = csv.reader(fin, delimiter=',')
        csvwriter = csv.writer(fout, delimiter=' ')
        header = next(csvreader)
        csvwriter.writerow(header)
        for row in csvreader:
            row[0] = row[0].replace('/', '-')
            row[-1] += '%'
            print(','.join(row))
            csvwriter.writerow(row)


