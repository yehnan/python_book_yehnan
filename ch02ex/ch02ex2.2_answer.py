

# for loop
for x in range(2, 9+1):
    for y in range(1, 9+1):
        print(x, ' * ', y, ' = ', x*y)
        # print(str(x) + ' * ' + str(y) + ' = ' + str(x*y))
        # print('%d * %d = %d' % (x, y, x*y))

# while loop
x = 2
while x < 9+1:
    y = 1
    while y < 9+1:
        print(x, ' * ', y, ' = ', x*y)
        # print(str(x) + ' * ' + str(y) + ' = ' + str(x*y))
        # print('%d * %d = %d' % (x, y, x*y))
        y += 1
    x += 1
