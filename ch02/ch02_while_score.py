
scores = [60, 73, 81, 95, 34]
n = 5
i = 0
total = 0
while i < 5:
    total += scores[i]
    i += 1

avg = total / n

print('total ' + str(total))
print('average ' + str(avg))
