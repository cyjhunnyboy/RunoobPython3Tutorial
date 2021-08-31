# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python3 基础语法
        1、import与from...import
            在python用import或者from...import来导入相应的模块。

            将整个模块(somemodule)导入，格式为：import somemodule
            从某个模块中导入某个函数,格式为：from somemodule import somefunction
            从某个模块中导入多个函数,格式为：from somemodule import firstfunc, secondfunc, thirdfunc
            将某个模块中的全部函数导入，格式为：from somemodule import *
'''
# 导入sys模块
import sys
# 导入sys模块的argv,path成员
# 导入特定的成员
from sys import argv, path

if __name__ == "__main__":
    print("================Python import mode==========================")
    print("命令行参数为:")
    for i in sys.argv:
        print(i)

    print("\n python 路径为", sys.path)
    print("================python from import===================================")
    # 因为已经导入path成员，所以此处引用时不需要加sys.path
    print("path:", path)
