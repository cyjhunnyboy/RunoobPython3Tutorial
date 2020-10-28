# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 OS 文件/目录方法
os.fchdir() 方法
描述：
    os.fchdir()方法通过文件描述符改变当前工作目录。
    Unix上可用。
语法：
    os.fchdir(fd)
    参数：
        fd -- 文件描述符
返回值：
    该方法没有返回值。
'''
import os, sys

if __name__ == "__main__":
    # 首先到目录"/var/www/html"
    os.chdir("/var/www/html")

    # 输出当前目录
    print("当前工作目录为：%s" % os.getcwd())

    # 打开新目录"/tmp"
    fd = os.open("/tmp", os.O_RDONLY)

    # 使用os.fchdir()方法修改到新目录
    os.fchdir(fd)

    # 输出当前目录
    print("当前工作目录为：%s" % os.getcwd())

    # 关闭打开的目录
    os.close(fd)
