# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 输入和输出
文件对象的方法
    本节中剩下的例子假设已经创建了一个称为f的文件对象。
    with关键字
        当处理一个文件对象时, 使用with关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。而且写起来也比try - finally语句块要简短
    文件对象还有其他方法, 如isatty()和trucate(), 但这些通常比较少用。
'''
if __name__ == "__main__":
    with open("tmp/foo.txt", "r+") as f:
        s = f.read()
        print(s, end="")
        f.write("My name is Jack!\n")
