
# -*- coding: utf-8 -*-
from __future__ import print_function
from io import open
import json

with open('json.txt', 'r', encoding='ascii') as fin:
    data = json.loads(fin.read())
    print(data['menu']['hello'])
    print(data['menu']['flag'])
    print(data['menu']['count'])
    with open('json_out1.txt', 'w', encoding='ascii') as fout:
        fout.write(json.dumps(data, separators=(',', ':')))
    with open('json_out2.txt', 'w', encoding='ascii') as fout:
        fout.write(json.dumps(data, sort_keys=True, 
                 indent=4, separators=(',', ':')))

