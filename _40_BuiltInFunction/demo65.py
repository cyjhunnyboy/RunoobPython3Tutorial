# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python globals() 函数
描述：
    globals() 函数会以字典类型返回当前位置的全部全局变量
语法：
    globals()
    参数：
        无
返回值：
    返回全局变量的字典
'''
if __name__ == "__main__":
    a = "runoob"
    # globals 函数返回一个全局变量的字典，包括所有导入的变量
    print(globals())
