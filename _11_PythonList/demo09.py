# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python3 List max()方法
            描述：
                max()方法返回列表元素中的最大值
            语法：
                max(list)
                参数：
                    list -- 要返回最大值的列表
            返回值：
                返回列表元素中的最大值
"""
if __name__ == "__main__":
    list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
    print("list1最大元素值：", max(list1))
    print("list2最大元素值：", max(list2))
