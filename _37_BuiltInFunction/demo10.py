# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python dir() 函数
描述：
    dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
    带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。
    如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
语法：
    dir([object])
    参数：
        object -- 对象、变量、类型
返回值：
    返回模块的属性列表
'''
if __name__ == "__main__":
    # 获得当前模块的属性列表
    print(dir())
