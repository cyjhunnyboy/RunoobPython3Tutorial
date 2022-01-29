# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python help() 函数
描述：
    help() 函数用于查看函数或模块用途的详细说明。
语法：
    help([object])
    参数：
        object -- 对象；
返回值：
    返回对象帮助信息。
'''
if __name__ == "__main__":
    # 查看 sys 模块的帮助
    help('sys')

    # 查看 str 数据类型的帮助
    help("str")

    # 查看列表 list 帮助信息
    list1 = [1, 2, 3]
    help(list1)

    # 显示list的append方法的帮助
    help(list1.append(1))
