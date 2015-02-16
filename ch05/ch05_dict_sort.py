

d = {'Amy': (45, 60, 33), 'Bob': (50, 62, 78), 
     'Cathy': (62, 98, 87), 'David': (45, 22, 12),
     'Eason': (63, 55, 71), 'Fred': (78, 79, 32)}

for k in sorted(d.keys()):
    print(k, d[k])

def foo(item):
    return item[1][2]
for item in sorted(d.items(), key=foo):
    print(item)

def bar(item):
    return sum(item[1])
for item in sorted(d.items(), key=bar):
    print(item)


