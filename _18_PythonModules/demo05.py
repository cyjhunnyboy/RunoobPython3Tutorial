# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 模块
from … import 语句
    Python的from语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
        from modname import name1[, name2[, ... nameN]]

    这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来。
'''
from _18_PythonModules.tool.fibonacci import fib, fib2

if __name__ == "__main__":
    fib(1000)
    print(fib2(100))
