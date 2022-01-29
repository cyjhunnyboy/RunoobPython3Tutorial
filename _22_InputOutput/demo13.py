# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 输入和输出
文件对象的方法
    本节中剩下的例子假设已经创建了一个称为f的文件对象。
    f.tell()
        f.tell()返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
'''
if __name__ == "__main__":
    # 打开一个文件
    f = open("tmp/foo.txt", "r")

    foo = f.read()
    print(foo)

    # 返回文件对象当前所处的位置，
    # 它是从文件开头开始算起的字节数。
    print(f.tell())

    # 关闭打开的文件
    f.close()
