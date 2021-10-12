# -*- coding: UTF-8 -*-
# author: chenyongjun

"""
    Python3 字典
        字典内置方法
            Python3 字典copy()方法
                描述：
                    Python字典copy()函数返回一个字典的浅复制
                语法：
                    dict.copy()
                    参数：
                        NA
                返回值：
                    返回一个字典的浅复制

            注意：直接赋值和copy的区别
"""
if __name__ == "__main__":
    dict_1 = {"user": "runoob", "num": [1, 2, 3]}

    # 浅拷贝: 引用对象
    dict_2 = dict_1
    # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
    dict_3 = dict_1.copy()

    # 修改data数据
    dict_1["user"] = "root"
    dict_1["num"].remove(1)

    # 输出结果
    # 实例中dict_2其实是dict_1的引用（别名）。所以输出结果都是一致的。
    # dict_3父对象进行了深拷贝，不会随dict_1修改而修改，子对象是浅拷贝所以随dict_1的修改而修改
    print(dict_1)
    print(dict_2)
    print(dict_3)
    print("dict_1的id值是：", id(dict_1))
    print("dict_2的id值是：", id(dict_2))
    print("dict_3的id值是：", id(dict_3))
    print("dict_1['num']的id值是：", id(dict_1["num"]))
    print("dict_2['num']的id值是：", id(dict_2["num"]))
    print("dict_3['num']的id值是：", id(dict_3["num"]))