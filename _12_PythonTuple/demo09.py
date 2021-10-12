# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 元组
        元组索引，截取
            因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素

            tuple_1 = ("Google", "Taobao", "Runoob", "Wiki", "Weibo", "Weixin")

               <------------------------------------------------
               -6        -5        -4      -3       -2       -1
            "Google", "Taobao", "Runoob", "Wiki", "Weibo", "Weixin"
                0         1         2       3        4        5
               ------------------------------------------------->
"""
if __name__ == "__main__":
    tuple_1 = ("Google", "Taobao", "Runoob", "Wiki", "Weibo", "Weixin")

    # 读取第二个元素
    print(tuple_1[1])

    # 反向读取，读取倒数第二个元素
    print(tuple_1[-2])

    # 截取元素，从第二个开始后的所有元素
    print(tuple_1[1:])

    # 截取元素，从第二个开始到第四个元素（索引为3）
    print(tuple_1[1:4])
