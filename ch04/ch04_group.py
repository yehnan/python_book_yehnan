

def group(iterable, size):
    result = []
    li = list(iterable)
    length = len(li)
    for i in range(0, length, size):
        result.append(li[i:i+size])
    return result

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
# [[1, 2, 3, 4], [5, 6, 7, 8], [9]]

print(group(range(20), 5))
