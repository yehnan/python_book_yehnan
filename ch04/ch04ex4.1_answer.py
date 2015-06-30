

def find_once(li):
    result = []
    for i, e in enumerate(li):
        if e not in li[:i] and e not in li[i+1:]:
            result.append(e)
    return result

if __name__ == '__main__':
    # simple tests
    li = [9, 5, 5, -4, 7, 6, 4, 1, -2, 0, 10, 9, 7]
    if find_once(li) != [-4, 6, 4, 1, -2, 0, 10]:
        print('Failed')
    
    li = [1, 1, -3, -3]
    if find_once(li) != []:
        print('Failed')
  
    li = [5, 6, 8, -3]
    if find_once(li) != [5, 6, 8, -3]:
        print('Failed')

    li = [-3, 8, 5, 6, 8, -3]
    if find_once(li) != [5, 6]:
        print('Failed')

        