# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 解释器
        环境变量设置
            1、Linux/Unix环境变量，设置环境变量
               PATH=$PATH:/usr/local/python3/bin/python3
            2、Window环境变量
               set path=%path%;C:\python34

        互式编程，启动Python
            1、python3
            2、脚本式编程，运行hello.py文件
            3、python3 hello.py
            4、在Linux/Unix系统中，你可以在脚本顶部添加以下命令让Python脚本可以像SHELL脚本一样可直接执行
               4-1、#! /usr/bin/env python3
               4-2、然后修改脚本权限，使其有执行权限
                    chmod +x hello.py
               4-3、./hello.py
"""
if __name__ == "__main__":
    print("Hello, Python!")
    flag = True
    if flag:
        print("flag 条件为 True!")
    else:
        print("flag 条件为 False!")
