

li = [('apple', 25), ('orange', 10), ('fig', 12), ('apricot', 20)]

def by_name(item):
    return item[0]
def by_name_len(item):
    return len(item[0])
def by_value(item):
    return item[1]

print(sorted(li, key=by_name))
print(sorted(li, key=by_name_len))
print(sorted(li, key=by_value))

####  ####
#[('apple', 25), ('apricot', 20), ('fig', 12), ('orange', 10)]
#[('fig', 12), ('apple', 25), ('orange', 10), ('apricot', 20)]
#[('orange', 10), ('fig', 12), ('apricot', 20), ('apple', 25)]

print(sorted(li, key=lambda item: item[0]))
print(sorted(li, key=lambda item: len(item[0])))
print(sorted(li, key=lambda item: item[1]))

