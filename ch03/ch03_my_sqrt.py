
diff = 0.00001
def is_ok(n, ans):
    return abs(ans**2 - n) < diff
def get_better(n, ans):
    return ((float(n) / ans) + ans) / 2
def my_sqrt(n):
    ans = 1
    while not is_ok(n, ans):
        ans = get_better(n, ans)
    return ans

import math
print(my_sqrt(9))
print(math.sqrt(9))
print(my_sqrt(2))
print(math.sqrt(2))
print(my_sqrt(3))
print(math.sqrt(3))






