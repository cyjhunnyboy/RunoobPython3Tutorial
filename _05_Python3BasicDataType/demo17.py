# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 基本数据类型
        Tuple（元组）
            元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号()里，元素之间用逗号隔开。
            元组中的元素类型也可以不相同
"""
if __name__ == "__main__":
    # 元组中的元素类型也可以不相同
    tuple_a = ('abcd', 786, 2.23, 'runoob', 70.2)
    tiny_tuple = (123, 'runoob')

    # 输出完整元组
    print(tuple_a)
    # 输出元组的第一个元素
    print(tuple_a[0])
    # 输出从第二个元素开始到第三个元素
    print(tuple_a[1:3])
    # 输出从第三个元素开始的所有元素
    print(tuple_a[2:])

    # 输出两次元组
    print(tiny_tuple * 2)

    # 连接元组
    print(tuple_a + tiny_tuple)
