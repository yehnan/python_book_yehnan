
a, b, c = 3, 5, 7
x = None

if a < b:
    if b < c:
        x = c
    else:
        x = b
else:
    if a < c:
        x = c
    else:
        x = a

x
print(x)
