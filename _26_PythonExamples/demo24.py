# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 九九乘法表
    print(end="")指定end参数的值，可以取消在末尾输出回车符，实现不换行
'''


def multiplicationtable():
    """控制台输出九九乘法表"""

    # 九九乘法表
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{}x{}={}\t".format(j, i, i * j), end="")
        print()


if __name__ == "__main__":
    # 九九乘法表
    multiplicationtable()
