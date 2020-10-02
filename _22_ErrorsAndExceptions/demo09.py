# -*- coding: UTF-8 -*-
# author: chenyongjun


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(e)
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 1)
divide(2, 0)
divide("2", "1")
