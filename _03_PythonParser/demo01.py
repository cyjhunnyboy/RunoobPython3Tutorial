# -*- coding: UTF-8 -*-
# author: chenyongjun

# Python3 解释器

'''环境变量设置'''
# Linux/Unix环境变量，设置环境变量
#  PATH=$PATH:/usr/local/python3/bin/python3
# Window环境变量
# set path=%path%;C:\python34

# 交互式编程，启动Python
# python3
# 脚本式编程，运行hello.py文件
# python3 hello.py
# 在Linux/Unix系统中，你可以在脚本顶部添加以下命令让Python脚本可以像SHELL脚本一样可直接执行
# #! /usr/bin/env python3
# 然后修改脚本权限，使其有执行权限
# chmod +x hello.py
# ./hello.py
print("Hello, Python!")

flag = True
if flag:
    print("flag 条件为 True!")
else:
    print("flag 条件为 False!")
