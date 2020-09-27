# -*- coding: UTF-8 -*-
# author: chen_yong_jun

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
