# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 列表
        Python3 List copy()方法
            描述：
                copy()函数用于复制列表，类似于a[:]
            语法
                list.copy()
                参数
                    无
            返回值：
                返回复制后的新列表
"""
if __name__ == "__main__":
    list_1 = ["Google", "Runoob", "Taobao", "Baidu"]
    print("list_1列表为：", list_1)
    list_2 = list_1.copy()
    print("list_2列表为：", list_2)
