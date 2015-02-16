

li = [30, 41, 52, 63]

def sum(li):
    result = 0
    for x in li:
        result += x
    return result
print(sum(li))

def sum(li):
    if not li:
        return 0
    else:
        return li[0] + sum(li[1:])
print(sum(li))

(lambda li: [print(x) for x in li])(li)

print((lambda li: 
        (lambda f, r, li: f(f, r, li))
            (lambda f, r, li: f(f, r+li[0], li[1:]) if li else r, 0, li))
      (li))

print((lambda li: 
        (lambda f, r, i: f(f, r, i))
            (lambda f, r, i: f(f, r+li[i], i+1) if i < len(li) else r, 0, 0))
      (li))

