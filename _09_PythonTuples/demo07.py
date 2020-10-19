# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Python3 元组
    元组索引，截取，因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素
    L = ("Google", "Taobao", "Runoob")
    Python表达式           结果                      描述
    L[2]                "Runoob"                    读取第三个元素
    L[-2]               "Taobao"                    反向读取，读取倒数第二个元素
    L[1:]               ("Taobao", "Runoob")        截取元素，从第二个开始后的所有元素
'''
if __name__ == "__main__":
    tuple_1 = ("Google", "Taobao", "Runoob")
    # 读取第三个元素
    print(tuple_1[2])
    # 反向读取，读取倒数第二个元素
    print(tuple_1[-2])
    # 截取元素，从第二个开始后的所有元素
    print(tuple_1[1:])
