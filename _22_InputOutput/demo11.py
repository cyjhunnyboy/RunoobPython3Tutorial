# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 输入和输出
文件对象的方法
    本节中剩下的例子假设已经创建了一个称为f的文件对象。
    f.write()
        f.write(string)将string写入到文件中, 然后返回写入的字符数
'''
if __name__ == "__main__":
    # 打开一个文件
    f = open("tmp/foo.txt", "w")

    count = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
    print(count)

    # 关闭打开的文件
    f.close()
