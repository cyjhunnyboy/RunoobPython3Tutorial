# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 OS 文件/目录方法
os.dup2() 方法
描述：
    os.dup2()方法用于将一个文件描述符fd复制到另一个 fd2。
    Unix, Windows上可用。
语法：
    os.dup2(fd, fd2)
    参数：
        fd -- 要被复制的文件描述符
        fd2 -- 复制的文件描述符
返回值：
    没有返回值。
'''
import os

if __name__ == "__main__":
    # 打开一个文件
    f = open("tmp/foo.txt", "a")

    # 将这个文件描述符代表的文件，传递给1描述符指向的文件（也就是stdout）
    os.dup2(f.fileno(), 1)

    # 关闭文件
    f.close()

    # print输出到标准输出流，就是文件描述符1
    print("runoob")
    print("google")
