# -*- coding: UTF-8 -*-
# author: chen_yong_jun

try:
    raise KeyboardInterrupt
except KeyboardInterrupt as e:
    raise e
finally:
    print('Goodbye, world!')
