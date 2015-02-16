

def cumulative_sum(iterable, start=0):
    result = []
    acc = start
    for x in iterable:
        acc += x
        result.append(acc)
    return result


print(cumulative_sum(range(10+1)))
print(cumulative_sum(range(0, 1000, 100)))

