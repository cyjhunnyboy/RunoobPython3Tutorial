# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置方法
            Python3 字典clear()方法
                描述：Python字典clear()函数用于删除字典内所有元素。
                语法：
                    dict.clear()
                    参数：
                        NA
                返回值：
                    该函数没有任何返回值
"""
if __name__ == "__main__":
    dict_1 = {"Name": "Zara", "Age": 7}

    print("字典长度：%d" % len(dict_1))
    dict_1.clear()
    print("字典删除后长度：%d" % len(dict_1))
