# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python3 基本数据类型
        1、List（列表）
            列表截取的语法格式如下：
                变量[头下标:尾下标]
            索引值以0为开始值，-1为从末尾的开始位置。
                t = ['a', 'b', 'c', 'd', 'e']
                索引  0    1    2    3    4
                     -5   -4   -3   -2   -1

            加号+是列表连接运算符，星号*是重复操作
'''
if __name__ == "__main__":
    list_a = ['abcd', 786, 2.23, 'runoob', 70.2]
    tiny_list = [123, 'runoob']

    # 输出完整列表
    print(list_a)
    # 输出列表第一个元素
    print(list_a[0])
    # 从第二个开始输出到第三个元素
    print(list_a[1:3])
    # 输出从第三个元素开始的所有元素
    print(list_a[2:])

    # 星号*是重复操作
    # 输出两次列表
    print(tiny_list * 2)

    # 加号+是列表连接运算符
    # 连接列表
    print(list_a + tiny_list)
