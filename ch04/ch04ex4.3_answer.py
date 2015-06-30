

def f(li):
    result = []
    for i, e in enumerate(li):
        result.append(e+i)
    
    return result
    
if __name__ == '__main__':
    # simple tests
    li = [8, 4, 1, 7]
    if f(li) != [8, 5, 3, 10]:
        print('Failed')

    li = [10, 11, 12, 13]
    if f(li) != [10, 12, 14, 16]:
        print('Failed')

        