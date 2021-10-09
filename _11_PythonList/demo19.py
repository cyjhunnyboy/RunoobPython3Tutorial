# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python3 List reverse()方法
            描述：
                reverse()函数用于反向列表中元素
            语法：
                list.reverse()
                参数
                    NA
            返回值：
                该方法没有返回值，但是会对列表的元素进行反向排序
"""
if __name__ == "__main__":
    list1 = ["Google", "Runoob", "Taobao", "Baidu"]
    list1.reverse()
    print("列表反转后：", list1)
