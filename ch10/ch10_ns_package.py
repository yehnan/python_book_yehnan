

import sys
# sys.path.append('/cygdrive/d/yehnan/wr_python_drmaster/python_book_yehnan/ch10/path1')
# sys.path.append('/cygdrive/d/yehnan/wr_python_drmaster/python_book_yehnan/ch10/path2')
sys.path.append(r'D:\yehnan\wr_python_drmaster\python_book_yehnan\ch10\path1')
sys.path.append(r'D:\yehnan\wr_python_drmaster\python_book_yehnan\ch10\path2')

# import mymodule
# print(mymodule.__name__)
# print(mymodule.__file__)
# print(mymodule.__path__)

import mymodule.sub1
import mymodule.sub2

print(mymodule.sub1.foo())
print(mymodule.sub2.bar())
