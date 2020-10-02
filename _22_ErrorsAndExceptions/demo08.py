# -*- coding: UTF-8 -*-
# author: chenyongjun

try:
    raise KeyboardInterrupt
except KeyboardInterrupt as e:
    raise e
finally:
    print('Goodbye, world!')
