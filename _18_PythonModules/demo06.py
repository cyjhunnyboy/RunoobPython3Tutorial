# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 模块
from … import * 语句
    把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
        from modname import *

    这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。
'''
from _18_PythonModules.tool.fibonacci import *

if __name__ == "__main__":
    fib(1000)
    print(fib2(100))
