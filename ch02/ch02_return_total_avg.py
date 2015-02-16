
scores = [60, 73, 81, 95, 34]

def total_avg(scores, initial=0):
    n = 0
    total = initial
    for x in scores:
        total += x
        n += 1
    return (total, total/n)

print('total,avg ' + str(total_avg(scores)))

