# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 输入和输出
文件对象的方法
    本节中剩下的例子假设已经创建了一个称为f的文件对象。
    f.close()
        在文本文件中(那些打开文件的模式下没有b的),只会相对于文件起始位置进行定位。
        当你处理完一个文件后, 调用f.close()来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。
'''
if __name__ == "__main__":
    # 打开一个文件
    f = open("tmp/foo.txt", "r")

    foo = f.read()
    print(foo)

    # 关闭打开的文件
    f.close()
