

import sys
sys.path.append('/cygdrive/d/yehnan/wr_python_drmaster/python_book_yehnan/ch10')

# import package_example.formats.bar
# square = package_example.formats.bar.square

# from bar import square

from . import bar
square = bar.square

# from .bar import square


def sos(a, b):
    return square(a) + square(b)

    
if __name__ == '__main__':
    if sos(3, 4) != 25:
        print('error')
    else:
        print('ok')


