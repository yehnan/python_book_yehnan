

def unique(iterable):
    result = []
    for x in iterable:
        if x not in result:
            result.append(x)
    return result


print(unique([1, 2, 1, 3, 2, 5, 5, 6, 1])) # [1, 2, 3, 5, 6]
print(unique([1, 2, 1, 3, 2, 5])) # [1, 2, 3, 5]
print(unique(range(10)))

