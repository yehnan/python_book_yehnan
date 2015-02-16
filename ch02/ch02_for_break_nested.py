
data = [[33, 44, 55], [18381, 99781], [60, 70, 42, 91], [32, 51]]
total = 0
for x in data:
    for y in x:
        if 0 <= y <= 100:
            total += y
        else:
            break

print(total)
