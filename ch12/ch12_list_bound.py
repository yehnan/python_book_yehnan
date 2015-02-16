

# def get(li, n):
    # try:
        # li[n]
    # except IndexError as e:
        # print('get IndexError')
        # raise 

def get(li, n):
    try:
        li[n]
    except IndexError as e:
        s = 'index %d, len of list is %d' % (n, len(li))
        raise IndexError(s) from e

li = [0, 1, 2]
get(li, 99)

