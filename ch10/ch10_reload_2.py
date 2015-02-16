
# -*- coding: utf-8 -*-
# from importlib import reload   # 3.4版
from imp import reload        # 3.4版之前
#                              # 2.x版直接使用內建函式reload
from time import sleep

import ch10_reload_module
from ch10_reload_module import pi
from ch10_reload_module import data
from ch10_reload_module import foo

while True:
    print('-' * 20)
    print(pi)
    print(data)
    print(foo(3, 4))
    sleep(5)
    reload(ch10_reload_module)

