# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 输入和输出
文件对象的方法
    本节中剩下的例子假设已经创建了一个称为f的文件对象。
    f.seek()
        如果要改变文件当前的位置, 可以使用f.seek(offset, from_what)函数。
        from_what的值, 如果是0表示开头, 如果是1表示当前位置, 2表示文件的结尾，例如：
        seek(x,0)：从起始位置即文件首行首字符开始移动x个字符
        seek(x,1)：表示从当前位置往后移动x个字符
        seek(-x,2)：表示从文件的结尾往前移动x个字符
        from_what值为默认为0，即文件开头
'''
if __name__ == "__main__":
    f = open("tmp/foo.txt", "rb+")
    f.write(b'0123456789abcdef')

    # 移动到文件的第六个字节
    f.seek(5)
    print(f.read(1))

    # 移动到文件的倒数第三字节
    f.seek(-3, 2)
    print(f.read(1))

    # 关闭打开的文件
    f.close()
