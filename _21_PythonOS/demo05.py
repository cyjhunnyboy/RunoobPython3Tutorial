# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 OS 文件/目录方法
os.chown() 方法
描述：
    os.chown()方法用于更改文件所有者，如果不修改可以设置为-1, 你需要超级用户权限来执行权限修改操作。
    只支持在Unix下使用。
语法：
    os.chown(path, uid, gid)
    参数：
        path -- 设置权限的文件路径
        uid -- 所属用户ID
        gid -- 所属用户组ID
返回值：
    该方法没有返回值。
'''
import os, sys

if __name__ == "__main__":
    # 假定/tmp/foo.txt文件存在.
    # 设置所有者ID为100
    os.chown("tmp/foo.txt", 100, -1)

    print("修改权限成功!!")
