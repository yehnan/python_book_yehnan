

def split_a(li, n):
    result = []
    for i in range(0, len(li), n):
        result.append(li[i:i+n])
    
    return result
    
def split_b(li, n):
    return [li[i:i+n] for i in range(0, len(li), n)]

if __name__ == '__main__':
    # simple tests
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if split_a(li, 3) != [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]:
        print('Failed')
    if split_a(li, 4) != [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]:
        print('Failed')
    if split_a(li, 1) != [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]:
        print('Failed')

    if split_b(li, 3) != [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]:
        print('Failed')
    if split_b(li, 4) != [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]:
        print('Failed')
    if split_b(li, 1) != [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]:
        print('Failed')
   