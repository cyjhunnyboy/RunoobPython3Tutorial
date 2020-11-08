# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python 按键(key)或值(value)对字典进行排序
    给定一个字典，然后按键(key)或值(value)对字典进行排序。
'''


def dictionairy():
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("按键(key)排序：")

    # sorted(key_value)返回重新排序的列表
    # 字典按键排序
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")


def main():
    # 调用函数
    dictionairy()


# 主函数
if __name__ == "__main__":
    main()
