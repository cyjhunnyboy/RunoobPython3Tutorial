# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 模块

import 语句
    想使用Python源文件，只需在另一个源文件里执行import语句
    语法格式如下：
        import module1[, module2[,... moduleN]
        当解释器遇到import语句，如果模块在当前的搜索路径就会被导入。
        搜索路径是一个解释器会先进行搜索的所有目录的列表。如想要导入模块support，需要把命令放在脚本的顶端
'''
# 导入模块
import _18_PythonModules.tool.support

if __name__ == "__main__":
    # 现在可以调用模块里包含的函数了
    support.print_func("Runoob")
