
def flatten(iterable):
    result = []
    for x in iterable:
        result.extend(x)
    return result


print(flatten([[0, 1, 2], [3, 4, 5], [6], [7, 8], [9]]))
print(flatten([[0, 1], [3, 5], [6], [7, 8], [9]]))
