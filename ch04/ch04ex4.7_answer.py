

# def group(iterable, size):
    # result = []
    # li = list(iterable) 
    # length = len(li)
    # for i in range(0, length, size): 
        # result.append(li[i:i+size])  
    # return result

def group(iterable, size):
    result = []
    it = iter(iterable)
    while True:
        temp = []
        try:
            for _ in range(size):
                temp.append(next(it))
            result.append(temp)
        except StopIteration:
            if temp != []:
                result.append(temp)
            break
    return result


if __name__ == '__main__':
    # simple tests
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if group(li, 3) != [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]:
        print('Failed')
    if group(li, 4) != [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]:
        print('Failed')
    if group(li, 1) != [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]:
        print('Failed')

    if group(li, 3) != [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]:
        print('Failed')
    if group(li, 4) != [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]:
        print('Failed')
    if group(li, 1) != [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]:
        print('Failed')


