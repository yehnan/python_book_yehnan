

a = 1
b = 2
c = 3

def foo(x, y):
    a = 'aaa'
    b = 'bbb'
    print(locals())

print(globals())
print('*' * 10)
foo(80, 91)
