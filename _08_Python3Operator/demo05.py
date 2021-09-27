# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 运算符
        Python逻辑运算符
            假设变量a为10, b为20
            and     (x and y)       布尔"与"，如果x为False，x and y返回False，否则它返回y的计算值。        实例：(a and b)返回20
            or      (x or y)        布尔"或"--如果x是True，它返回x的值，否则它返回y的计算值。              实例：(a or b)返回10
            not     (not x)         布尔"非"--如果x为True，返回False。如果x为False，它返回True。          实例：not(a and b)返回False
"""
if __name__ == "__main__":
    a = 10
    b = 20

    if a and b:
        print("1-变量a和b都为true")
    else:
        print("1-变量a和b有一个不为true")

    if a or b:
        print("2-变量a和b都为true，或其中一个变量为true")
    else:
        print("2-变量a和b都不为true")

    # 修改变量a的值
    a = 0
    if a and b:
        print("3-变量a和b都为true")
    else:
        print("3-变量a和b有一个不为true")

    if a or b:
        print("4-变量a和b都为true，或其中一个变量为true")
    else:
        print("4-变量a和b都不为true")

    if not (a and b):
        print("5-变量a和b都为false，或其中一个变量为false")
    else:
        print("5-变量a和b都为true")
