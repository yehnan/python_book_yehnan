
li = [60, 73, 81, 95, 34]
t = (0, 1, 2, 3, 4, 5)
s = 'Learning Python is fun'
empty = []

def my_len(seq):
    n = 0
    for x in seq:
        n += 1
    return n

print(str(li) + ' length ' + str(my_len(li)))
print(str(t) + ' length ' + str(my_len(t)))
print(str(s) + ' length ' + str(my_len(s)))
print(str(empty) + ' length ' + str(my_len(empty)))
