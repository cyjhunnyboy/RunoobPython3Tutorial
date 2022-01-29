# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 OS 文件/目录方法
os.close() 方法
描述：
    os.close()方法用于关闭指定的文件描述符fd。
语法：
    os.close(fd)
    参数：
        fd -- 文件描述符。
返回值：
    该方法没有返回值。
'''
import os, sys

if __name__ == "__main__":
    # 打开文件
    fd = os.open("tmp/foo.txt", os.O_RDWR | os.O_CREAT)

    #  写入字符串
    os.write(fd, b"This is test")

    # 关闭文件
    os.close(fd)
    print("关闭文件成功!!")
