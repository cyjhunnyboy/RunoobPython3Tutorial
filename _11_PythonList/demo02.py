# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        访问列表中的值
            与字符串的索引一样，列表索引从0开始，第二个索引是1，依此类推
            通过索引列表可以进行截取、组合等操作
            索引也可以从尾部开始，最后一个元素的索引为-1，往前一位为-2，以此类推
            使用下标索引来访问列表中的值，同样你也可以使用方括号 [] 的形式截取字符
"""
if __name__ == "__main__":
    list_1 = ["red", "green", "blue", "yellow", "white", "black"]
    # 与字符串的索引一样，列表索引从0开始，第二个索引是1，依此类推
    print(list_1[0])
    print(list_1[1])
    print(list_1[2])
    print(list_1[3])
    print(list_1[4])
    print(list_1[5])

    print("=========")

    # 索引也可以从尾部开始，最后一个元素的索引为-1，往前一位为-2，以此类推
    print(list_1[-1])
    print(list_1[-2])
    print(list_1[-3])
    print(list_1[-4])
    print(list_1[-5])
    print(list_1[-6])

    print("=========")

    # 使用下标索引来访问列表中的值，同样你也可以使用方括号[]的形式截取字符
    nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print(nums[0:4])
    # 使用负数索引值截取
    list_2 = ["Google", "Runoob", "Zhihu", "Taobao", "Wiki"]
    # 读取第二位
    print("list_2[1]：", list_2[1])
    # 从第二位开始（包含）截取到倒数第二位（不包含）
    print("list_2[1:-2]：", list_2[1:-2])
