# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 循环语句
        Python中的循环语句有for和while
        while循环
            Python中while语句的一般形式：
                while 判断条件(condition)：
                    执行语句(statements)……

        同样需要注意冒号和缩进。另外，在Python中没有do..while循环
"""
if __name__ == "__main__":
    # 打印1~10范围内的奇数
    a = 1
    while a < 10:
        print(a)
        a += 2
