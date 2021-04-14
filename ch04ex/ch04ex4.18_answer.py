

def is_palindrome(n):
    ns = str(n)
    a, b = 0, len(ns)-1
    while a < b:
        if ns[a] != ns[b]:
            return False
        else:
            a += 1
            b -= 1
    return True

def is_palindrome_2(n):
    ns = str(n)
    ns_r = ''.join(reversed(ns))
    return ns == ns_r

print(sum([1 for i in range(10, 99+1) if is_palindrome(i)]))
print(sum([1 for i in range(100, 999+1) if is_palindrome(i)]))
print(sum([1 for i in range(1000, 9999+1) if is_palindrome(i)]))

