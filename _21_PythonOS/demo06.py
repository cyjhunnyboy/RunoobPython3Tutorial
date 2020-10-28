# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 OS 文件/目录方法
os.chroot() 方法
描述：
    os.chroot()方法用于更改当前进程的根目录为指定的目录，使用该函数需要管理员权限。
    在unix中有效。
语法：
    os.chroot(path)
    参数：
        path -- 要设置为根目录的目录。
返回值：
    该方法没有返回值。
'''
import os, sys

if __name__ == "__main__":
    # 设置根目录为/tmp
    os.chroot("/tmp")

    print("修改根目录成功!!")
