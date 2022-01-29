# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 File(文件) 方法
open()方法
描述：
    Python open()方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出OSError。
    注意：使用open()方法一定要保证关闭文件对象，即调用close()方法。
语法：
    open()函数常用形式是接收两个参数：文件名(file)和模式(mode)。
        open(file, mode='r')
    完整的语法格式为：
        open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
        参数说明：
            file: 必需，文件路径（相对或者绝对路径）。
            mode: 可选，文件打开模式
            buffering: 设置缓冲
            encoding: 一般使用utf8
            errors: 报错级别
            newline: 区分换行符
            closefd: 传入的file参数类型
            opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

    mode参数有：
    模式	    描述
    t       文本模式（默认）。
    x       写模式，新建一个文件，如果该文件已存在则会报错。
    b       二进制模式。
    +       打开一个文件进行更新(可读可写)。
    U       通用换行模式（Python 3不支持）。
    r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    rb	    以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
    r+	    打开一个文件用于读写。文件指针将会放在文件的开头。
    rb+	    以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
    w	    打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，
            即原有内容会被删除。如果该文件不存在，创建新文件。
    wb	    以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，
            并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    w+	    打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，
            即原有内容会被删除。如果该文件不存在，创建新文件。
    wb+	    以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，
            即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
    a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，
            新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    ab	    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
            也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    a+	    打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。
            文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    ab+	    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
            如果该文件不存在，创建新文件用于读写。

    默认为文本模式，如果要以二进制模式打开，加上b。
'''
if __name__ == "__main__":
    # 打开文件
    f = open("tmp/foo.txt", "a+")
    print("文件名为: ", f.name)

    # 写入文件
    count = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
    print(count)

    # 读取文件
    f.seek(0)
    foo = f.read()
    print(foo)

    # 关闭文件
    f.close()
