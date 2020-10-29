# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 错误和异常
预定义的清理行为
    一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。

    for line in open("myfile.txt"):
        print(line, end="")
    以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。

    关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法
'''
if __name__ == "__main__":
    with open("myfile.txt") as f:
        for line in f:
            print(line, end="")
