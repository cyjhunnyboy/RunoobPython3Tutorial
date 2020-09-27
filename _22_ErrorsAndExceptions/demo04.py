# -*- coding: UTF-8 -*-
# author: chen_yong_jun


def this_fails():
    x = 1 / 0
    print("The result of divide is: ", x)


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
