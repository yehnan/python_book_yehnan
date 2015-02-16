

ALPHA_DEFAULT = 1.0
def color(red, green, blue, alpha=ALPHA_DEFAULT):
    # alpha = ...
    # ...
    print (red, green, blue, alpha)

def foo(x, y=[]):
    y.append(x)
    print(y)

foo(1)
foo(2)
foo(3)

def foo(x, y=None):
    if y is None:
        y = []
    y.append(x)
    print(y)

foo(1)
foo(2)
foo(3, [90, 91])