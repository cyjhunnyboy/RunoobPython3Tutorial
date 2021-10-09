# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python3 List clear()方法
            描述：
                clear()函数用于清空列表，类似于del a[:]
            语法：
                list.clear()
                参数
                    无
            返回值：
                该方法没有返回值
"""
if __name__ == "__main__":
    list1 = ["Google", "Runoob", "Taobao", "Baidu"]
    print("执行list.clear()方法前列表为：", list1)
    list1.clear()
    print("执行list.clear()方法后列表为：", list1)
