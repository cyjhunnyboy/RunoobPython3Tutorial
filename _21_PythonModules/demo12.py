# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 模块
标准模块
    Python本身带着一些标准的模块库，在Python库参考文档中将会介绍到（就是后面的"库参考文档"）。
    有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统级调用也没问题。
    这些组件会根据不同的操作系统进行不同形式的配置，比如winreg这个模块就只会提供给Windows系统。
    应该注意到这有一个特别的模块sys ，它内置在每一个Python解析器中。
    变量sys.ps1和sys.ps2定义了主提示符和副提示符所对应的字符串
'''
import sys

if __name__ == "__main__":
    print(sys.ps1)
    print(sys.ps2)
