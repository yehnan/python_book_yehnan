

def sq(n): return n**2
def even(n): return n % 2 == 0
def sum_sq_even(n):
    result = 0
    for i in range(1, n):
        if even(i):
            result += sq(i)
    return result

print(sum_sq_even(10))


