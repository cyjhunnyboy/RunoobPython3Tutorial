# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 输入和输出
文件对象的方法
    本节中剩下的例子假设已经创建了一个称为f的文件对象。
    f.readlines()
        f.readlines() 将返回该文件中包含的所有行。
        如果设置可选参数sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
'''
if __name__ == "__main__":
    # 打开一个文件
    f = open("tmp/foo.txt", "r")

    # 另一种方式是迭代一个文件对象然后读取每行
    # 这个方法很简单, 但是并没有提供一个很好的控制。
    # 因为两者的处理机制不同, 最好不要混用。
    for line in f:
        print(line, end="")

    # 关闭打开的文件
    f.close()
