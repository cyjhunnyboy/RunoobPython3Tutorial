# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 输入和输出
文件对象的方法
    本节中剩下的例子假设已经创建了一个称为f的文件对象。
    f.read()
        为了读取一个文件的内容，调用f.read(size)，这将读取一定数目的数据, 然后作为字符串或字节对象返回。
        size是一个可选的数字类型的参数。当size被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。

    以下实例假定文件foo.txt已存在（上面实例中已创建）
'''
if __name__ == "__main__":
    # 打开一个文件
    f = open("tmp/foo.txt", "r")

    foo = f.read()
    print(foo)

    # 关闭打开的文件
    f.close()
