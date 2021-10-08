# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 数字(Number)
        Python3 shuffle() 函数
            描述：
                shuffle()方法将序列的所有元素随机排序
            语法：
                import random
                random.shuffle(lst)
                参数：
                    lst -- 列表
            返回值：
                返回None

        注意：shuffle()是不能直接访问的，需要导入random模块，然后通过random静态对象调用该方法。
"""
import random

if __name__ == "__main__":
    list1 = [20, 16, 10, 5]

    random.shuffle(list1)
    print("随机排序列表：", list1)

    random.shuffle(list1)
    print("随机排序列表：", list1)
