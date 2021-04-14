

li_a = [1, 5, 9, 11, 22, 4, 9, 1, 3, 7]
li_b = [9, 4, 55, 66, 1, 11, 77]

def f(li_a, li_b):
    li = []
    for n in li_a:
        if n in li_b and n not in li:
            li += [n]
    return li
    
print(f(li_a, li_b))


