# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python3 List sort()方法
            描述：
                sort()函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
            语法：
                list.sort(key=None, reverse=False)
                参数：
                    key -- 主要是用来进行比较的元素，只有一个参数，
                           具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
                    reverse -- 排序规则，reverse=True降序，reverse=False升序（默认）
            返回值：
                该方法没有返回值，但是会对列表的对象进行排序
"""


# 获取列表的第二个元素
def take_second(elem):
    return elem[1]


if __name__ == "__main__":
    aList = ["Google", "Runoob", "Taobao", "Facebook"]
    print("排序前的列表为：", aList)
    aList.sort()
    print("默认排序（升序）后的列表为：", aList)

    print("=====================================")

    # 列表
    vowels = ['e', 'a', 'u', 'o', 'i']
    print("排序前的列表为：", vowels)
    # 降序
    vowels.sort(reverse=True)
    # 输出结果
    print("降序排序后的列表为：", vowels)

    print("=====================================")

    # 列表
    random = [(2, 2), (3, 4), (4, 1), (1, 3)]
    print("排序前的列表为：", random)
    # 指定第二个元素排序
    random.sort(key=take_second)
    # 输出类别
    print("按指定第二个元素排序后的列表为：", random)
