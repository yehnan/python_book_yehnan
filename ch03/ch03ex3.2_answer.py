

def f(n):
    if n < 0:
        n = 0
    elif n > 255:
        n = 255
        
    if 0 <= n <= 130:
        return int(n / 130.0 * 60.0)
    elif 130 < n < 200:
        return int((n - 130) / 70.0 * 15.0 + 60)
    else: # 200 <= n <= 255
        return int((n - 200) / 55.0 * 15.0 + 85)


if __name__ == '__main__':
    # simple tests
    if f(0) != 0:
        print('Failed')
    if f(130) != 60:
        print('Failed')
    if f(200) != 85:
        print('Failed')
    if f(255) != 100:
        print('Failed')
