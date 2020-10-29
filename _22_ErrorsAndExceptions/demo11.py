# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 错误和异常
定义清理行为
    try语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。
'''
if __name__ == "__main__":
    try:
        raise KeyboardInterrupt
    except KeyboardInterrupt as e:
        raise e
    finally:
        print("Goodbye, world!")
