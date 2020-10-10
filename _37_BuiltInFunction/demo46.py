# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python format 格式化函数
描述：
    Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能
    基本语法是通过 {} 和 : 来代替以前的 %
    format 函数可以接受不限个参数，位置可以不按顺序
'''


class AssignValue(object):

    def __init__(self, value):
        self.value = value


if __name__ == "__main__":
    # 不设置指定位置，按默认顺序
    print("{} {}".format("hello", "world"))
    # 设置指定位置
    print("{0} {1}".format("hello", "world"))
    # 设置指定位置
    print("{1} {0} {1}".format("hello", "world"))

    # 也可以设置参数
    print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
    # 通过字典设置参数
    site = {"name": "菜鸟教程", "url": "www.runoob.com"}
    print("网站名：{name}, 地址 {url}".format(**site))
    # 通过列表索引设置参数
    my_list = ['菜鸟教程', 'www.runoob.com']
    # "0" 是必须的
    print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))

    # 也可以向 str.format() 传入对象
    my_value = AssignValue(6)
    # "0" 是可选的
    print('value 为: {0.value}'.format(my_value))
