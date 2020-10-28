# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 OS 文件/目录方法
os.dup() 方法
描述：
    os.dup()方法用于复制文件描述符fd。
语法：
    os.dup(fd)
    参数：
        fd -- 文件描述符
返回值：
    返回复制的文件描述符。
'''
import os, sys

if __name__ == "__main__":
    # 打开文件
    fd = os.open("tmp/foo.txt", os.O_RDWR | os.O_CREAT)

    # 复制文件描述符
    d_fd = os.dup(fd)

    # 使用复制的文件描述符写入文件
    os.write(d_fd, "This is test".encode())

    # 关闭文件
    os.closerange(fd, d_fd)
    print("关闭所有文件成功!!")
