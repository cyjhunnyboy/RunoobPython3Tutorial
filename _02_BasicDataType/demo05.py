# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
Tuple（元组）
    元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号()里，元素之间用逗号隔开。
    元组中的元素类型也可以不相同
    元组与字符串类似，可以被索引且下标索引从0开始，-1为从末尾开始的位置。也可以进行截取
    其实，可以把字符串看作一种特殊的元组。
    虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。

    string、list和tuple都属于sequence（序列）。
    注意：
    1、与字符串一样，元组的元素不能修改。
    2、元组也可以被索引和切片，方法一样。
    3、注意构造包含0或1个元素的元组的特殊语法规则。
    4、元组也可以使用+操作符进行拼接。
'''
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

    tup = (1, 2, 3, 4, 5, 6)
    print(tup[0])
    print(tup[1:5])
    # 修改元组元素的操作是非法的
    # tup[0] = 11

    # 构造包含0个或1个元素的元组比较特殊
    # 所以有一些额外的语法规则
    # 空元组
    tup1 = ()
    # 一个元素，需要在元素后添加逗号
    tup2 = (20,)
