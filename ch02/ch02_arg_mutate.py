
def my_len(seq):
    n = 0
    for x in seq:
        n += 1
    return n

data = [-30.2, -22.5, 15.8, 23.7, 35.2]
print(data)
def ctof(temp):
    n = my_len(temp)
    i = 0
    while i < n:
        temp[i] = temp[i] * 9.0 / 5.0 + 32
        i += 1

ctof(data)
print(data)



