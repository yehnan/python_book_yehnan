

# use for loop
for x in range(2, 9+1):
    for y in range(1, 9+1):
        print('%d * %d = %d' % (x, y, x*y))

# use while loop
x = 2
while x < 9+1:
    y = 1
    while y < 9+1:
        print('%d * %d = %d' % (x, y, x*y))
        y += 1
    x += 1
