# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 OS 文件/目录方法
 os.chdir() 方法
 描述：
    os.chdir()方法用于改变当前工作目录到指定的路径。
语法：
    os.chdir(path)
    参数：
        path -- 要切换到的新路径。
返回值：
    如果允许访问返回True , 否则返回False。
'''
import os, sys

if __name__ == "__main__":
    path = "/tmp"

    # 查看当前工作目录
    retval = os.getcwd()
    print("当前工作目录为 %s" % retval)

    # 修改当前工作目录
    os.chdir(path)

    # 查看修改后的工作目录
    retval = os.getcwd()

    print("目录修改成功 %s" % retval)
