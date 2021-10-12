# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置方法
            Python3 字典pop()方法
                描述：
                    Python字典pop()方法删除字典给定键key所对应的值，返回值为被删除的值。
                    key值必须给出。否则，返回default值。
                语法：
                    pop(key[,default])
                    参数
                        key: 要删除的键值
                        default: 如果没有key，返回default值
                返回值
                    返回被删除的值
"""
if __name__ == "__main__":
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    print("执行dict.pop()方法删除最后一个元素前字典为：", weekdays)
    # 括号里没有参数，表示删除list列表中最后一个元素
    lastday = weekdays.pop()
    print("执行dict.pop()方法删除最后一个元素后字典为：", weekdays)

    print("执行dict.pop(0)方法删第一个元素前字典为：", weekdays)
    # 0参数表示删除list列表中第一个元素
    lastday = weekdays.pop(0)
    print("执行dict.pop(0)方法删除第一个元素后字典为：", weekdays)
