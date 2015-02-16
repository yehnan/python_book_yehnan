
scores = [30, 99, 41, 55, 84]
scores_new = []
for x in scores:
    if x >= 90:
        scores_new += [x]
        continue
    x += 10
    if x >= 90:
        x = 90
    scores_new += [x]

print(scores)
print(scores_new)
