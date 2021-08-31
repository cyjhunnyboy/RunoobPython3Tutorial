# -*- coding: UTF-8 -*-
# author: chenyongjun

'''
    Python数据类型转换
        Python List list()方法
            描述：
                list()方法用于将元组转换为列表
                注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中
            语法：
                list(seq)
            参数：
                list -- 要转换为列表的元组
            返回值：
                返回列表
'''
if __name__ == "__main__":
    aTuple = (123, "Google", "Runoob", "Taobao")
    list1 = list(aTuple)
    print("列表元素：", list1)

    str_a = "Hello World"
    list2 = list(str_a)
    print("列表元素：", list2)
