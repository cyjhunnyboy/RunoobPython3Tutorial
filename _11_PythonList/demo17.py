# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python3 List pop()方法
            描述：
                pop()函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
            语法：
                list.pop([index=-1]])
                参数
                    index -- 可选参数，要移除列表元素的索引值，
                             不能超过列表总长度，默认为index=-1，删除最后一个列表值
            返回值：
                该方法返回从列表中移除的元素对象
"""
if __name__ == "__main__":
    list1 = ["Google", "Runoob", "Taobao"]
    web = list1.pop(2)
    print("删除的元素为：", web)
    print("列表现在为：", list1)
    web = list1.pop(1)
    print("删除的元素为：", web)
    print("列表现在为：", list1)
    # IndexError: pop index out of range
    # web = list1.pop(1)
    web = list1.pop()
    print("删除的元素为：", web)
    print("列表现在为：", list1)
