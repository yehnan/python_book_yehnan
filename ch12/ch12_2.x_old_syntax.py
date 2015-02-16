

# different in 2.x and 3.x
try:
    [0, 1, 2][999]
except IndexError, ValueError:
    print('hi')




