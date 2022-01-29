# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python bool() 函数
描述：
    bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False。
    bool 是 int 的子类。
语法：
    class bool([x])
    参数：
        x -- 要进行转换的参数
返回值：
    返回 True 或 False
'''
if __name__ == "__main__":
    print(bool())
    print(bool(0))
    print(bool(1))
    print(bool(2))

    # bool 是 int 子类
    print(issubclass(bool, int))
