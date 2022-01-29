# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 错误和异常
用户自定义异常
    创建一个新的异常类来拥有自己的异常。异常类继承自Exception类，可以直接继承，或者间接继承
'''


class MyError(Exception):
    """自定义异常类MyError"""

    # 类 Exception默认的 __init__()被覆盖
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


if __name__ == "__main__":
    try:
        raise MyError(2 * 2)
    except MyError as e:
        print("My exception occurred, value:", e.value)
