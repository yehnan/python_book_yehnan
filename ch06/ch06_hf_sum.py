

def sum_number(start, end):
    result = 0
    while start <= end:
        result += start
        start += 1
    return result

def sum_square(start, end):
    result = 0
    while start <= end:
        result += start**2
        start += 1
    return result

# pi/8
def sum_pi(start, end):
    result = 0
    while start <= end:
        result += 1.0 / (start * (start+2))
        start += 4
    return result

def sum_hf(item, start, next, end):
    result = 0
    while start <= end:
        result += item(start)
        start = next(start)
    return result


def sum_number_r(start, end):
    if start > end:
        return 0
    else:
        return start + sum_number_r(start+1, end)
def sum_square_r(start, end):
    if start > end:
        return 0
    else:
        return start**2 + sum_square_r(start+1, end)
def sum_pi_r(start, end):
    if start > end:
        return 0
    else:
        return (1.0 / (start * (start+2))) + sum_pi_r(start+4, end)

def sum_hf_r(item, start, next, end):
    if start > end:
        return 0
    else:
        return item(start) + sum_hf_r(item, next(start), next, end)

if __name__ == '__main__':
    tests = [(0, 10), (100, 200), (2000, 2500)]
    for t in tests:
        fa = sum(range(t[0], t[1]+1))
        fb = sum_number(t[0], t[1])
        fc = sum_hf(lambda x: x, t[0], lambda i: i+1, t[1])
        fd = sum_number_r(t[0], t[1])
        fe = sum_hf_r(lambda x: x, t[0], lambda i: i+1, t[1])
        if fa == fb == fc == fd == fe:
            print('pass')
    for t in tests:
        fa = sum([x**2 for x in range(t[0], t[1]+1)])
        fb = sum_square(t[0], t[1])
        fc = sum_hf(lambda x: x**2, t[0], lambda i: i+1, t[1])
        fd = sum_square_r(t[0], t[1])
        fe = sum_hf_r(lambda x: x**2, t[0], lambda i: i+1, t[1])
        if fa == fb == fc == fd == fe:
            print('pass')
    for end in range(200, 205):
        print(sum_pi(1, end) * 8)
        print(sum_pi_r(1, end) * 8)
        print(sum_hf(lambda x: 1.0 / (x * (x+2)), 1, lambda i: i+4, end) * 8)
        print(sum_hf_r(lambda x: 1.0 / (x * (x+2)), 1, lambda i: i+4, end) * 8)
        print('---')

        
        