
names_scores = (('Amy', 82, 90), ('John', 33, 64), ('Zoe', 91, 94))
highs = []
for x, y, z in names_scores:
    if y >= 90 and z >= 90:
        highs += [x, y, z]

print(highs)
