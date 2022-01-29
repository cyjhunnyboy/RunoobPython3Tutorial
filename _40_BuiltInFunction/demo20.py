# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 input() 函数
描述：
    Python3.x 中 input() 函数接受一个标准输入数据，返回为 string 类型。
    注意：在 Python3.x 中 raw_input() 和 input() 进行了整合，去除了 raw_input( )，
    仅保留了input( )函数，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型
语法：
    input([prompt])
    参数说明：
        prompt: 提示信息
'''
if __name__ == "__main__":
    # 输入整数
    a = input("input:")
    print(a)
    print(type(a))

    # 输入字符串
    b = input("input:")
    print(b)
    print(type(b))
