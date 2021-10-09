# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python3 List min()方法
            描述：
                min()方法返回列表元素中的最小值
            语法：
                max(list)
                参数：
                    list -- 要返回最小值的列表
            返回值：
                返回列表元素中的最小值
"""
if __name__ == "__main__":
    list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
    print("list1最小元素值：", min(list1))
    print("list2最小元素值：", min(list2))
