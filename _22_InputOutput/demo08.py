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

    # 读取文件中所有行数据，包括换行符
    # 并以列表形式返回读取的数据
    foos = f.readlines()
    print(foos)

    # 关闭打开的文件
    f.close()
