# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 输入和输出
文件对象的方法
    本节中剩下的例子假设已经创建了一个称为f的文件对象。
    f.readline()
        f.readline()会从文件中读取单独的一行。换行符为"\n"。f.readline()如果返回一个空字符串, 说明已经已经读取到最后一行。
'''
if __name__ == "__main__":
    # 打开一个文件
    f = open("tmp/foo.txt", "r")

    # 从文件中读取一行数据
    foo = f.readline()
    print(foo)

    # 关闭打开的文件
    f.close()
